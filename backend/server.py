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

# Discogs API token
DISCOGS_TOKEN = os.environ.get('DISCOGS_TOKEN', '')

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

# ==================== FAMOUS SONGWRITING CREDITS DATABASE ====================
# Curated database of famous songs written for other artists

FAMOUS_SONGWRITING_CREDITS = {
    "ed sheeran": {
        "anecdotes": [
            "Ed Sheeran a écrit plus de 100 chansons pour d'autres artistes avant de devenir célèbre.",
            "Il a commencé à écrire des chansons à 11 ans et a sorti son premier album indépendant à 14 ans.",
            "Ed écrit souvent ses chansons en moins de 30 minutes - 'Shape of You' a été écrite en seulement 20 minutes.",
            "Il a un tatouage de ketchup Heinz sur son bras car c'est sa sauce préférée."
        ],
        "songs_written_for_others": [
            {"title": "Love Yourself", "artist": "Justin Bieber", "year": 2015, "info": "Ed a écrit cette chanson mais Justin a changé 'fuck yourself' en 'love yourself'", "youtube_id": "oyEuk8j8imI"},
            {"title": "Cold Water", "artist": "Major Lazer ft. Justin Bieber", "year": 2016, "info": "Co-écrite avec Benny Blanco et produite par Major Lazer", "youtube_id": "a59gmGkq_pw"},
            {"title": "Tattoo", "artist": "Hilary Duff", "year": 2014, "info": "Une ballade pop écrite pour son album 'Breathe In. Breathe Out.'"},
            {"title": "Little Things", "artist": "One Direction", "year": 2012, "info": "Ed a écrit cette chanson en pensant à son ex-petite amie", "youtube_id": "EDwb9jOVRtU"},
            {"title": "Moments", "artist": "One Direction", "year": 2011, "info": "Sa première chanson écrite pour le groupe"},
            {"title": "Over Again", "artist": "One Direction", "year": 2012, "info": "Co-écrite avec les membres du groupe"},
            {"title": "18", "artist": "One Direction", "year": 2014, "info": "Une chanson nostalgique sur la jeunesse"},
            {"title": "Lay It All on Me", "artist": "Rudimental", "year": 2015, "info": "Ed apparaît aussi comme featuring sur cette chanson", "youtube_id": "7Sr9dZJUwXw"},
            {"title": "The Rest of Our Life", "artist": "Tim McGraw & Faith Hill", "year": 2017, "info": "Écrite pour le duo country légendaire"}
        ]
    },
    "sia": {
        "anecdotes": [
            "Sia souffre d'une maladie neurologique appelée syndrome d'Ehlers-Danlos qui cause des douleurs chroniques.",
            "Elle porte des perruques pour cacher son visage car elle ne voulait pas être célèbre, juste écrire des chansons.",
            "Sia a écrit 'Titanium' en seulement 40 minutes et ne voulait pas la chanter elle-même.",
            "Elle a été sobre depuis 2010 après des années de lutte contre l'addiction."
        ],
        "songs_written_for_others": [
            {"title": "Titanium", "artist": "David Guetta ft. Sia", "year": 2011, "info": "Écrite pour Alicia Keys à l'origine, mais Sia a gardé les vocaux de démo", "youtube_id": "JRfuAukYTKg"},
            {"title": "Diamonds", "artist": "Rihanna", "year": 2012, "info": "Écrite en 14 minutes, devenue #1 mondial", "youtube_id": "lWA2pjMjpBs"},
            {"title": "Wild Ones", "artist": "Flo Rida ft. Sia", "year": 2012, "info": "Un hit dance-pop co-écrit et chanté par Sia", "youtube_id": "bpOR_HuHRNs"},
            {"title": "Pretty Hurts", "artist": "Beyoncé", "year": 2013, "info": "Sur l'album éponyme surprise de Beyoncé", "youtube_id": "LXXQLa-5n5w"},
            {"title": "Perfume", "artist": "Britney Spears", "year": 2013, "info": "Une ballade émotionnelle pour l'album 'Britney Jean'", "youtube_id": "p1JPKLa-Ofc"},
            {"title": "Radioactive", "artist": "Rita Ora", "year": 2012, "info": "Single principal de l'album 'Ora'"},
            {"title": "Waving Goodbye", "artist": "Sia", "year": 2010, "info": "Écrite pour Shakira mais gardée pour elle-même"},
            {"title": "Flames", "artist": "David Guetta & Sia", "year": 2018, "info": "Nouvelle collaboration avec Guetta", "youtube_id": "pSPdGdTLQkU"},
            {"title": "Unstoppable", "artist": "Sia", "year": 2016, "info": "Initialement écrite pour Demi Lovato mais Sia l'a gardée"}
        ]
    },
    "pharrell williams": {
        "anecdotes": [
            "Pharrell a produit plus de 100 hits #1 en carrière avec The Neptunes.",
            "Son chapeau Vivienne Westwood porté aux Grammys 2014 est devenu viral et a été vendu aux enchères pour 44 000$.",
            "Il a une condition appelée synesthésie - il peut 'voir' la musique en couleurs.",
            "Pharrell avait 40 ans quand 'Happy' est sorti, prouvant qu'on peut percer à tout âge."
        ],
        "songs_written_for_others": [
            {"title": "Hollaback Girl", "artist": "Gwen Stefani", "year": 2005, "info": "Premier single à atteindre 1 million de téléchargements", "youtube_id": "Kgjkth6BRRY"},
            {"title": "Drop It Like It's Hot", "artist": "Snoop Dogg", "year": 2004, "info": "Pharrell a co-écrit et produit ce classique", "youtube_id": "GtUVQei3nX4"},
            {"title": "Blurred Lines", "artist": "Robin Thicke ft. T.I.", "year": 2013, "info": "Chanson de l'été 2013, controversée pour plagiat", "youtube_id": "yyDUC1LUXSU"},
            {"title": "Get Lucky", "artist": "Daft Punk", "year": 2013, "info": "Co-écrite et co-chantée avec le duo français", "youtube_id": "5NV6Rdv1a3I"},
            {"title": "Beautiful", "artist": "Snoop Dogg", "year": 2003, "info": "Produit par The Neptunes"},
            {"title": "Frontin'", "artist": "Pharrell ft. Jay-Z", "year": 2003, "info": "Son premier single solo à succès"},
            {"title": "Milkshake", "artist": "Kelis", "year": 2003, "info": "Produit avec Chad Hugo, devenu un hymne", "youtube_id": "pGL2rytTraA"},
            {"title": "Grindin'", "artist": "Clipse", "year": 2002, "info": "Beat minimaliste révolutionnaire", "youtube_id": "TjWAWcx4xdE"},
            {"title": "Sweetest Girl", "artist": "Wyclef Jean", "year": 2007, "info": "Featuring Akon, Lil Wayne et Niia"}
        ]
    },
    "bruno mars": {
        "anecdotes": [
            "Bruno Mars a été arrêté en 2010 pour possession de cocaïne à Las Vegas - il a plaidé coupable et fait des travaux d'intérêt général.",
            "Son vrai nom est Peter Gene Hernandez - 'Bruno' vient d'un catcheur et 'Mars' car les filles disaient qu'il n'était pas de cette planète.",
            "Il a commencé comme impersonator d'Elvis Presley à 4 ans à Hawaï.",
            "Bruno joue de plus de 10 instruments différents."
        ],
        "songs_written_for_others": [
            {"title": "Right Round", "artist": "Flo Rida", "year": 2009, "info": "Premier #1 de Bruno en tant qu'auteur", "youtube_id": "CcCw1ggftuQ"},
            {"title": "Nothin' on You", "artist": "B.o.B ft. Bruno Mars", "year": 2010, "info": "Sa première apparition majeure", "youtube_id": "8PTDv_szmL0"},
            {"title": "Billionaire", "artist": "Travie McCoy ft. Bruno Mars", "year": 2010, "info": "Co-écrit avec Travie McCoy"},
            {"title": "F**k You (Forget You)", "artist": "Cee Lo Green", "year": 2010, "info": "Hit mondial écrit par Bruno et Philip Lawrence", "youtube_id": "pc0mxOXbWIU"},
            {"title": "Lighters", "artist": "Bad Meets Evil ft. Bruno Mars", "year": 2011, "info": "Featuring Eminem et Royce da 5'9\"", "youtube_id": "Y8wifV5RYr8"},
            {"title": "Wavin' Flag", "artist": "K'naan", "year": 2010, "info": "Hymne de la Coupe du Monde - Bruno a co-écrit la version Coca-Cola"},
            {"title": "All I Ask", "artist": "Adele", "year": 2015, "info": "Co-écrite pour l'album '25'", "youtube_id": "2-MBfn8XjIU"}
        ]
    },
    "max martin": {
        "anecdotes": [
            "Max Martin est le songwriter avec le plus de #1 aux USA après Paul McCartney et John Lennon.",
            "Il a écrit 25 chansons #1 au Billboard Hot 100.",
            "Son vrai nom est Karl Martin Sandberg - il vient de Suède.",
            "Il refuse presque toutes les interviews et reste très discret malgré son succès."
        ],
        "songs_written_for_others": [
            {"title": "...Baby One More Time", "artist": "Britney Spears", "year": 1998, "info": "La chanson qui a lancé Britney et Max Martin", "youtube_id": "C-u5WLJ9Yk4"},
            {"title": "I Want It That Way", "artist": "Backstreet Boys", "year": 1999, "info": "Considérée comme l'une des meilleures chansons pop de tous les temps", "youtube_id": "4fndeDfaWCg"},
            {"title": "Shake It Off", "artist": "Taylor Swift", "year": 2014, "info": "Premier single de l'album '1989'", "youtube_id": "nfWlot6h_JM"},
            {"title": "Blank Space", "artist": "Taylor Swift", "year": 2014, "info": "Écrite avec Taylor et Shellback", "youtube_id": "e-ORhEE9VVg"},
            {"title": "Can't Feel My Face", "artist": "The Weeknd", "year": 2015, "info": "A relancé la carrière de Max Martin", "youtube_id": "KEI4qSrkPAs"},
            {"title": "Roar", "artist": "Katy Perry", "year": 2013, "info": "Hymne d'empowerment", "youtube_id": "CevxZvSJLk8"},
            {"title": "Since U Been Gone", "artist": "Kelly Clarkson", "year": 2004, "info": "A transformé Kelly en superstar", "youtube_id": "R7UrFYvl5TE"},
            {"title": "Teenage Dream", "artist": "Katy Perry", "year": 2010, "info": "L'album a égalé le record de Michael Jackson avec 5 singles #1", "youtube_id": "98WtmW-lfeE"},
            {"title": "Problem", "artist": "Ariana Grande", "year": 2014, "info": "Avec Big Sean et Iggy Azalea"}
        ]
    },
    "the-dream": {
        "anecdotes": [
            "The-Dream a écrit 'Umbrella' en seulement 10 minutes dans un taxi.",
            "Son vrai nom est Terius Youngdell Nash.",
            "Il a remporté plusieurs Grammy Awards pour ses compositions.",
            "Il était marié à Christina Milian de 2009 à 2011."
        ],
        "songs_written_for_others": [
            {"title": "Umbrella", "artist": "Rihanna ft. Jay-Z", "year": 2007, "info": "La chanson était destinée à Britney Spears mais elle l'a refusée", "youtube_id": "CvBfHwUxHIk"},
            {"title": "Single Ladies", "artist": "Beyoncé", "year": 2008, "info": "L'un des plus grands hits de Beyoncé", "youtube_id": "4m1EFMoRFvY"},
            {"title": "Baby", "artist": "Justin Bieber", "year": 2010, "info": "Le clip le plus vu de YouTube pendant des années", "youtube_id": "kffacxfA7G4"},
            {"title": "Me Against the Music", "artist": "Britney Spears ft. Madonna", "year": 2003, "info": "Collaboration iconique"},
            {"title": "Rude Boy", "artist": "Rihanna", "year": 2010, "info": "#1 pendant 5 semaines", "youtube_id": "e82VE8UtW8A"}
        ]
    },
    "ryan tedder": {
        "anecdotes": [
            "Ryan est le chanteur de OneRepublic mais aussi l'un des producteurs les plus demandés.",
            "Il a un studio chez lui qu'il appelle 'Patriot Studios'.",
            "Il a failli vendre 'Halo' à plusieurs artistes avant que Beyoncé ne la prenne.",
            "Ryan souffre d'une perte auditive partielle à cause de l'exposition aux concerts."
        ],
        "songs_written_for_others": [
            {"title": "Halo", "artist": "Beyoncé", "year": 2008, "info": "Leona Lewis a sorti 'Bleeding Love' avec une mélodie similaire car Ryan avait proposé les deux", "youtube_id": "bnVUHWCynig"},
            {"title": "Bleeding Love", "artist": "Leona Lewis", "year": 2007, "info": "Premier single #1 UK de Leona", "youtube_id": "Vzo-EL_62fQ"},
            {"title": "Rumour Has It", "artist": "Adele", "year": 2011, "info": "Sur l'album historique '21'", "youtube_id": "eB03nPXlhXc"},
            {"title": "Already Gone", "artist": "Kelly Clarkson", "year": 2009, "info": "Kelly était furieuse car la mélodie ressemblait à 'Halo'"},
            {"title": "Battlefield", "artist": "Jordin Sparks", "year": 2009, "info": "Power ballad"},
            {"title": "Apologize", "artist": "Timbaland ft. OneRepublic", "year": 2007, "info": "Le remix a propulsé le groupe", "youtube_id": "ZSM3w1v-A_Y"}
        ]
    },
    "diane warren": {
        "anecdotes": [
            "Diane a été nominée 13 fois aux Oscars sans jamais gagner - un record.",
            "Elle travaille seule et n'a jamais co-écrit une chanson de sa vie.",
            "Elle a écrit sa première chanson à 11 ans.",
            "Elle garde tous ses manuscrits originaux dans un coffre-fort."
        ],
        "songs_written_for_others": [
            {"title": "I Don't Want to Miss a Thing", "artist": "Aerosmith", "year": 1998, "info": "Pour le film Armageddon - seul #1 d'Aerosmith", "youtube_id": "JkK8g6FMEXE"},
            {"title": "Because You Loved Me", "artist": "Céline Dion", "year": 1996, "info": "Pour le film 'Up Close and Personal'", "youtube_id": "amzNDmp4tVI"},
            {"title": "Un-Break My Heart", "artist": "Toni Braxton", "year": 1996, "info": "Un des plus grands succès de Toni", "youtube_id": "p2Rch6WvPJE"},
            {"title": "If I Could Turn Back Time", "artist": "Cher", "year": 1989, "info": "Retour triomphal de Cher", "youtube_id": "BsKbwR7WXN4"},
            {"title": "Nothing's Gonna Stop Us Now", "artist": "Starship", "year": 1987, "info": "Pour le film Mannequin"},
            {"title": "How Do I Live", "artist": "LeAnn Rimes / Trisha Yearwood", "year": 1997, "info": "Les deux versions sont sorties en même temps!"}
        ]
    },
    "daft punk": {
        "anecdotes": [
            "Thomas Bangalter et Guy-Manuel de Homem-Christo se sont rencontrés au lycée à Paris.",
            "Ils portent des casques de robots depuis 1999 pour rester anonymes.",
            "Le nom 'Daft Punk' vient d'une critique négative de leur ancien groupe Darlin'.",
            "Ils ont mis 5 ans à créer l'album 'Random Access Memories'."
        ],
        "songs_written_for_others": [
            {"title": "Outlands", "artist": "Daft Punk (TRON: Legacy)", "year": 2010, "info": "Bande originale complète du film Disney"},
            {"title": "Starboy", "artist": "The Weeknd", "year": 2016, "info": "Collaboration surprise avec le chanteur canadien", "youtube_id": "34Na4j8AVgA"},
            {"title": "I Feel It Coming", "artist": "The Weeknd", "year": 2016, "info": "Deuxième collaboration sur l'album 'Starboy'", "youtube_id": "qFLhGq0060w"}
        ]
    },
    "kanye west": {
        "anecdotes": [
            "Kanye a survécu à un accident de voiture en 2002 et a enregistré 'Through the Wire' avec la mâchoire encore câblée.",
            "Il a été refusé par plusieurs labels car ils ne voyaient pas un producteur devenir rappeur.",
            "Son album 'My Beautiful Dark Twisted Fantasy' est considéré comme l'un des meilleurs albums de tous les temps.",
            "Il a changé son nom légal en 'Ye' en 2021."
        ],
        "songs_written_for_others": [
            {"title": "You Don't Know My Name", "artist": "Alicia Keys", "year": 2003, "info": "Premier hit produit par Kanye pour une autre artiste", "youtube_id": "ByS-JzuJNtc"},
            {"title": "Stand Up", "artist": "Ludacris", "year": 2003, "info": "Production emblématique"},
            {"title": "Talk About Our Love", "artist": "Brandy", "year": 2004, "info": "Single à succès"},
            {"title": "Encore", "artist": "Jay-Z", "year": 2003, "info": "Sur l'album 'The Black Album'"},
            {"title": "Lucifer", "artist": "Jay-Z", "year": 2003, "info": "Sample soul signature de Kanye"},
            {"title": "Run This Town", "artist": "Jay-Z ft. Rihanna & Kanye", "year": 2009, "info": "Collaboration épique", "youtube_id": "tPGc9Fg80jI"}
        ]
    },
    "rihanna": {
        "anecdotes": [
            "Rihanna a été découverte à 16 ans par Evan Rogers lors d'un voyage à la Barbade.",
            "Elle a sorti 8 albums en 7 ans entre 2005 et 2012 - un rythme incroyable.",
            "Son vrai nom est Robyn Rihanna Fenty.",
            "Elle est devenue la première milliardaire de la musique grâce à Fenty Beauty."
        ],
        "songs_written_for_others": [
            {"title": "Bitch Better Have My Money", "artist": "Rihanna", "year": 2015, "info": "Co-écrite par Rihanna, rare moment où elle écrit"},
            {"title": "American Oxygen", "artist": "Rihanna", "year": 2015, "info": "Message politique fort"}
        ]
    },
    "justin bieber": {
        "anecdotes": [
            "Justin a été découvert par Scooter Braun sur YouTube à 13 ans.",
            "Il a battu le record de concerts sold-out au Madison Square Garden à 18 ans.",
            "Il souffre de la maladie de Lyme diagnostiquée en 2020.",
            "Il s'est marié avec Hailey Baldwin en 2018."
        ],
        "songs_written_for_others": []
    },
    "taylor swift": {
        "anecdotes": [
            "Taylor a déménagé au Tennessee à 14 ans pour poursuivre sa carrière country.",
            "Elle réenregistre tous ses anciens albums pour en récupérer les droits.",
            "C'est la seule artiste à avoir 4 albums vendus à plus d'1 million en première semaine.",
            "Elle cache des indices (Easter eggs) dans tout ce qu'elle fait pour ses fans."
        ],
        "songs_written_for_others": [
            {"title": "This Is What You Came For", "artist": "Calvin Harris ft. Rihanna", "year": 2016, "info": "Écrite sous le pseudonyme 'Nils Sjöberg' quand elle sortait avec Calvin", "youtube_id": "kOkQ4T5WO9E"},
            {"title": "Better Man", "artist": "Little Big Town", "year": 2016, "info": "Grammy de la meilleure chanson country", "youtube_id": "Z3KHPEPQDGY"},
            {"title": "Babe", "artist": "Sugarland", "year": 2018, "info": "Taylor fait les choeurs sur la chanson"}
        ]
    }
}

def get_artist_songwriting_data(artist_name: str):
    """Get curated songwriting data for an artist"""
    # Normalize artist name
    normalized = artist_name.lower().strip()
    
    # Try exact match first
    if normalized in FAMOUS_SONGWRITING_CREDITS:
        return FAMOUS_SONGWRITING_CREDITS[normalized]
    
    # Try partial match
    for key in FAMOUS_SONGWRITING_CREDITS:
        if key in normalized or normalized in key:
            return FAMOUS_SONGWRITING_CREDITS[key]
        # Also check without special characters
        clean_key = key.replace("-", " ").replace("'", "")
        clean_name = normalized.replace("-", " ").replace("'", "")
        if clean_key in clean_name or clean_name in clean_key:
            return FAMOUS_SONGWRITING_CREDITS[key]
    
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
