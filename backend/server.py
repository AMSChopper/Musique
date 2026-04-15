from fastapi import FastAPI, APIRouter, HTTPException, Query
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
import os
import logging
from pathlib import Path
from pydantic import BaseModel, Field, ConfigDict
from typing import List, Optional
import uuid
from datetime import datetime, timezone
import httpx
from bs4 import BeautifulSoup
import random
from songwriting_credits import FAMOUS_SONGWRITING_CREDITS

ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

# MongoDB connection
mongo_url = os.environ['MONGO_URL']
client = AsyncIOMotorClient(mongo_url)
db = client[os.environ['DB_NAME']]

# Discogs API token
DISCOGS_TOKEN = os.environ.get('DISCOGS_TOKEN', '')

# Genius API token
GENIUS_TOKEN = os.environ.get('GENIUS_TOKEN', '')

# Create the main app
app = FastAPI()

# Create a router with the /api prefix
api_router = APIRouter(prefix="/api")

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Deezer API base URL
DEEZER_API = "https://api.deezer.com"

# User agent for web scraping
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

# ==================== MODELS ====================

class Artist(BaseModel):
    id: int
    name: str
    picture: Optional[str] = None
    picture_medium: Optional[str] = None
    picture_big: Optional[str] = None
    nb_album: Optional[int] = None
    nb_fan: Optional[int] = None
    
class Album(BaseModel):
    id: int
    title: str
    cover: Optional[str] = None
    cover_medium: Optional[str] = None
    cover_big: Optional[str] = None
    release_date: Optional[str] = None
    
class Track(BaseModel):
    id: int
    title: str
    duration: Optional[int] = None
    preview: Optional[str] = None
    artist: Optional[dict] = None
    album: Optional[dict] = None
    
class BillboardSong(BaseModel):
    rank: int
    title: str
    artist: str
    
class BlindTestSong(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str
    artist: str
    youtube_id: Optional[str] = None
    
class HighScore(BaseModel):
    model_config = ConfigDict(extra="ignore")
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    player_name: str
    score: int
    total_questions: int
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

# ==================== DEEZER API ENDPOINTS ====================

@api_router.get("/search/artists")
async def search_artists(q: str = Query(..., min_length=1)):
    """Search artists on Deezer"""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{DEEZER_API}/search/artist",
                params={"q": q, "limit": 10}
            )
            data = response.json()
            
            if "error" in data:
                raise HTTPException(status_code=400, detail=data["error"]["message"])
            
            artists = []
            for item in data.get("data", []):
                artists.append({
                    "id": item.get("id"),
                    "name": item.get("name"),
                    "picture": item.get("picture"),
                    "picture_medium": item.get("picture_medium"),
                    "picture_big": item.get("picture_big"),
                    "nb_album": item.get("nb_album"),
                    "nb_fan": item.get("nb_fan")
                })
            
            return {"artists": artists}
    except httpx.RequestError as e:
        logger.error(f"Deezer API error: {e}")
        raise HTTPException(status_code=500, detail="Failed to search artists")

@api_router.get("/artist/{artist_id}")
async def get_artist(artist_id: int):
    """Get artist details from Deezer"""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{DEEZER_API}/artist/{artist_id}")
            data = response.json()
            
            if "error" in data:
                raise HTTPException(status_code=404, detail="Artist not found")
            
            return {
                "id": data.get("id"),
                "name": data.get("name"),
                "picture": data.get("picture"),
                "picture_medium": data.get("picture_medium"),
                "picture_big": data.get("picture_big"),
                "picture_xl": data.get("picture_xl"),
                "nb_album": data.get("nb_album"),
                "nb_fan": data.get("nb_fan"),
                "link": data.get("link")
            }
    except httpx.RequestError as e:
        logger.error(f"Deezer API error: {e}")
        raise HTTPException(status_code=500, detail="Failed to get artist")

@api_router.get("/artist/{artist_id}/albums")
async def get_artist_albums(artist_id: int, limit: int = 20):
    """Get artist's albums from Deezer"""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{DEEZER_API}/artist/{artist_id}/albums",
                params={"limit": limit}
            )
            data = response.json()
            
            if "error" in data:
                raise HTTPException(status_code=404, detail="Artist not found")
            
            albums = []
            for item in data.get("data", []):
                albums.append({
                    "id": item.get("id"),
                    "title": item.get("title"),
                    "cover": item.get("cover"),
                    "cover_medium": item.get("cover_medium"),
                    "cover_big": item.get("cover_big"),
                    "release_date": item.get("release_date")
                })
            
            return {"albums": albums}
    except httpx.RequestError as e:
        logger.error(f"Deezer API error: {e}")
        raise HTTPException(status_code=500, detail="Failed to get albums")

