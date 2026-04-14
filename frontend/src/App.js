import React, { useState, useEffect, useCallback } from "react";
import "@/App.css";
import { BrowserRouter, Routes, Route, useNavigate, useParams, Link } from "react-router-dom";
import axios from "axios";
import { Search, Trophy, Music, ArrowLeft, Play, Clock, Disc, Users, ChevronRight, Volume2, Check, X, Loader2, Pen } from "lucide-react";

const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;
const API = `${BACKEND_URL}/api`;

// ==================== HEADER COMPONENT ====================
const Header = ({ showSearch = true }) => {
  const navigate = useNavigate();
  const [searchQuery, setSearchQuery] = useState("");
  const [searchResults, setSearchResults] = useState([]);
  const [showDropdown, setShowDropdown] = useState(false);
  const [isSearching, setIsSearching] = useState(false);

  const searchArtists = useCallback(async (query) => {
    if (!query.trim()) {
      setSearchResults([]);
      return;
    }
    
    setIsSearching(true);
    try {
      const response = await axios.get(`${API}/search/artists`, { params: { q: query } });
      setSearchResults(response.data.artists || []);
    } catch (error) {
      console.error("Search error:", error);
      setSearchResults([]);
    } finally {
      setIsSearching(false);
    }
  }, []);

  useEffect(() => {
    const timer = setTimeout(() => {
      if (searchQuery) {
        searchArtists(searchQuery);
      }
    }, 300);
    return () => clearTimeout(timer);
  }, [searchQuery, searchArtists]);

  const handleArtistClick = (artist) => {
    setShowDropdown(false);
    setSearchQuery("");
    navigate(`/artist/${artist.id}`);
  };

  return (
    <header className="sticky top-0 z-50 glass border-b border-[#282828]">
      <div className="max-w-7xl mx-auto px-4 py-4 flex items-center justify-between gap-6">
        <Link to="/" className="flex items-center gap-2 hover:opacity-80 transition-opacity" data-testid="logo-link">
          <Music className="w-8 h-8 text-[#1db954]" />
          <span className="text-2xl font-black tracking-tight">
            MUSIC <span className="text-[#1db954]">HUB</span>
          </span>
        </Link>

        {showSearch && (
          <div className="relative flex-1 max-w-xl">
            <Search className="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-[#7A7A7A]" />
            <input
              type="text"
              value={searchQuery}
              onChange={(e) => {
                setSearchQuery(e.target.value);
                setShowDropdown(true);
              }}
              onFocus={() => setShowDropdown(true)}
              placeholder="Rechercher un artiste..."
              className="search-input"
              data-testid="search-input"
            />
            
            {showDropdown && (searchResults.length > 0 || isSearching) && (
              <div className="dropdown-menu" data-testid="search-dropdown">
                {isSearching ? (
                  <div className="p-4 flex items-center justify-center gap-2 text-[#B3B3B3]">
                    <Loader2 className="w-5 h-5 animate-spin" />
                    Recherche...
                  </div>
                ) : (
                  searchResults.map((artist) => (
                    <div
                      key={artist.id}
                      className="dropdown-item"
                      onClick={() => handleArtistClick(artist)}
                      data-testid={`artist-result-${artist.id}`}
                    >
                      <img
                        src={artist.picture_medium || artist.picture || "/placeholder-artist.png"}
                        alt={artist.name}
                        className="w-12 h-12 rounded-full object-cover"
                        onError={(e) => { e.target.src = "https://via.placeholder.com/48?text=A"; }}
                      />
                      <div>
                        <p className="font-semibold text-white">{artist.name}</p>
                        <p className="text-sm text-[#B3B3B3]">{artist.nb_fan?.toLocaleString()} fans</p>
                      </div>
                    </div>
                  ))
                )}
              </div>
            )}
          </div>
        )}

        <nav className="hidden md:flex items-center gap-4">
          <Link 
            to="/billboard" 
            className="btn-secondary text-sm py-2 px-4"
            data-testid="nav-billboard"
          >
            Top 100
          </Link>
          <Link 
            to="/blindtest" 
            className="btn-primary text-sm py-2 px-4"
            data-testid="nav-blindtest"
          >
            Blind Test
          </Link>
        </nav>
      </div>

      {/* Click outside to close dropdown */}
      {showDropdown && (
        <div 
          className="fixed inset-0 z-40" 
          onClick={() => setShowDropdown(false)}
        />
      )}
    </header>
  );
};

