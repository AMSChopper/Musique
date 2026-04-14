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

ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

# MongoDB connection
mongo_url = os.environ['MONGO_URL']
client = AsyncIOMotorClient(mongo_url)
db = client[os.environ['DB_NAME']]

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