@api_router.get("/artist/{artist_id}/top")
async def get_artist_top_tracks(artist_id: int, limit: int = 10):
    """Get artist's top tracks from Deezer"""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{DEEZER_API}/artist/{artist_id}/top",
                params={"limit": limit}
            )
            data = response.json()
            
            if "error" in data:
                raise HTTPException(status_code=404, detail="Artist not found")
            
            tracks = []
            for item in data.get("data", []):
                tracks.append({
                    "id": item.get("id"),
                    "title": item.get("title"),
                    "duration": item.get("duration"),
                    "preview": item.get("preview"),
                    "album": {
                        "id": item.get("album", {}).get("id"),
                        "title": item.get("album", {}).get("title"),
                        "cover": item.get("album", {}).get("cover"),
                        "cover_medium": item.get("album", {}).get("cover_medium")
                    }
                })
            
            return {"tracks": tracks}
    except httpx.RequestError as e:
        logger.error(f"Deezer API error: {e}")
        raise HTTPException(status_code=500, detail="Failed to get top tracks")

@api_router.get("/artist/{artist_id}/related")
async def get_artist_related(artist_id: int, limit: int = 10):
    """Get related/collaborating artists from Deezer"""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{DEEZER_API}/artist/{artist_id}/related",
                params={"limit": limit}
            )
            data = response.json()
            
            if "error" in data:
                raise HTTPException(status_code=404, detail="Artist not found")
            
            related = []
            for item in data.get("data", []):
                # Create initials from name
                name_parts = item.get("name", "").split()
                initials = ""
                if len(name_parts) >= 2:
                    initials = name_parts[0][0].upper() + "." + name_parts[-1][0].upper()
                elif len(name_parts) == 1:
                    initials = name_parts[0][:2].upper()
                
                related.append({
                    "id": item.get("id"),
                    "name": item.get("name"),
                    "initials": initials,
                    "picture": item.get("picture"),
                    "picture_medium": item.get("picture_medium"),
                    "picture_big": item.get("picture_big"),
                    "nb_fan": item.get("nb_fan")
                })
            
            return {"related": related}
    except httpx.RequestError as e:
        logger.error(f"Deezer API error: {e}")
        raise HTTPException(status_code=500, detail="Failed to get related artists")

# ==================== DISCOGS API ENDPOINTS ====================

DISCOGS_API = "https://api.discogs.com"
DISCOGS_HEADERS = {
    "User-Agent": "MusicHub/1.0",
    "Authorization": f"Discogs token={DISCOGS_TOKEN}" if DISCOGS_TOKEN else ""
}


# Songwriting credits imported from songwriting_credits.py

def get_artist_songwriting_data(artist_name: str):
    """Get curated songwriting data for an artist"""
    import unicodedata
    
    def strip_accents(s):
        return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')
    
    # Normalize artist name - remove accents + lowercase
    normalized = strip_accents(artist_name.lower().strip())
    
    # Try exact match first
    for key, val in FAMOUS_SONGWRITING_CREDITS.items():
        if strip_accents(key) == normalized:
            return val
    
    # Try partial match
    for key, val in FAMOUS_SONGWRITING_CREDITS.items():
        clean_key = strip_accents(key).replace("-", " ").replace("'", "")
        clean_name = normalized.replace("-", " ").replace("'", "")
        if clean_key in clean_name or clean_name in clean_key:
            return val
    
    return None

@api_router.get("/artist-extras")
async def get_artist_extras(name: str = Query(..., min_length=1)):
    """Get curated anecdotes and songwriting credits for an artist"""
    songwriting_data = get_artist_songwriting_data(name)
    
    if songwriting_data:
        return {
            "found": True,
            "artist_name": name,
            "anecdotes": songwriting_data.get("anecdotes", []),
            "songs_written_for_others": songwriting_data.get("songs_written_for_others", [])
        }
    
    return {
        "found": False,
        "artist_name": name,
        "anecdotes": [],
        "songs_written_for_others": []
    }

# ==================== GENIUS API ENDPOINTS ====================

GENIUS_API = "https://api.genius.com"
GENIUS_HEADERS = {
    "Authorization": f"Bearer {GENIUS_TOKEN}" if GENIUS_TOKEN else ""
}

@api_router.get("/genius/search")
async def genius_search(q: str = Query(..., min_length=1)):
    """Search songs on Genius"""
    if not GENIUS_TOKEN:
        raise HTTPException(status_code=500, detail="Genius API token not configured")
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{GENIUS_API}/search",
                params={"q": q, "per_page": 10},
                headers=GENIUS_HEADERS,
                timeout=15.0
            )
            data = response.json()
            
            songs = []
            for hit in data.get("response", {}).get("hits", []):
                song = hit.get("result", {})
                songs.append({
                    "id": song.get("id"),
                    "title": song.get("title"),
                    "full_title": song.get("full_title"),
                    "artist": song.get("primary_artist", {}).get("name"),
                    "artist_id": song.get("primary_artist", {}).get("id"),
                    "url": song.get("url"),
                    "thumbnail": song.get("song_art_image_thumbnail_url"),
                    "page_views": song.get("stats", {}).get("pageviews")
                })
            
            return {"songs": songs}
    except httpx.RequestError as e:
        logger.error(f"Genius API error: {e}")
        raise HTTPException(status_code=500, detail="Failed to search Genius")