// ==================== HOME PAGE ====================
const Home = () => {
  const navigate = useNavigate();

  return (
    <div className="min-h-screen">
      <Header showSearch={true} />
      
      {/* Hero Section */}
      <section className="gradient-hero pt-20 pb-32 px-4" data-testid="hero-section">
        <div className="max-w-4xl mx-auto text-center">
          <h1 className="text-5xl sm:text-6xl lg:text-7xl font-black tracking-tight mb-6 animate-fadeIn">
            L'encyclopédie de tes
            <span className="text-[#1db954] block mt-2">artistes préférés</span>
          </h1>
          <p className="text-xl text-[#B3B3B3] max-w-2xl mx-auto mb-10 animate-fadeIn stagger-1">
            Découvre les artistes, explore les classements Billboard et teste tes connaissances musicales.
          </p>
        </div>
      </section>

      {/* Feature Cards */}
      <section className="max-w-4xl mx-auto px-4 -mt-16" data-testid="features-section">
        <div className="grid md:grid-cols-2 gap-6">
          <div 
            className="feature-card animate-fadeIn stagger-2"
            onClick={() => navigate("/billboard")}
            data-testid="billboard-card"
          >
            <div className="flex items-center gap-4 mb-4">
              <div className="w-14 h-14 rounded-full bg-[#282828] flex items-center justify-center">
                <Trophy className="w-7 h-7 text-[#1db954]" />
              </div>
              <h2 className="text-2xl font-bold">Billboard Top 100</h2>
            </div>
            <p className="text-[#B3B3B3] mb-4">
              Explore les classements de 2010 à aujourd'hui. Découvre les hits qui ont marqué chaque année.
            </p>
            <div className="flex items-center text-[#1db954] font-semibold">
              Voir les classements <ChevronRight className="w-5 h-5 ml-1" />
            </div>
          </div>

          <div 
            className="feature-card animate-fadeIn stagger-3"
            onClick={() => navigate("/blindtest")}
            data-testid="blindtest-card"
          >
            <div className="flex items-center gap-4 mb-4">
              <div className="w-14 h-14 rounded-full bg-[#282828] flex items-center justify-center">
                <Volume2 className="w-7 h-7 text-[#1db954]" />
              </div>
              <h2 className="text-2xl font-bold">Blind Test</h2>
            </div>
            <p className="text-[#B3B3B3] mb-4">
              Sauras-tu reconnaître ces tubes en seulement quelques secondes ? Teste tes connaissances !
            </p>
            <div className="flex items-center text-[#1db954] font-semibold">
              Jouer maintenant <ChevronRight className="w-5 h-5 ml-1" />
            </div>
          </div>
        </div>
      </section>

      {/* Popular Artists Preview */}
      <section className="max-w-6xl mx-auto px-4 py-20" data-testid="popular-section">
        <h2 className="text-3xl font-bold mb-8">Artistes populaires</h2>
        <p className="text-[#B3B3B3] mb-8">
          Utilise la barre de recherche pour découvrir n'importe quel artiste sur Deezer.
        </p>
      </section>

      {/* Footer */}
      <footer className="border-t border-[#282828] py-8 px-4">
        <div className="max-w-6xl mx-auto text-center text-[#7A7A7A]">
          <p>Music Hub - Données fournies par Deezer & Billboard</p>
        </div>
      </footer>
    </div>
  );
};

