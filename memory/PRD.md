# Music Hub PRD

## Architecture
- **Backend**: FastAPI + MongoDB + Deezer API + Discogs API + Genius API + Billboard scraping
- **Frontend**: React + Tailwind CSS + Lucide icons + react-force-graph-2d
- **Database**: MongoDB (high scores), Python dict (curated songwriting credits)

## What's Implemented
- **Artist Search**: Deezer API autocomplete search
- **Artist Page**: Bio, albums, top tracks with inline Deezer audio previews (30 sec), collaborations from Discogs
- **Anecdotes**: 72 artists with curated anecdotes (228 total) + 19 French artists
- **Ghostwriting Credits**: 286 curated songs + clickable artist names + inline YouTube player
- **Genius Credits**: Real-time songwriter/producer credits from Genius API (async loading)
- **Artist Connection Graph**: Interactive force-directed graph with artist photos, 2-level depth
- **Billboard Top 100**: Web scraping + Deezer audio previews + album art
- **Blind Test**: YouTube embeds, score tracking, MongoDB high scores
- **Inline Players**: Deezer 30-sec preview audio + YouTube inline embed

## API Keys
- Discogs Token: configured in backend .env
- Genius Token: configured in backend .env

## Backlog
- P1: Quiz Ghostwriter game mode
- P2: Cache Genius results in MongoDB
- P3: User favorites/bookmarks