@api_router.get("/genius/song/{song_id}")
async def genius_song_details(song_id: int):
    """Get full song details from Genius including credits"""
    if not GENIUS_TOKEN:
        raise HTTPException(status_code=500, detail="Genius API token not configured")
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{GENIUS_API}/songs/{song_id}",
                headers=GENIUS_HEADERS,
                timeout=15.0
            )
            data = response.json()
            song = data.get("response", {}).get("song", {})
            
            if not song:
                raise HTTPException(status_code=404, detail="Song not found")
            
            # Extract writer artists
            writers = []
            for wa in song.get("writer_artists", []):
                writers.append({
                    "id": wa.get("id"),
                    "name": wa.get("name"),
                    "image": wa.get("image_url")
                })
            
            # Extract producer artists
            producers = []
            for cp in song.get("custom_performances", []):
                if "producer" in cp.get("label", "").lower():
                    for artist in cp.get("artists", []):
                        producers.append({
                            "id": artist.get("id"),
                            "name": artist.get("name"),
                            "image": artist.get("image_url")
                        })
            
            # Also check producer_artists field
            for pa in song.get("producer_artists", []):
                if not any(p["id"] == pa.get("id") for p in producers):
                    producers.append({
                        "id": pa.get("id"),
                        "name": pa.get("name"),
                        "image": pa.get("image_url")
                    })
            
            return {
                "id": song.get("id"),
                "title": song.get("title"),
                "full_title": song.get("full_title"),
                "artist": song.get("primary_artist", {}).get("name"),
                "artist_id": song.get("primary_artist", {}).get("id"),
                "album": song.get("album", {}).get("name") if song.get("album") else None,
                "release_date": song.get("release_date_for_display"),
                "url": song.get("url"),
                "thumbnail": song.get("song_art_image_thumbnail_url"),
                "image": song.get("song_art_image_url"),
                "writers": writers,
                "producers": producers,
                "description": song.get("description", {}).get("plain") if isinstance(song.get("description"), dict) else None
            }
    except httpx.RequestError as e:
        logger.error(f"Genius API error: {e}")
        raise HTTPException(status_code=500, detail="Failed to get song details")

@api_router.get("/genius/artist/{artist_id}/songs")
async def genius_artist_songs(artist_id: int, per_page: int = 20, sort: str = "popularity"):
    """Get artist's songs from Genius with credits"""
    if not GENIUS_TOKEN:
        raise HTTPException(status_code=500, detail="Genius API token not configured")
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{GENIUS_API}/artists/{artist_id}/songs",
                params={"per_page": per_page, "sort": sort},
                headers=GENIUS_HEADERS,
                timeout=15.0
            )
            data = response.json()
            
            songs = []
            for song in data.get("response", {}).get("songs", []):
                songs.append({
                    "id": song.get("id"),
                    "title": song.get("title"),
                    "full_title": song.get("full_title"),
                    "url": song.get("url"),
                    "thumbnail": song.get("song_art_image_thumbnail_url"),
                    "page_views": song.get("stats", {}).get("pageviews")
                })
            
            return {"songs": songs, "artist_id": artist_id}
    except httpx.RequestError as e:
        logger.error(f"Genius API error: {e}")
        raise HTTPException(status_code=500, detail="Failed to get artist songs")

@api_router.get("/genius/credits")
async def genius_get_credits(artist_name: str = Query(..., min_length=1)):
    """Get songwriter/producer credits for an artist from Genius - 
    finds songs where this artist is credited as writer/producer"""
    if not GENIUS_TOKEN:
        raise HTTPException(status_code=500, detail="Genius API token not configured")
    try:
        async with httpx.AsyncClient() as client:
            # Search for the artist's most popular songs
            search_response = await client.get(
                f"{GENIUS_API}/search",
                params={"q": artist_name, "per_page": 15},
                headers=GENIUS_HEADERS,
                timeout=15.0
            )
            search_data = search_response.json()
            hits = search_data.get("response", {}).get("hits", [])
            
            if not hits:
                return {"artist_name": artist_name, "credits": [], "written_for": []}
            
            # Get detailed info for top songs to find credits
            credits_info = []
            written_for_others = []
            
            for hit in hits[:8]:
                song = hit.get("result", {})
                song_id = song.get("id")
                primary_artist = song.get("primary_artist", {}).get("name", "")
                
                if not song_id:
                    continue
                
                # Get full song details with credits
                try:
                    detail_response = await client.get(
                        f"{GENIUS_API}/songs/{song_id}",
                        headers=GENIUS_HEADERS,
                        timeout=10.0
                    )
                    detail_data = detail_response.json()
                    song_detail = detail_data.get("response", {}).get("song", {})
                    
                    if not song_detail:
                        continue
                    
                    # Get writers
                    writers = [w.get("name") for w in song_detail.get("writer_artists", [])]
                    producers = [p.get("name") for p in song_detail.get("producer_artists", [])]
                    
                    song_info = {
                        "id": song_id,
                        "title": song_detail.get("title"),
                        "full_title": song_detail.get("full_title"),
                        "primary_artist": primary_artist,
                        "album": song_detail.get("album", {}).get("name") if song_detail.get("album") else None,
                        "release_date": song_detail.get("release_date_for_display"),
                        "thumbnail": song_detail.get("song_art_image_thumbnail_url"),
                        "url": song_detail.get("url"),
                        "writers": writers,
                        "producers": producers
                    }
                    
                    credits_info.append(song_info)
                    
                    # Check if artist wrote for someone else
                    artist_lower = artist_name.lower()
                    if any(artist_lower in w.lower() for w in writers):
                        if artist_lower not in primary_artist.lower():
                            written_for_others.append(song_info)
                    
                except Exception as e:
                    logger.warning(f"Error getting song {song_id}: {e}")
                    continue
            
            return {
                "artist_name": artist_name,
                "credits": credits_info,
                "written_for": written_for_others
            }
    except httpx.RequestError as e:
        logger.error(f"Genius API error: {e}")
        raise HTTPException(status_code=500, detail="Failed to get credits from Genius")