// ==================== ARTIST PAGE ====================
const ArtistPage = () => {
  const { artistId } = useParams();
  const navigate = useNavigate();
  const [artist, setArtist] = useState(null);
  const [albums, setAlbums] = useState([]);
  const [topTracks, setTopTracks] = useState([]);
  const [relatedArtists, setRelatedArtists] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchArtistData = async () => {
      setLoading(true);
      setError(null);
      try {
        const [artistRes, albumsRes, tracksRes, relatedRes] = await Promise.all([
          axios.get(`${API}/artist/${artistId}`),
          axios.get(`${API}/artist/${artistId}/albums`),
          axios.get(`${API}/artist/${artistId}/top`),
          axios.get(`${API}/artist/${artistId}/related`)
        ]);
        
        setArtist(artistRes.data);
        setAlbums(albumsRes.data.albums || []);
        setTopTracks(tracksRes.data.tracks || []);
        setRelatedArtists(relatedRes.data.related || []);
      } catch (err) {
        console.error("Error fetching artist:", err);
        setError("Impossible de charger les données de l'artiste");
      } finally {
        setLoading(false);
      }
    };

    fetchArtistData();
  }, [artistId]);

  const formatDuration = (seconds) => {
    const mins = Math.floor(seconds / 60);
    const secs = seconds % 60;
    return `${mins}:${secs.toString().padStart(2, '0')}`;
  };

  if (loading) {
    return (
      <div className="min-h-screen">
        <Header />
        <div className="flex items-center justify-center py-32">
          <Loader2 className="w-12 h-12 text-[#1db954] animate-spin" />
        </div>
      </div>
    );
  }

  if (error || !artist) {
    return (
      <div className="min-h-screen">
        <Header />
        <div className="max-w-4xl mx-auto px-4 py-20 text-center">
          <p className="text-xl text-[#B3B3B3] mb-8">{error || "Artiste non trouvé"}</p>
          <button onClick={() => navigate("/")} className="btn-primary">
            Retour à l'accueil
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen" data-testid="artist-page">
      <Header />
      
      {/* Artist Hero */}
      <section className="relative">
        <div 
          className="h-80 bg-cover bg-center"
          style={{ 
            backgroundImage: `linear-gradient(to bottom, rgba(18,18,18,0.3), #121212), url(${artist.picture_xl || artist.picture_big})` 
          }}
        />
        <div className="absolute bottom-0 left-0 right-0 p-8">
          <div className="max-w-6xl mx-auto flex items-end gap-6">
            <img
              src={artist.picture_big || artist.picture_medium}
              alt={artist.name}
              className="w-48 h-48 rounded-full shadow-2xl object-cover border-4 border-[#181818]"
              data-testid="artist-image"
            />
            <div className="pb-4">
              <p className="text-sm uppercase tracking-widest text-[#B3B3B3] mb-2">Artiste</p>
              <h1 className="text-5xl md:text-6xl font-black mb-4" data-testid="artist-name">{artist.name}</h1>
              <div className="flex items-center gap-6 text-[#B3B3B3]">
                <span className="flex items-center gap-2">
                  <Users className="w-5 h-5" />
                  {artist.nb_fan?.toLocaleString()} fans
                </span>
                <span className="flex items-center gap-2">
                  <Disc className="w-5 h-5" />
                  {artist.nb_album} albums
                </span>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Content */}
      <section className="max-w-6xl mx-auto px-4 py-12">
        <div className="grid lg:grid-cols-5 gap-12">
          {/* Top Tracks */}
          <div className="lg:col-span-3">
            <h2 className="text-2xl font-bold mb-6">Titres populaires</h2>
            <div className="space-y-2" data-testid="top-tracks">
              {topTracks.map((track, index) => (
                <div 
                  key={track.id} 
                  className="track-row flex items-center gap-4 animate-fadeIn"
                  style={{ animationDelay: `${index * 0.05}s` }}
                  data-testid={`track-${track.id}`}
                >
                  <span className="w-8 text-center text-[#7A7A7A] font-medium">{index + 1}</span>
                  <img
                    src={track.album?.cover_medium || track.album?.cover}
                    alt={track.album?.title}
                    className="w-12 h-12 rounded"
                    onError={(e) => { e.target.src = "https://via.placeholder.com/48?text=A"; }}
                  />
                  <div className="flex-1 min-w-0">
                    <p className="font-medium truncate">{track.title}</p>
                    <p className="text-sm text-[#B3B3B3] truncate">{track.album?.title}</p>
                  </div>
                  {track.preview && (
                    <a 
                      href={track.preview} 
                      target="_blank" 
                      rel="noopener noreferrer"
                      className="p-2 hover:bg-[#282828] rounded-full transition-colors"
                    >
                      <Play className="w-5 h-5 text-[#1db954]" />
                    </a>
                  )}
                  <span className="text-[#7A7A7A] text-sm w-12 text-right">
                    <Clock className="w-4 h-4 inline mr-1" />
                    {formatDuration(track.duration)}
                  </span>
                </div>
              ))}
            </div>
          </div>

          {/* Albums */}
          <div className="lg:col-span-2">
            <h2 className="text-2xl font-bold mb-6">Discographie</h2>
            <div className="space-y-4" data-testid="albums-list">
              {albums.slice(0, 8).map((album, index) => (
                <div 
                  key={album.id} 
                  className="flex items-center gap-4 p-3 rounded-lg hover:bg-[#282828] transition-colors animate-fadeIn"
                  style={{ animationDelay: `${index * 0.05}s` }}
                  data-testid={`album-${album.id}`}
                >
                  <img
                    src={album.cover_medium || album.cover}
                    alt={album.title}
                    className="w-16 h-16 rounded shadow-lg"
                    onError={(e) => { e.target.src = "https://via.placeholder.com/64?text=A"; }}
                  />
                  <div>
                    <p className="font-semibold">{album.title}</p>
                    <p className="text-sm text-[#B3B3B3]">{album.release_date?.slice(0, 4)}</p>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>

        {/* Collaborations & Connexions Section */}
        {relatedArtists.length > 0 && (
          <div className="mt-16" data-testid="collaborations-section">
            <h2 className="text-2xl font-bold mb-2">Collaborations & Connexions</h2>
            <p className="text-[#B3B3B3] text-sm mb-6">Artistes liés et collaborateurs</p>
            
            <div className="collab-grid">
              {relatedArtists.slice(0, 10).map((related, index) => (
                <div 
                  key={related.id}
                  className="collab-item animate-fadeIn"
                  style={{ animationDelay: `${index * 0.05}s` }}
                  onClick={() => navigate(`/artist/${related.id}`)}
                  data-testid={`collab-${related.id}`}
                >
                  {/* Random ghostwriter badge for demo - in real app this would come from data */}
                  {index === 2 && (
                    <span className="ghost-writer-badge">
                      <Pen className="w-3 h-3 inline mr-1" />
                      PLUME
                    </span>
                  )}
                  <div className={`collab-circle ${index === 2 ? 'ghostwriter' : ''}`}>
                    {related.picture_medium ? (
                      <img 
                        src={related.picture_medium} 
                        alt={related.name}
                        onError={(e) => { 
                          e.target.style.display = 'none';
                          e.target.parentNode.innerText = related.initials;
                        }}
                      />
                    ) : (
                      related.initials
                    )}
                  </div>
                  <span className="collab-name">{related.name}</span>
                </div>
              ))}
            </div>
          </div>
        )}
      </section>

      {/* Back button */}
      <div className="max-w-6xl mx-auto px-4 pb-12">
        <button 
          onClick={() => navigate(-1)} 
          className="flex items-center gap-2 text-[#B3B3B3] hover:text-white transition-colors"
          data-testid="back-button"
        >
          <ArrowLeft className="w-5 h-5" />
          Retour
        </button>
      </div>
    </div>
  );
};

// ==================== BILLBOARD PAGE ====================
const BillboardPage = () => {
  const navigate = useNavigate();
  const currentYear = new Date().getFullYear();
  const [selectedYear, setSelectedYear] = useState(currentYear);
  const [songs, setSongs] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [isCurrentWeek, setIsCurrentWeek] = useState(true);

  const years = Array.from({ length: currentYear - 2009 }, (_, i) => currentYear - i);

  useEffect(() => {
    const fetchBillboard = async () => {
      setLoading(true);
      setError(null);
      try {
        let response;
        if (isCurrentWeek) {
          response = await axios.get(`${API}/billboard/hot100`);
        } else {
          response = await axios.get(`${API}/billboard/year/${selectedYear}`);
        }
        setSongs(response.data.songs || []);
      } catch (err) {
        console.error("Error fetching Billboard:", err);
        setError("Impossible de charger le classement Billboard");
        setSongs([]);
      } finally {
        setLoading(false);
      }
    };

    fetchBillboard();
  }, [selectedYear, isCurrentWeek]);

  return (
    <div className="min-h-screen" data-testid="billboard-page">
      <Header />
      
      {/* Hero */}
      <section className="gradient-hero py-16 px-4">
        <div className="max-w-4xl mx-auto">
          <button 
            onClick={() => navigate(-1)} 
            className="flex items-center gap-2 text-[#B3B3B3] hover:text-white transition-colors mb-8"
            data-testid="back-button"
          >
            <ArrowLeft className="w-5 h-5" />
            Retour
          </button>
          
          <div className="flex items-center gap-4 mb-6">
            <div className="w-16 h-16 rounded-full bg-[#282828] flex items-center justify-center">
              <Trophy className="w-8 h-8 text-[#1db954]" />
            </div>
            <div>
              <h1 className="text-4xl md:text-5xl font-black">Billboard Hot 100</h1>
              <p className="text-[#B3B3B3]">Les plus grands hits américains</p>
            </div>
          </div>

          {/* View Toggle */}
          <div className="flex gap-4 mb-6">
            <button
              onClick={() => setIsCurrentWeek(true)}
              className={`btn-${isCurrentWeek ? 'primary' : 'secondary'} text-sm py-2 px-4`}
              data-testid="current-week-btn"
            >
              Cette semaine
            </button>
            <button
              onClick={() => setIsCurrentWeek(false)}
              className={`btn-${!isCurrentWeek ? 'primary' : 'secondary'} text-sm py-2 px-4`}
              data-testid="year-end-btn"
            >
              Classement annuel
            </button>
          </div>

          {/* Year Selector */}
          {!isCurrentWeek && (
            <div className="flex flex-wrap gap-2" data-testid="year-selector">
              {years.map((year) => (
                <button
                  key={year}
                  onClick={() => setSelectedYear(year)}
                  className={`year-btn ${selectedYear === year ? 'active' : ''}`}
                  data-testid={`year-${year}`}
                >
                  {year}
                </button>
              ))}
            </div>
          )}
        </div>
      </section>

      {/* Chart List */}
      <section className="max-w-4xl mx-auto px-4 py-8">
        {loading ? (
          <div className="flex items-center justify-center py-20">
            <Loader2 className="w-12 h-12 text-[#1db954] animate-spin" />
          </div>
        ) : error ? (
          <div className="text-center py-20">
            <p className="text-[#B3B3B3] mb-4">{error}</p>
            <button onClick={() => window.location.reload()} className="btn-primary">
              Réessayer
            </button>
          </div>
        ) : songs.length === 0 ? (
          <div className="text-center py-20">
            <p className="text-[#B3B3B3]">Aucune chanson trouvée pour cette période.</p>
          </div>
        ) : (
          <div className="bg-[#181818] rounded-xl overflow-hidden" data-testid="billboard-list">
            <div className="grid grid-cols-[60px_1fr_1fr] gap-4 px-6 py-4 border-b border-[#282828] text-[#7A7A7A] text-sm font-medium uppercase tracking-wider">
              <span>#</span>
              <span>Titre</span>
              <span>Artiste</span>
            </div>
            {songs.map((song, index) => (
              <div 
                key={`${song.rank}-${song.title}`}
                className="billboard-row grid grid-cols-[60px_1fr_1fr] gap-4 items-center animate-fadeIn"
                style={{ animationDelay: `${index * 0.02}s` }}
                data-testid={`billboard-row-${song.rank}`}
              >
                <span className={`text-2xl font-black ${song.rank <= 10 ? 'text-[#1db954]' : 'text-[#7A7A7A]'}`}>
                  {song.rank}
                </span>
                <span className="font-semibold truncate">{song.title}</span>
                <span className="text-[#B3B3B3] truncate">{song.artist}</span>
              </div>
            ))}
          </div>
        )}
      </section>
    </div>
  );
};

// ==================== BLIND TEST PAGE ====================
const BlindTestPage = () => {
  const navigate = useNavigate();
  const [gameState, setGameState] = useState("start"); // start, playing, finished
  const [songs, setSongs] = useState([]);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [score, setScore] = useState(0);
  const [selectedAnswer, setSelectedAnswer] = useState(null);
  const [showResult, setShowResult] = useState(false);
  const [playerName, setPlayerName] = useState("");
  const [highScores, setHighScores] = useState([]);
  const [loading, setLoading] = useState(false);

  const fetchHighScores = async () => {
    try {
      const response = await axios.get(`${API}/blindtest/highscores`);
      setHighScores(response.data.scores || []);
    } catch (error) {
      console.error("Error fetching high scores:", error);
    }
  };

  useEffect(() => {
    fetchHighScores();
  }, []);

  const startGame = async () => {
    if (!playerName.trim()) return;
    
    setLoading(true);
    try {
      const response = await axios.get(`${API}/blindtest/songs`, { params: { count: 10 } });
      setSongs(response.data.songs || []);
      setCurrentIndex(0);
      setScore(0);
      setSelectedAnswer(null);
      setShowResult(false);
      setGameState("playing");
    } catch (error) {
      console.error("Error starting game:", error);
    } finally {
      setLoading(false);
    }
  };

  const handleAnswer = (choice) => {
    if (selectedAnswer !== null) return;
    
    setSelectedAnswer(choice);
    setShowResult(true);
    
    if (choice.correct) {
      setScore(prev => prev + 1);
    }
  };

  const nextQuestion = async () => {
    if (currentIndex + 1 >= songs.length) {
      // Game finished - save score
      try {
        await axios.post(`${API}/blindtest/score`, null, {
          params: {
            player_name: playerName,
            score: score,
            total_questions: songs.length
          }
        });
        await fetchHighScores();
      } catch (error) {
        console.error("Error saving score:", error);
      }
      setGameState("finished");
    } else {
      setCurrentIndex(prev => prev + 1);
      setSelectedAnswer(null);
      setShowResult(false);
    }
  };

  const currentSong = songs[currentIndex];

  return (
    <div className="min-h-screen" data-testid="blindtest-page">
      <Header showSearch={false} />

      {/* Start Screen */}
      {gameState === "start" && (
        <section className="max-w-2xl mx-auto px-4 py-20 text-center">
          <button 
            onClick={() => navigate(-1)} 
            className="flex items-center gap-2 text-[#B3B3B3] hover:text-white transition-colors mb-12 mx-auto"
            data-testid="back-button"
          >
            <ArrowLeft className="w-5 h-5" />
            Retour
          </button>

          <div className="w-24 h-24 rounded-full bg-[#282828] flex items-center justify-center mx-auto mb-8">
            <Volume2 className="w-12 h-12 text-[#1db954]" />
          </div>
          
          <h1 className="text-4xl md:text-5xl font-black mb-4">Blind Test</h1>
          <p className="text-xl text-[#B3B3B3] mb-12">
            Écoute l'extrait et devine la chanson !
          </p>

          <div className="max-w-sm mx-auto mb-8">
            <input
              type="text"
              value={playerName}
              onChange={(e) => setPlayerName(e.target.value)}
              placeholder="Entre ton pseudo..."
              className="search-input text-center"
              data-testid="player-name-input"
            />
          </div>

          <button
            onClick={startGame}
            disabled={!playerName.trim() || loading}
            className="btn-primary text-lg px-12 py-4"
            data-testid="start-game-btn"
          >
            {loading ? (
              <span className="flex items-center gap-2">
                <Loader2 className="w-5 h-5 animate-spin" />
                Chargement...
              </span>
            ) : (
              "Commencer le jeu"
            )}
          </button>

          {/* High Scores */}
          {highScores.length > 0 && (
            <div className="mt-16">
              <h2 className="text-2xl font-bold mb-6">Meilleurs scores</h2>
              <div className="bg-[#181818] rounded-xl p-6" data-testid="high-scores">
                {highScores.slice(0, 5).map((hs, index) => (
                  <div 
                    key={hs.id || index}
                    className="flex items-center justify-between py-3 border-b border-[#282828] last:border-0"
                  >
                    <div className="flex items-center gap-4">
                      <span className={`text-xl font-bold ${index < 3 ? 'text-[#1db954]' : 'text-[#7A7A7A]'}`}>
                        #{index + 1}
                      </span>
                      <span className="font-semibold">{hs.player_name}</span>
                    </div>
                    <span className="score-badge">
                      {hs.score}/{hs.total_questions}
                    </span>
                  </div>
                ))}
              </div>
            </div>
          )}
        </section>
      )}

      {/* Playing Screen */}
      {gameState === "playing" && currentSong && (
        <section className="max-w-3xl mx-auto px-4 py-12">
          {/* Progress */}
          <div className="mb-8">
            <div className="flex justify-between items-center mb-2">
              <span className="text-[#B3B3B3]">Question {currentIndex + 1}/{songs.length}</span>
              <span className="score-badge text-sm">Score: {score}</span>
            </div>
            <div className="progress-bar">
              <div 
                className="progress-fill"
                style={{ width: `${((currentIndex + 1) / songs.length) * 100}%` }}
              />
            </div>
          </div>

          {/* YouTube Player */}
          <div className="mb-8" data-testid="youtube-player">
            <div className="youtube-container bg-[#181818]">
              <iframe
                src={`https://www.youtube.com/embed/${currentSong.youtube_id}?autoplay=1&start=30&end=35&controls=0&modestbranding=1`}
                title="Blind Test"
                frameBorder="0"
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowFullScreen
              />
            </div>
            <p className="text-center text-[#B3B3B3] mt-4">
              Écoute l'extrait et choisis la bonne réponse !
            </p>
          </div>

          {/* Choices */}
          <div className="space-y-4" data-testid="choices">
            {currentSong.choices.map((choice, index) => {
              let btnClass = "choice-btn";
              if (showResult) {
                if (choice.correct) btnClass += " correct";
                else if (selectedAnswer === choice && !choice.correct) btnClass += " incorrect";
              }
              
              return (
                <button
                  key={index}
                  onClick={() => handleAnswer(choice)}
                  disabled={showResult}
                  className={btnClass}
                  data-testid={`choice-${index}`}
                >
                  <div className="flex items-center justify-between">
                    <div>
                      <p className="text-lg">{choice.title}</p>
                      <p className="text-sm text-[#B3B3B3]">{choice.artist}</p>
                    </div>
                    {showResult && choice.correct && (
                      <Check className="w-6 h-6 text-[#1db954]" />
                    )}
                    {showResult && selectedAnswer === choice && !choice.correct && (
                      <X className="w-6 h-6 text-red-500" />
                    )}
                  </div>
                </button>
              );
            })}
          </div>

          {/* Next Button */}
          {showResult && (
            <div className="mt-8 text-center">
              <button
                onClick={nextQuestion}
                className="btn-primary text-lg px-12 py-4"
                data-testid="next-question-btn"
              >
                {currentIndex + 1 >= songs.length ? "Voir les résultats" : "Question suivante"}
              </button>
            </div>
          )}
        </section>
      )}

      {/* Finished Screen */}
      {gameState === "finished" && (
        <section className="max-w-2xl mx-auto px-4 py-20 text-center">
          <div className="w-24 h-24 rounded-full bg-[#282828] flex items-center justify-center mx-auto mb-8">
            <Trophy className="w-12 h-12 text-[#1db954]" />
          </div>
          
          <h1 className="text-4xl md:text-5xl font-black mb-4">Partie terminée !</h1>
          <p className="text-xl text-[#B3B3B3] mb-8">
            Bravo {playerName} !
          </p>

          <div className="score-badge text-4xl px-12 py-6 inline-block mb-12" data-testid="final-score">
            {score}/{songs.length}
          </div>

          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <button
              onClick={() => {
                setGameState("start");
                setPlayerName("");
              }}
              className="btn-primary"
              data-testid="play-again-btn"
            >
              Rejouer
            </button>
            <button
              onClick={() => navigate("/")}
              className="btn-secondary"
              data-testid="home-btn"
            >
              Retour à l'accueil
            </button>
          </div>

          {/* Final High Scores */}
          {highScores.length > 0 && (
            <div className="mt-16">
              <h2 className="text-2xl font-bold mb-6">Classement</h2>
              <div className="bg-[#181818] rounded-xl p-6" data-testid="final-high-scores">
                {highScores.slice(0, 10).map((hs, index) => (
                  <div 
                    key={hs.id || index}
                    className={`flex items-center justify-between py-3 border-b border-[#282828] last:border-0 ${hs.player_name === playerName ? 'bg-[#1db954]/10 -mx-4 px-4 rounded' : ''}`}
                  >
                    <div className="flex items-center gap-4">
                      <span className={`text-xl font-bold ${index < 3 ? 'text-[#1db954]' : 'text-[#7A7A7A]'}`}>
                        #{index + 1}
                      </span>
                      <span className="font-semibold">{hs.player_name}</span>
                    </div>
                    <span className="font-bold text-[#1db954]">
                      {hs.score}/{hs.total_questions}
                    </span>
                  </div>
                ))}
              </div>
            </div>
          )}
        </section>
      )}
    </div>
  );
};

// ==================== APP ====================
function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/artist/:artistId" element={<ArtistPage />} />
          <Route path="/billboard" element={<BillboardPage />} />
          <Route path="/blindtest" element={<BlindTestPage />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
