# Music Hub PRD

## Architecture
- **Backend**: FastAPI + MongoDB + Deezer API + Discogs API + Genius API + Billboard scraping
- **Frontend**: React + Tailwind CSS + Lucide icons
- **Database**: MongoDB (high scores), Python dict (curated songwriting credits)

## What's Implemented
- **Artist Search**: Deezer API autocomplete search
- **Artist Page**: Bio, albums, top tracks with inline Deezer audio previews (30 sec), collaborations from Discogs
- **Anecdotes**: 72 artists with curated anecdotes (228 total)
- **Ghostwriting Credits**: 286 curated songs written for other artists with inline YouTube player + clickable artist names
- **Genius Credits**: Real-time songwriter/producer credits from Genius API (loads asynchronously)
- **Clickable Artist Names**: All artist names in credits are clickable → search on Deezer → navigate to artist page
- **Billboard Top 100**: Web scraping (current week + year-end 2010-now)
- **Blind Test**: YouTube embeds, score tracking, MongoDB high scores
- **French Artists (19)**: Aya Nakamura, Jul, PNL, Nekfeu, Damso, Orelsan, Booba, Ninho, Maître Gims, MC Solaar, IAM, Tiakola, Niska, Francis Cabrel, Édith Piaf, Stromae, Angèle, Daft Punk, David Guetta
- **Inline Players**: Deezer 30-sec preview audio player + YouTube inline embed player

## API Keys
- Discogs Token: configured in backend .env
- Genius Token: configured in backend .env

## Backlog
- P1: Quiz Ghostwriter game mode
- P2: Artist connection graph visualization
- P2: Cache Genius results in MongoDB for faster loads
- P3: User favorites/bookmarks