@api_router.get("/discogs/search/artist")
async def search_discogs_artist(q: str = Query(..., min_length=1)):
    """Search artist on Discogs"""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{DISCOGS_API}/database/search",
                params={"q": q, "type": "artist", "per_page": 10},
                headers=DISCOGS_HEADERS,
                timeout=15.0
            )
            data = response.json()
            
            artists = []
            for item in data.get("results", []):
                artists.append({
                    "id": item.get("id"),
                    "name": item.get("title"),
                    "thumb": item.get("thumb"),
                    "cover_image": item.get("cover_image"),
                    "resource_url": item.get("resource_url")
                })
            
            return {"artists": artists}
    except httpx.RequestError as e:
        logger.error(f"Discogs API error: {e}")
        raise HTTPException(status_code=500, detail="Failed to search Discogs")

@api_router.get("/discogs/artist/{artist_id}")
async def get_discogs_artist(artist_id: int):
    """Get detailed artist info from Discogs including members and groups"""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{DISCOGS_API}/artists/{artist_id}",
                headers=DISCOGS_HEADERS,
                timeout=15.0
            )
            data = response.json()
            
            if "message" in data:
                raise HTTPException(status_code=404, detail="Artist not found on Discogs")
            
            # Extract members (for bands) or groups (for solo artists)
            members = []
            for member in data.get("members", []):
                members.append({
                    "id": member.get("id"),
                    "name": member.get("name"),
                    "active": member.get("active", True),
                    "thumbnail_url": member.get("thumbnail_url")
                })
            
            groups = []
            for group in data.get("groups", []):
                groups.append({
                    "id": group.get("id"),
                    "name": group.get("name"),
                    "active": group.get("active", True),
                    "thumbnail_url": group.get("thumbnail_url")
                })
            
            # Extract aliases
            aliases = []
            for alias in data.get("aliases", []):
                aliases.append({
                    "id": alias.get("id"),
                    "name": alias.get("name")
                })
            
            return {
                "id": data.get("id"),
                "name": data.get("name"),
                "profile": data.get("profile", ""),
                "images": data.get("images", []),
                "members": members,
                "groups": groups,
                "aliases": aliases,
                "urls": data.get("urls", []),
                "namevariations": data.get("namevariations", [])
            }
    except httpx.RequestError as e:
        logger.error(f"Discogs API error: {e}")
        raise HTTPException(status_code=500, detail="Failed to get Discogs artist")

@api_router.get("/discogs/artist/{artist_id}/releases")
async def get_discogs_artist_releases(artist_id: int, page: int = 1, per_page: int = 20):
    """Get artist releases with credit information from Discogs"""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{DISCOGS_API}/artists/{artist_id}/releases",
                params={"page": page, "per_page": per_page, "sort": "year", "sort_order": "desc"},
                headers=DISCOGS_HEADERS,
                timeout=15.0
            )
            data = response.json()
            
            releases = []
            for item in data.get("releases", []):
                # Get role information (collaboration type)
                role = item.get("role", "Main")
                
                releases.append({
                    "id": item.get("id"),
                    "title": item.get("title"),
                    "year": item.get("year"),
                    "type": item.get("type"),
                    "role": role,
                    "artist": item.get("artist"),
                    "thumb": item.get("thumb"),
                    "resource_url": item.get("resource_url"),
                    "format": item.get("format")
                })
            
            return {
                "releases": releases,
                "pagination": data.get("pagination", {})
            }
    except httpx.RequestError as e:
        logger.error(f"Discogs API error: {e}")
        raise HTTPException(status_code=500, detail="Failed to get Discogs releases")

