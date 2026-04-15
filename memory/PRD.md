# Music Hub PRD

## Architecture
- **Backend**: FastAPI + MongoDB + Deezer API + Discogs API + Billboard scraping
- **Frontend**: React + Tailwind CSS + Lucide icons
- **Database**: MongoDB (high scores), Python dict (curated songwriting credits)

## What's Implemented
- **Artist Search**: Deezer API autocomplete search
- **Artist Page**: Bio, albums, top tracks with inline Deezer audio previews, collaborations from Discogs
- **Anecdotes**: 72 artists with curated anecdotes (228 total)
- **Ghostwriting Credits**: 286 songs written for other artists with inline YouTube player
- **Billboard Top 100**: Web scraping (current week + year-end 2010-now)
- **Blind Test**: YouTube embeds, score tracking, MongoDB high scores
- **French Artists (19)**: Aya Nakamura, Jul, PNL, Nekfeu, Damso, Orelsan, Booba, Ninho, Maître Gims, MC Solaar, IAM, Tiakola, Niska, Francis Cabrel, Édith Piaf, Stromae, Angèle, Daft Punk, David Guetta
- **Inline Players**: Deezer 30-sec preview audio player + YouTube inline embed player

## Backlog
- P1: Add more French artists (Aya Nakamura, Gazo, SDM, Werenoi, Laylow)
- P1: Integrate Genius API for auto-enriching credits
- P2: Make credits clickable (link to artist pages)
- P2: Quiz Ghostwriter game mode
- P3: Artist graph visualization