@api_router.get("/discogs/release/{release_id}/credits")
async def get_discogs_release_credits(release_id: int):
    """Get detailed credits for a specific release from Discogs"""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{DISCOGS_API}/releases/{release_id}",
                headers=DISCOGS_HEADERS,
                timeout=15.0
            )
            data = response.json()
            
            if "message" in data:
                raise HTTPException(status_code=404, detail="Release not found")
            
            # Extract artists (main)
            artists = []
            for artist in data.get("artists", []):
                artists.append({
                    "id": artist.get("id"),
                    "name": artist.get("name"),
                    "role": "Main Artist"
                })
            
            # Extract extra artists (collaborators, producers, writers, etc.)
            extra_artists = []
            for extra in data.get("extraartists", []):
                extra_artists.append({
                    "id": extra.get("id"),
                    "name": extra.get("name"),
                    "role": extra.get("role", "Unknown"),
                    "tracks": extra.get("tracks", "")
                })
            
            # Group credits by role
            credits_by_role = {}
            for ea in extra_artists:
                role = ea["role"]
                if role not in credits_by_role:
                    credits_by_role[role] = []
                credits_by_role[role].append(ea)
            
            # Extract tracklist with credits
            tracklist = []
            for track in data.get("tracklist", []):
                track_artists = []
                for ta in track.get("artists", []):
                    track_artists.append({
                        "id": ta.get("id"),
                        "name": ta.get("name")
                    })
                for tea in track.get("extraartists", []):
                    track_artists.append({
                        "id": tea.get("id"),
                        "name": tea.get("name"),
                        "role": tea.get("role")
                    })
                
                tracklist.append({
                    "position": track.get("position"),
                    "title": track.get("title"),
                    "duration": track.get("duration"),
                    "artists": track_artists
                })
            
            return {
                "id": data.get("id"),
                "title": data.get("title"),
                "year": data.get("year"),
                "genres": data.get("genres", []),
                "styles": data.get("styles", []),
                "artists": artists,
                "extra_artists": extra_artists,
                "credits_by_role": credits_by_role,
                "tracklist": tracklist,
                "images": data.get("images", []),
                "labels": data.get("labels", [])
            }
    except httpx.RequestError as e:
        logger.error(f"Discogs API error: {e}")
        raise HTTPException(status_code=500, detail="Failed to get release credits")

@api_router.get("/credits/artist")
async def get_artist_full_credits(name: str = Query(..., min_length=1)):
    """Get comprehensive artist credits combining Deezer and Discogs data"""
    try:
        result = {
            "artist_name": name,
            "deezer": None,
            "discogs": None,
            "collaborations": [],
            "writing_credits": [],
            "production_credits": []
        }
        
        async with httpx.AsyncClient() as client:
            # Search on Deezer first
            deezer_response = await client.get(
                f"{DEEZER_API}/search/artist",
                params={"q": name, "limit": 1}
            )
            deezer_data = deezer_response.json()
            
            if deezer_data.get("data"):
                deezer_artist = deezer_data["data"][0]
                result["deezer"] = {
                    "id": deezer_artist.get("id"),
                    "name": deezer_artist.get("name"),
                    "picture": deezer_artist.get("picture_medium"),
                    "nb_fan": deezer_artist.get("nb_fan")
                }
            
            # Search on Discogs
            discogs_response = await client.get(
                f"{DISCOGS_API}/database/search",
                params={"q": name, "type": "artist", "per_page": 1},
                headers=DISCOGS_HEADERS,
                timeout=15.0
            )
            discogs_search = discogs_response.json()
            
            if discogs_search.get("results"):
                discogs_artist_id = discogs_search["results"][0]["id"]
                
                # Get full artist info
                artist_response = await client.get(
                    f"{DISCOGS_API}/artists/{discogs_artist_id}",
                    headers=DISCOGS_HEADERS,
                    timeout=15.0
                )
                discogs_artist = artist_response.json()
                
                result["discogs"] = {
                    "id": discogs_artist.get("id"),
                    "name": discogs_artist.get("name"),
                    "profile": discogs_artist.get("profile", "")[:500],
                    "images": discogs_artist.get("images", [])[:3]
                }
                
                # Get members/groups for collaborations
                for member in discogs_artist.get("members", []):
                    result["collaborations"].append({
                        "type": "member",
                        "id": member.get("id"),
                        "name": member.get("name"),
                        "active": member.get("active", True),
                        "thumbnail": member.get("thumbnail_url")
                    })
                
                for group in discogs_artist.get("groups", []):
                    result["collaborations"].append({
                        "type": "group",
                        "id": group.get("id"),
                        "name": group.get("name"),
                        "active": group.get("active", True),
                        "thumbnail": group.get("thumbnail_url")
                    })
                
                # Get releases to find writing/production credits
                releases_response = await client.get(
                    f"{DISCOGS_API}/artists/{discogs_artist_id}/releases",
                    params={"per_page": 50, "sort": "year", "sort_order": "desc"},
                    headers=DISCOGS_HEADERS,
                    timeout=15.0
                )
                releases_data = releases_response.json()
                
                # Identify writing credits (where role contains "Written" or "Songwriter")
                writing_roles = ["Written-By", "Songwriter", "Lyrics By", "Music By", "Composed By"]
                production_roles = ["Producer", "Produced By", "Executive Producer", "Co-Producer"]
                
                for release in releases_data.get("releases", [])[:30]:
                    role = release.get("role", "Main")
                    
                    # Check if this is a writing credit
                    for wr in writing_roles:
                        if wr.lower() in role.lower():
                            result["writing_credits"].append({
                                "release_id": release.get("id"),
                                "title": release.get("title"),
                                "artist": release.get("artist"),
                                "year": release.get("year"),
                                "role": role,
                                "thumb": release.get("thumb")
                            })
                            break
                    
                    # Check if this is a production credit
                    for pr in production_roles:
                        if pr.lower() in role.lower():
                            result["production_credits"].append({
                                "release_id": release.get("id"),
                                "title": release.get("title"),
                                "artist": release.get("artist"),
                                "year": release.get("year"),
                                "role": role,
                                "thumb": release.get("thumb")
                            })
                            break
        
        return result
        
    except httpx.RequestError as e:
        logger.error(f"Credits API error: {e}")
        raise HTTPException(status_code=500, detail="Failed to get artist credits")

# ==================== DEEZER TRACK SEARCH (for previews) ====================

@api_router.get("/deezer/track/search")
async def search_deezer_track(q: str = Query(..., min_length=1)):
    """Search a track on Deezer and return preview URL"""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{DEEZER_API}/search/track",
                params={"q": q, "limit": 1},
                timeout=10.0
            )
            data = response.json()
            
            tracks = data.get("data", [])
            if tracks:
                track = tracks[0]
                return {
                    "found": True,
                    "title": track.get("title"),
                    "artist": track.get("artist", {}).get("name"),
                    "preview": track.get("preview"),
                    "album_cover": track.get("album", {}).get("cover_medium")
                }
            return {"found": False}
    except httpx.RequestError:
        return {"found": False}

@api_router.get("/deezer/tracks/batch")
async def batch_search_deezer_tracks(songs: str = Query(...)):
    """Batch search tracks on Deezer - songs format: 'title1|artist1,,title2|artist2'"""
    import asyncio
    
    song_list = [s.strip() for s in songs.split(",,") if s.strip()]
    
    async def search_one(query):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    f"{DEEZER_API}/search/track",
                    params={"q": query, "limit": 1},
                    timeout=8.0
                )
                data = response.json()
                tracks = data.get("data", [])
                if tracks:
                    t = tracks[0]
                    return {
                        "query": query,
                        "found": True,
                        "preview": t.get("preview"),
                        "album_cover": t.get("album", {}).get("cover_small"),
                        "deezer_title": t.get("title"),
                        "deezer_artist": t.get("artist", {}).get("name")
                    }
        except Exception:
            pass
        return {"query": query, "found": False}
    
    # Process in batches of 5 to avoid rate limiting
    results = []
    for i in range(0, len(song_list), 5):
        batch = song_list[i:i+5]
        batch_results = await asyncio.gather(*[search_one(q) for q in batch])
        results.extend(batch_results)
    
    return {"results": results}

# ==================== ARTIST CONNECTION GRAPH ====================

@api_router.get("/artist/{artist_id}/graph")
async def get_artist_graph(artist_id: int, depth: int = 1):
    """Build a connection graph for an artist using Deezer related artists"""
    try:
        nodes = {}
        links = []
        
        async with httpx.AsyncClient() as client:
            # Get main artist
            main_response = await client.get(f"{DEEZER_API}/artist/{artist_id}")
            main_data = main_response.json()
            
            if "error" in main_data:
                raise HTTPException(status_code=404, detail="Artist not found")
            
            main_node = {
                "id": str(main_data["id"]),
                "name": main_data.get("name"),
                "picture": main_data.get("picture_medium"),
                "nb_fan": main_data.get("nb_fan", 0),
                "is_main": True
            }
            nodes[main_node["id"]] = main_node
            
            # Get related artists (level 1)
            related_response = await client.get(
                f"{DEEZER_API}/artist/{artist_id}/related",
                params={"limit": 8}
            )
            related_data = related_response.json()
            
            for rel in related_data.get("data", []):
                rel_id = str(rel["id"])
                if rel_id not in nodes:
                    nodes[rel_id] = {
                        "id": rel_id,
                        "name": rel.get("name"),
                        "picture": rel.get("picture_medium"),
                        "nb_fan": rel.get("nb_fan", 0),
                        "is_main": False
                    }
                links.append({
                    "source": main_node["id"],
                    "target": rel_id
                })
            
            # Get level 2 connections (related of related) for richer graph
            if depth >= 2:
                level1_ids = [l["target"] for l in links[:4]]  # limit to first 4
                for l1_id in level1_ids:
                    try:
                        l2_response = await client.get(
                            f"{DEEZER_API}/artist/{l1_id}/related",
                            params={"limit": 4}
                        )
                        l2_data = l2_response.json()
                        
                        for rel2 in l2_data.get("data", []):
                            rel2_id = str(rel2["id"])
                            if rel2_id not in nodes:
                                nodes[rel2_id] = {
                                    "id": rel2_id,
                                    "name": rel2.get("name"),
                                    "picture": rel2.get("picture_medium"),
                                    "nb_fan": rel2.get("nb_fan", 0),
                                    "is_main": False
                                }
                            link = {"source": l1_id, "target": rel2_id}
                            if link not in links and {"source": rel2_id, "target": l1_id} not in links:
                                links.append(link)
                    except Exception:
                        continue
        
        return {
            "nodes": list(nodes.values()),
            "links": links
        }
    except httpx.RequestError as e:
        logger.error(f"Graph API error: {e}")
        raise HTTPException(status_code=500, detail="Failed to build artist graph")

# ==================== BILLBOARD SCRAPING ====================

@api_router.get("/billboard/hot100")
async def get_billboard_hot100():
    """Scrape current Billboard Hot 100"""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                "https://www.billboard.com/charts/hot-100/",
                headers=HEADERS,
                timeout=30.0
            )
            
            if response.status_code != 200:
                raise HTTPException(status_code=500, detail="Failed to fetch Billboard chart")
            
            soup = BeautifulSoup(response.text, 'html.parser')
            songs = []
            
            # Find all chart rows
            chart_rows = soup.select('div.o-chart-results-list-row-container')
            
            for i, row in enumerate(chart_rows[:100], 1):
                try:
                    # Get song title
                    title_elem = row.select_one('h3#title-of-a-story')
                    title = title_elem.get_text(strip=True) if title_elem else "Unknown"
                    
                    # Get artist - it's the span right after the h3 title
                    artist_elem = row.select_one('h3#title-of-a-story + span')
                    if not artist_elem:
                        artist_elem = row.select_one('span.c-label.a-no-trucate')
                    artist = artist_elem.get_text(strip=True) if artist_elem else "Unknown"
                    
                    songs.append({
                        "rank": i,
                        "title": title,
                        "artist": artist
                    })
                except Exception as e:
                    logger.warning(f"Error parsing row {i}: {e}")
                    continue
            
            # Fallback if main selector doesn't work
            if not songs:
                # Try alternative selectors
                list_items = soup.select('ul.o-chart-results-list li')
                rank = 1
                for item in list_items:
                    title_elem = item.select_one('h3')
                    artist_spans = item.select('span')
                    
                    if title_elem:
                        title = title_elem.get_text(strip=True)
                        artist = "Unknown"
                        for span in artist_spans:
                            text = span.get_text(strip=True)
                            if text and text != title and len(text) > 2:
                                artist = text
                                break
                        
                        songs.append({
                            "rank": rank,
                            "title": title,
                            "artist": artist
                        })
                        rank += 1
                        if rank > 100:
                            break
            
            return {"songs": songs, "date": datetime.now().strftime("%Y-%m-%d")}
            
    except httpx.RequestError as e:
        logger.error(f"Billboard scraping error: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch Billboard chart")

@api_router.get("/billboard/year/{year}")
async def get_billboard_year_end(year: int):
    """Scrape Billboard Year-End Hot 100"""
    if year < 2006 or year > datetime.now().year:
        raise HTTPException(status_code=400, detail="Year must be between 2006 and current year")
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"https://www.billboard.com/charts/year-end/{year}/hot-100-songs/",
                headers=HEADERS,
                timeout=30.0
            )
            
            if response.status_code != 200:
                raise HTTPException(status_code=500, detail="Failed to fetch Billboard year-end chart")
            
            soup = BeautifulSoup(response.text, 'html.parser')
            songs = []
            
            # Year-end charts structure
            chart_rows = soup.select('div.o-chart-results-list-row-container')
            
            for i, row in enumerate(chart_rows[:100], 1):
                try:
                    title_elem = row.select_one('h3#title-of-a-story')
                    title = title_elem.get_text(strip=True) if title_elem else "Unknown"
                    
                    artist_elem = row.select_one('h3#title-of-a-story + span')
                    if not artist_elem:
                        artist_elem = row.select_one('span.c-label.a-no-trucate')
                    artist = artist_elem.get_text(strip=True) if artist_elem else "Unknown"
                    
                    songs.append({
                        "rank": i,
                        "title": title,
                        "artist": artist
                    })
                except Exception as e:
                    logger.warning(f"Error parsing row {i}: {e}")
                    continue
            
            return {"songs": songs, "year": year}
            
    except httpx.RequestError as e:
        logger.error(f"Billboard scraping error: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch Billboard year-end chart")

# ==================== BLIND TEST ====================

# Pre-defined popular songs with YouTube IDs for blind test
BLIND_TEST_SONGS = [
    {"title": "Blinding Lights", "artist": "The Weeknd", "youtube_id": "4NRXx6U8ABQ"},
    {"title": "Shape of You", "artist": "Ed Sheeran", "youtube_id": "JGwWNGJdvx8"},
    {"title": "Dance Monkey", "artist": "Tones and I", "youtube_id": "q0hyYWKXF0Q"},
    {"title": "Someone Like You", "artist": "Adele", "youtube_id": "hLQl3WQQoQ0"},
    {"title": "Uptown Funk", "artist": "Bruno Mars", "youtube_id": "OPf0YbXqDm0"},
    {"title": "Despacito", "artist": "Luis Fonsi", "youtube_id": "kJQP7kiw5Fk"},
    {"title": "See You Again", "artist": "Wiz Khalifa ft. Charlie Puth", "youtube_id": "RgKAFK5djSk"},
    {"title": "Gangnam Style", "artist": "PSY", "youtube_id": "9bZkp7q19f0"},
    {"title": "Hello", "artist": "Adele", "youtube_id": "YQHsXMglC9A"},
    {"title": "Thinking Out Loud", "artist": "Ed Sheeran", "youtube_id": "lp-EO5I60KA"},
    {"title": "Counting Stars", "artist": "OneRepublic", "youtube_id": "hT_nvWreIhg"},
    {"title": "Roar", "artist": "Katy Perry", "youtube_id": "CevxZvSJLk8"},
    {"title": "Happy", "artist": "Pharrell Williams", "youtube_id": "ZbZSe6N_BXs"},
    {"title": "Radioactive", "artist": "Imagine Dragons", "youtube_id": "ktvTqknDobU"},
    {"title": "Stay", "artist": "The Kid LAROI & Justin Bieber", "youtube_id": "kTJczUoc26U"},
    {"title": "Levitating", "artist": "Dua Lipa", "youtube_id": "TUVcZfQe-Kw"},
    {"title": "drivers license", "artist": "Olivia Rodrigo", "youtube_id": "ZmDBbnmKpqQ"},
    {"title": "Bad Guy", "artist": "Billie Eilish", "youtube_id": "DyDfgMOUjCI"},
    {"title": "Old Town Road", "artist": "Lil Nas X", "youtube_id": "w2Ov5jzm3j8"},
    {"title": "Señorita", "artist": "Shawn Mendes & Camila Cabello", "youtube_id": "Pkh8UtuejGw"},
    {"title": "Get Lucky", "artist": "Daft Punk", "youtube_id": "5NV6Rdv1a3I"},
    {"title": "Stressed Out", "artist": "Twenty One Pilots", "youtube_id": "pXRviuL6vMY"},
    {"title": "Thunder", "artist": "Imagine Dragons", "youtube_id": "fKopy74weus"},
    {"title": "Shallow", "artist": "Lady Gaga & Bradley Cooper", "youtube_id": "bo_efYhYU2A"},
    {"title": "Closer", "artist": "The Chainsmokers ft. Halsey", "youtube_id": "PT2_F-1esPk"},
    {"title": "Love Yourself", "artist": "Justin Bieber", "youtube_id": "oyEuk8j8imI"},
    {"title": "Can't Stop the Feeling", "artist": "Justin Timberlake", "youtube_id": "ru0K8uYEZWw"},
    {"title": "Havana", "artist": "Camila Cabello", "youtube_id": "BQ0mxQXmLsk"},
    {"title": "Perfect", "artist": "Ed Sheeran", "youtube_id": "2Vv-BfVoq4g"},
    {"title": "Believer", "artist": "Imagine Dragons", "youtube_id": "7wtfhZwyrcc"},
]

@api_router.get("/blindtest/songs")
async def get_blindtest_songs(count: int = 10):
    """Get random songs for blind test"""
    if count > len(BLIND_TEST_SONGS):
        count = len(BLIND_TEST_SONGS)
    
    selected_songs = random.sample(BLIND_TEST_SONGS, count)
    
    # Generate fake choices for each song
    result = []
    for song in selected_songs:
        # Get 3 random wrong answers
        other_songs = [s for s in BLIND_TEST_SONGS if s["title"] != song["title"]]
        wrong_answers = random.sample(other_songs, min(3, len(other_songs)))
        
        choices = [
            {"title": song["title"], "artist": song["artist"], "correct": True}
        ]
        for wrong in wrong_answers:
            choices.append({
                "title": wrong["title"],
                "artist": wrong["artist"],
                "correct": False
            })
        
        random.shuffle(choices)
        
        result.append({
            "id": str(uuid.uuid4()),
            "youtube_id": song["youtube_id"],
            "choices": choices,
            "correct_answer": {"title": song["title"], "artist": song["artist"]}
        })
    
    return {"songs": result}

@api_router.post("/blindtest/score")
async def save_blindtest_score(player_name: str, score: int, total_questions: int):
    """Save blind test high score"""
    score_obj = HighScore(
        player_name=player_name,
        score=score,
        total_questions=total_questions
    )
    
    doc = score_obj.model_dump()
    doc['timestamp'] = doc['timestamp'].isoformat()
    
    await db.high_scores.insert_one(doc)
    
    return {"message": "Score saved", "score": score_obj.model_dump()}

@api_router.get("/blindtest/highscores")
async def get_highscores(limit: int = 10):
    """Get top high scores"""
    scores = await db.high_scores.find(
        {},
        {"_id": 0}
    ).sort("score", -1).limit(limit).to_list(limit)
    
    return {"scores": scores}

# ==================== HEALTH CHECK ====================

@api_router.get("/")
async def root():
    return {"message": "Music Hub API", "status": "running"}

@api_router.get("/health")
async def health_check():
    return {"status": "healthy"}

# Include the router in the main app
app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=os.environ.get('CORS_ORIGINS', '*').split(','),
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("shutdown")
async def shutdown_db_client():
    client.close()
