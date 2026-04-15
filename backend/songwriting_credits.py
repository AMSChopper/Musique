# -*- coding: utf-8 -*-
"""
Curated database of famous songwriting credits, anecdotes, and ghostwriting data.
"""

FAMOUS_SONGWRITING_CREDITS = {
    # ===================== MEGA SONGWRITERS =====================
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
            {"title": "Flames", "artist": "David Guetta & Sia", "year": 2018, "info": "Nouvelle collaboration avec Guetta", "youtube_id": "pSPdGdTLQkU"},
            {"title": "Unstoppable", "artist": "Sia", "year": 2016, "info": "Initialement écrite pour Demi Lovato mais Sia l'a gardée"},
            {"title": "Cheap Thrills", "artist": "Sia", "year": 2016, "info": "Écrite pour Rihanna à l'origine, devenue l'un de ses plus grands succès", "youtube_id": "nYh-n7EOtMA"}
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
            {"title": "Milkshake", "artist": "Kelis", "year": 2003, "info": "Produit avec Chad Hugo, devenu un hymne", "youtube_id": "pGL2rytTraA"},
            {"title": "Grindin'", "artist": "Clipse", "year": 2002, "info": "Beat minimaliste révolutionnaire", "youtube_id": "TjWAWcx4xdE"},
            {"title": "Frontin'", "artist": "Pharrell ft. Jay-Z", "year": 2003, "info": "Son premier single solo à succès"},
            {"title": "Sweetest Girl", "artist": "Wyclef Jean", "year": 2007, "info": "Featuring Akon, Lil Wayne et Niia"}
        ]
    },
    "bruno mars": {
        "anecdotes": [
            "Son vrai nom est Peter Gene Hernandez - 'Bruno' vient d'un catcheur et 'Mars' car les filles disaient qu'il n'était pas de cette planète.",
            "Il a commencé comme impersonator d'Elvis Presley à 4 ans à Hawaï.",
            "Bruno joue de plus de 10 instruments différents.",
            "Il a remporté 15 Grammy Awards au cours de sa carrière."
        ],
        "songs_written_for_others": [
            {"title": "Right Round", "artist": "Flo Rida", "year": 2009, "info": "Premier #1 de Bruno en tant qu'auteur", "youtube_id": "CcCw1ggftuQ"},
            {"title": "Nothin' on You", "artist": "B.o.B ft. Bruno Mars", "year": 2010, "info": "Sa première apparition majeure", "youtube_id": "8PTDv_szmL0"},
            {"title": "F**k You (Forget You)", "artist": "Cee Lo Green", "year": 2010, "info": "Hit mondial écrit par Bruno et Philip Lawrence", "youtube_id": "pc0mxOXbWIU"},
            {"title": "Lighters", "artist": "Bad Meets Evil ft. Bruno Mars", "year": 2011, "info": "Featuring Eminem et Royce da 5'9\"", "youtube_id": "Y8wifV5RYr8"},
            {"title": "Wavin' Flag", "artist": "K'naan", "year": 2010, "info": "Hymne de la Coupe du Monde FIFA 2010"},
            {"title": "All I Ask", "artist": "Adele", "year": 2015, "info": "Co-écrite pour l'album '25'", "youtube_id": "2-MBfn8XjIU"},
            {"title": "Billionaire", "artist": "Travie McCoy ft. Bruno Mars", "year": 2010, "info": "Co-écrit avec Travie McCoy"}
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
            {"title": "I Want It That Way", "artist": "Backstreet Boys", "year": 1999, "info": "Considérée comme l'une des meilleures chansons pop", "youtube_id": "4fndeDfaWCg"},
            {"title": "Shake It Off", "artist": "Taylor Swift", "year": 2014, "info": "Premier single de l'album '1989'", "youtube_id": "nfWlot6h_JM"},
            {"title": "Blank Space", "artist": "Taylor Swift", "year": 2014, "info": "Écrite avec Taylor et Shellback", "youtube_id": "e-ORhEE9VVg"},
            {"title": "Can't Feel My Face", "artist": "The Weeknd", "year": 2015, "info": "A relancé la carrière de Max Martin", "youtube_id": "KEI4qSrkPAs"},
            {"title": "Roar", "artist": "Katy Perry", "year": 2013, "info": "Hymne d'empowerment", "youtube_id": "CevxZvSJLk8"},
            {"title": "Since U Been Gone", "artist": "Kelly Clarkson", "year": 2004, "info": "A transformé Kelly en superstar", "youtube_id": "R7UrFYvl5TE"},
            {"title": "Teenage Dream", "artist": "Katy Perry", "year": 2010, "info": "L'album a égalé le record de MJ avec 5 singles #1", "youtube_id": "98WtmW-lfeE"},
            {"title": "Problem", "artist": "Ariana Grande", "year": 2014, "info": "Avec Big Sean et Iggy Azalea"},
            {"title": "It's My Life", "artist": "Bon Jovi", "year": 2000, "info": "A relancé Bon Jovi dans les années 2000", "youtube_id": "vx2u5uUu3DE"}
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
            "Il a failli vendre 'Halo' à plusieurs artistes avant que Beyoncé ne la prenne.",
            "Ryan souffre d'une perte auditive partielle à cause de l'exposition aux concerts.",
            "Il a écrit des chansons pour plus de 30 artistes différents."
        ],
        "songs_written_for_others": [
            {"title": "Halo", "artist": "Beyoncé", "year": 2008, "info": "Leona Lewis a sorti 'Bleeding Love' avec une mélodie similaire car Ryan avait proposé les deux", "youtube_id": "bnVUHWCynig"},
            {"title": "Bleeding Love", "artist": "Leona Lewis", "year": 2007, "info": "Premier single #1 UK de Leona", "youtube_id": "Vzo-EL_62fQ"},
            {"title": "Rumour Has It", "artist": "Adele", "year": 2011, "info": "Sur l'album historique '21'", "youtube_id": "eB03nPXlhXc"},
            {"title": "Already Gone", "artist": "Kelly Clarkson", "year": 2009, "info": "Kelly était furieuse car la mélodie ressemblait à 'Halo'"},
            {"title": "Battlefield", "artist": "Jordin Sparks", "year": 2009, "info": "Power ballad pop"},
            {"title": "Apologize", "artist": "Timbaland ft. OneRepublic", "year": 2007, "info": "Le remix a propulsé le groupe", "youtube_id": "ZSM3w1v-A_Y"}
        ]
    },
    "diane warren": {
        "anecdotes": [
            "Diane a été nominée 15 fois aux Oscars - un record pour un songwriter.",
            "Elle travaille seule et n'a presque jamais co-écrit une chanson.",
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

    # ===================== POP SUPERSTARS =====================
    "beyonce": {
        "anecdotes": [
            "Beyoncé a sorti son album éponyme en 2013 sans aucune promo - une première dans l'industrie.",
            "Elle a créé un alter ego appelé 'Sasha Fierce' pour surmonter sa timidité sur scène.",
            "Son père Mathew Knowles a hypothéqué sa maison pour financer Destiny's Child.",
            "Elle a chanté devant 118 millions de téléspectateurs au Super Bowl 2013."
        ],
        "songs_written_for_others": [
            {"title": "Independent Women Part I", "artist": "Destiny's Child", "year": 2000, "info": "Co-écrite par Beyoncé pour le film Charlie's Angels", "youtube_id": "0lPQZni7I18"},
            {"title": "Irreplaceable", "artist": "Beyoncé", "year": 2006, "info": "Co-écrite avec Ne-Yo et Stargate, #1 pendant 10 semaines", "youtube_id": "2EwViQxSJJQ"},
            {"title": "Telephone", "artist": "Lady Gaga ft. Beyoncé", "year": 2010, "info": "Beyoncé a co-écrit cette chanson avec Gaga", "youtube_id": "GQ95z6ywcBY"}
        ]
    },
    "drake": {
        "anecdotes": [
            "Drake a commencé comme acteur dans la série canadienne 'Degrassi' à 15 ans.",
            "Il détient le record du plus grand nombre de chansons dans le Billboard Hot 100 (300+).",
            "Son vrai nom est Aubrey Drake Graham - il est à moitié canadien, à moitié américain.",
            "Drake ne boit pas d'alcool et ne fume pas malgré ses paroles."
        ],
        "songs_written_for_others": [
            {"title": "Man Down", "artist": "Rihanna", "year": 2010, "info": "Drake a co-écrit ce titre pour l'album 'Loud'"},
            {"title": "Throw It in the Bag", "artist": "Fabolous ft. The-Dream", "year": 2009, "info": "Un des premiers crédits de Drake comme auteur"},
            {"title": "Congratulations", "artist": "Post Malone", "year": 2017, "info": "Drake est crédité comme co-auteur", "youtube_id": "SC4xMk98Pdc"},
            {"title": "Work", "artist": "Rihanna ft. Drake", "year": 2016, "info": "La chimie entre les deux a créé un hit mondial", "youtube_id": "HL1UzIK-flA"}
        ]
    },
    "adele": {
        "anecdotes": [
            "Adele a écrit '21' après une rupture dévastatrice - l'album s'est vendu à 31 millions d'exemplaires.",
            "Elle souffre de trac sévère et a vomi en coulisse avant plusieurs concerts.",
            "Le titre de ses albums correspond à son âge au moment de l'écriture (19, 21, 25, 30).",
            "Elle a refusé un contrat de 50 millions $ avec L'Oréal pour rester authentique."
        ],
        "songs_written_for_others": [
            {"title": "Turning Tables", "artist": "Adele", "year": 2011, "info": "Co-écrite avec Ryan Tedder, inspirée par sa thérapie", "youtube_id": "F5gUTl6Gy6g"},
            {"title": "Remedy", "artist": "Adele", "year": 2015, "info": "Écrite pour son fils Angelo"},
            {"title": "Skyfall", "artist": "Adele", "year": 2012, "info": "Écrite en 10 minutes avec Paul Epworth pour James Bond", "youtube_id": "DeumyOzKqgI"}
        ]
    },
    "the weeknd": {
        "anecdotes": [
            "The Weeknd était sans-abri à 17 ans après avoir quitté le lycée pour poursuivre la musique.",
            "Son vrai nom est Abel Tesfaye - il a enlevé le 'e' de 'Weekend' pour éviter un conflit de marque.",
            "Il a refusé de soumettre 'After Hours' aux Grammys pour protester contre le manque de transparence.",
            "'Blinding Lights' est la chanson la plus streamée de l'histoire de Spotify."
        ],
        "songs_written_for_others": [
            {"title": "Gifted", "artist": "French Montana ft. The Weeknd", "year": 2012, "info": "Un de ses premiers featurings"},
            {"title": "Or Nah", "artist": "Ty Dolla $ign ft. The Weeknd", "year": 2014, "info": "Le remix avec Abel est devenu plus populaire que l'original", "youtube_id": "2JhAR8Xb1Bo"},
            {"title": "Pray for Me", "artist": "The Weeknd & Kendrick Lamar", "year": 2018, "info": "Pour la bande-son de Black Panther", "youtube_id": "XR8LFNUr3vw"},
            {"title": "Might Not", "artist": "Belly ft. The Weeknd", "year": 2015, "info": "Collaboration avec son ami de longue date XO"}
        ]
    },
    "lady gaga": {
        "anecdotes": [
            "Lady Gaga a été renvoyée de son contrat avec Def Jam après seulement 3 mois.",
            "Son nom vient de la chanson 'Radio Ga Ga' de Queen.",
            "Elle souffre de fibromyalgie, une maladie chronique causant des douleurs.",
            "Elle a étudié à la Tisch School of the Arts de NYU avant de partir pour la musique."
        ],
        "songs_written_for_others": [
            {"title": "Telephone", "artist": "Lady Gaga ft. Beyoncé", "year": 2010, "info": "Initialement écrite pour Britney Spears qui l'a refusée", "youtube_id": "GQ95z6ywcBY"},
            {"title": "Quicksand", "artist": "Britney Spears", "year": 2007, "info": "Gaga a écrit des chansons pour Britney avant de devenir célèbre"},
            {"title": "Nothing Else I Can Say", "artist": "Pussycat Dolls", "year": 2008, "info": "Écrite quand Gaga était encore auteure anonyme"},
            {"title": "Hypnotico", "artist": "Jennifer Lopez", "year": 2011, "info": "Gaga a co-écrit cette chanson pour J.Lo"},
            {"title": "Shallow", "artist": "Lady Gaga & Bradley Cooper", "year": 2018, "info": "Oscar de la meilleure chanson originale - 'A Star Is Born'", "youtube_id": "bo_efYhYU2A"}
        ]
    },
    "ariana grande": {
        "anecdotes": [
            "Ariana a commencé sa carrière comme actrice dans la comédie musicale '13' à Broadway à 15 ans.",
            "Elle possède une tessiture vocale de 4 octaves, comparable à Mariah Carey.",
            "Sa queue de cheval signature est due aux dommages causés à ses cheveux par les colorations pour 'Victorious'.",
            "Elle a nommé son album 'thank u, next' d'après l'expression qu'elle utilisait en thérapie."
        ],
        "songs_written_for_others": [
            {"title": "Nobody Does It Better", "artist": "Nicki Minaj", "year": 2018, "info": "Ariana a co-écrit cette chanson pour l'album 'Queen'"},
            {"title": "Stuck with U", "artist": "Ariana Grande & Justin Bieber", "year": 2020, "info": "Écrite pendant le confinement COVID, revenus donnés à la charité", "youtube_id": "pE49WK-oNjU"},
            {"title": "Rain on Me", "artist": "Lady Gaga ft. Ariana Grande", "year": 2020, "info": "Co-écrite et co-produite, #1 mondial instantané", "youtube_id": "AoAm4om0wTs"}
        ]
    },
    "billie eilish": {
        "anecdotes": [
            "Billie a enregistré 'When We All Fall Asleep, Where Do We Go?' dans la chambre de son frère Finneas.",
            "Elle a le syndrome de Tourette et souffre de synesthésie.",
            "À 18 ans, elle est devenue la plus jeune artiste à remporter les 4 Grammy principaux en une soirée.",
            "Elle a écrit 'Bad Guy' en pensant que c'était une blague et ne voulait pas la sortir."
        ],
        "songs_written_for_others": [
            {"title": "lovely", "artist": "Billie Eilish & Khalid", "year": 2018, "info": "Utilisée dans la série '13 Reasons Why'", "youtube_id": "V1Pl8CzNzCw"},
            {"title": "No Time to Die", "artist": "Billie Eilish", "year": 2020, "info": "Plus jeune artiste à écrire un thème de James Bond", "youtube_id": "BboMpayJomw"}
        ]
    },
    "taylor swift": {
        "anecdotes": [
            "Taylor a déménagé au Tennessee à 14 ans pour poursuivre sa carrière country.",
            "Elle réenregistre tous ses anciens albums pour en récupérer les droits ('Taylor's Version').",
            "C'est la seule artiste à avoir 5 albums vendus à plus d'1 million en première semaine.",
            "Elle cache des indices (Easter eggs) dans tout ce qu'elle fait pour ses fans."
        ],
        "songs_written_for_others": [
            {"title": "This Is What You Came For", "artist": "Calvin Harris ft. Rihanna", "year": 2016, "info": "Écrite sous le pseudonyme 'Nils Sjöberg' quand elle sortait avec Calvin", "youtube_id": "kOkQ4T5WO9E"},
            {"title": "Better Man", "artist": "Little Big Town", "year": 2016, "info": "Grammy de la meilleure chanson country", "youtube_id": "Z3KHEPQDGY"},
            {"title": "Babe", "artist": "Sugarland", "year": 2018, "info": "Taylor fait les choeurs sur la chanson"},
            {"title": "You'll Always Find Your Way Back Home", "artist": "Hannah Montana / Miley Cyrus", "year": 2009, "info": "Écrite pour le film 'Hannah Montana: The Movie'"}
        ]
    },
    "rihanna": {
        "anecdotes": [
            "Rihanna a été découverte à 16 ans par Evan Rogers lors d'un voyage à la Barbade.",
            "Elle a sorti 8 albums en 7 ans entre 2005 et 2012 - un rythme incroyable.",
            "Son vrai nom est Robyn Rihanna Fenty.",
            "Elle est devenue la première milliardaire de la musique grâce à Fenty Beauty, pas grâce à la musique."
        ],
        "songs_written_for_others": [
            {"title": "Bitch Better Have My Money", "artist": "Rihanna", "year": 2015, "info": "Co-écrite par Rihanna, un de ses rares crédits d'écriture"},
            {"title": "FourFiveSeconds", "artist": "Rihanna, Kanye West & Paul McCartney", "year": 2015, "info": "Collaboration historique entre trois géants", "youtube_id": "kt0g4dWxEBo"}
        ]
    },
    "justin bieber": {
        "anecdotes": [
            "Justin a été découvert par Scooter Braun sur YouTube à 13 ans.",
            "Il a battu le record de concerts sold-out au Madison Square Garden à 18 ans.",
            "Il souffre de la maladie de Lyme et du syndrome de Ramsay Hunt.",
            "Il s'est marié avec Hailey Baldwin en 2018."
        ],
        "songs_written_for_others": [
            {"title": "Bigger", "artist": "Justin Bieber", "year": 2010, "info": "L'une de ses premières co-écritures pour son propre album"},
            {"title": "Next to You", "artist": "Chris Brown ft. Justin Bieber", "year": 2011, "info": "Co-écrite avec Chris Brown"}
        ]
    },

    # ===================== PRODUCERS & DJs =====================
    "daft punk": {
        "anecdotes": [
            "Thomas Bangalter et Guy-Manuel de Homem-Christo se sont rencontrés au lycée à Paris.",
            "Ils portent des casques de robots depuis 1999 pour rester anonymes.",
            "Le nom 'Daft Punk' vient d'une critique négative de leur ancien groupe Darlin'.",
            "Ils ont mis 5 ans à créer l'album 'Random Access Memories'."
        ],
        "songs_written_for_others": [
            {"title": "Starboy", "artist": "The Weeknd", "year": 2016, "info": "Collaboration surprise avec le chanteur canadien", "youtube_id": "34Na4j8AVgA"},
            {"title": "I Feel It Coming", "artist": "The Weeknd", "year": 2016, "info": "Deuxième collaboration sur l'album 'Starboy'", "youtube_id": "qFLhGq0060w"},
            {"title": "TRON: Legacy OST", "artist": "Daft Punk", "year": 2010, "info": "Bande originale complète du film Disney"},
            {"title": "Lose Yourself to Dance", "artist": "Daft Punk ft. Pharrell", "year": 2013, "info": "Tout l'album RAM est une collaboration avec des musiciens live"}
        ]
    },
    "david guetta": {
        "anecdotes": [
            "David Guetta a commencé comme DJ dans des petites boîtes parisiennes dans les années 80.",
            "Il a été nommé DJ #1 mondial par DJ Mag à deux reprises.",
            "Son album 'One Love' a été le premier album dance à se vendre à 3 millions d'exemplaires.",
            "Il a un alias secret appelé 'Jack Back' pour sortir de la musique underground."
        ],
        "songs_written_for_others": [
            {"title": "Titanium", "artist": "David Guetta ft. Sia", "year": 2011, "info": "A défini le son de la pop électronique des années 2010", "youtube_id": "JRfuAukYTKg"},
            {"title": "When Love Takes Over", "artist": "David Guetta ft. Kelly Rowland", "year": 2009, "info": "La chanson qui a lancé Guetta aux USA", "youtube_id": "PlKJvJYnvGo"},
            {"title": "Where Them Girls At", "artist": "David Guetta ft. Flo Rida & Nicki Minaj", "year": 2011, "info": "Hit de l'été dansant"},
            {"title": "Turn Me On", "artist": "David Guetta ft. Nicki Minaj", "year": 2011, "info": "Produit pour l'album 'Nothing but the Beat'", "youtube_id": "hHDTnLKqOTM"},
            {"title": "Hey Mama", "artist": "David Guetta ft. Nicki Minaj & Bebe Rexha", "year": 2015, "info": "Tube de l'été", "youtube_id": "uO59tfQ2TbA"},
            {"title": "Play Hard", "artist": "David Guetta ft. Ne-Yo & Akon", "year": 2012, "info": "Le trio parfait de la dance-pop", "youtube_id": "5dbEhBKGOtY"}
        ]
    },
    "calvin harris": {
        "anecdotes": [
            "Calvin Harris a écrit et produit son premier album seul dans sa chambre en Écosse.",
            "Son vrai nom est Adam Richard Wiles.",
            "Il est le premier DJ à atteindre 1 milliard de streams Spotify.",
            "Il a une relation secrète avec la production country sous un pseudonyme."
        ],
        "songs_written_for_others": [
            {"title": "We Found Love", "artist": "Rihanna ft. Calvin Harris", "year": 2011, "info": "Le plus gros hit de Calvin, #1 dans 25 pays", "youtube_id": "tg00YEETFzg"},
            {"title": "This Is What You Came For", "artist": "Calvin Harris ft. Rihanna", "year": 2016, "info": "Les paroles ont été écrites par Taylor Swift sous pseudonyme", "youtube_id": "kOkQ4T5WO9E"},
            {"title": "How Deep Is Your Love", "artist": "Calvin Harris & Disciples", "year": 2015, "info": "Un des hymnes house de la décennie", "youtube_id": "EgqUJOudrcM"},
            {"title": "Summer", "artist": "Calvin Harris", "year": 2014, "info": "Écrite et produite en une seule session", "youtube_id": "ebXbLfLACGM"},
            {"title": "Slide", "artist": "Calvin Harris ft. Frank Ocean & Migos", "year": 2017, "info": "Collaboration inattendue devenue un classique", "youtube_id": "8Ee4QjCEHHc"},
            {"title": "One Kiss", "artist": "Calvin Harris & Dua Lipa", "year": 2018, "info": "Chanson de l'été 2018 en Europe", "youtube_id": "DkeiKbqa02g"}
        ]
    },
    "timbaland": {
        "anecdotes": [
            "Timbaland a révolutionné la production musicale avec ses beats innovants dans les années 90-2000.",
            "Son vrai nom est Timothy Zachery Mosley.",
            "Il a produit plus de 85 millions de singles vendus.",
            "Il a grandi avec Pharrell Williams et Missy Elliott en Virginie."
        ],
        "songs_written_for_others": [
            {"title": "Cry Me a River", "artist": "Justin Timberlake", "year": 2002, "info": "Écrite sur la rupture de JT avec Britney Spears", "youtube_id": "DksSPZTZES0"},
            {"title": "SexyBack", "artist": "Justin Timberlake", "year": 2006, "info": "A redéfini le son R&B-pop", "youtube_id": "3gOHvDP_vCs"},
            {"title": "Promiscuous", "artist": "Nelly Furtado ft. Timbaland", "year": 2006, "info": "A transformé la carrière de Nelly Furtado", "youtube_id": "0J3vgcE5i2o"},
            {"title": "Apologize", "artist": "Timbaland ft. OneRepublic", "year": 2007, "info": "Son remix a propulsé OneRepublic au sommet", "youtube_id": "ZSM3w1v-A_Y"},
            {"title": "The Way I Are", "artist": "Timbaland ft. Keri Hilson", "year": 2007, "info": "Hit de l'été 2007", "youtube_id": "U5rLz5AZBIA"},
            {"title": "Give It to Me", "artist": "Timbaland ft. Nelly Furtado & Justin Timberlake", "year": 2007, "info": "Trio de superstars réunis", "youtube_id": "GhMvKv4GX5U"},
            {"title": "Are You That Somebody?", "artist": "Aaliyah", "year": 1998, "info": "Collaboration iconique avec Aaliyah", "youtube_id": "Nr4Kp-BNQK0"},
            {"title": "Try Again", "artist": "Aaliyah", "year": 2000, "info": "Premier single à atteindre le #1 uniquement grâce aux diffusions radio", "youtube_id": "xcIvIladNnQ"}
        ]
    },
    "dr. dre": {
        "anecdotes": [
            "Dr. Dre a découvert Eminem, 50 Cent, Snoop Dogg et Kendrick Lamar.",
            "Son album 'The Chronic' a inventé le genre G-funk.",
            "Il a vendu Beats Electronics à Apple pour 3 milliards de dollars en 2014.",
            "Il est connu pour être perfectionniste et peut passer des mois sur un seul beat."
        ],
        "songs_written_for_others": [
            {"title": "In Da Club", "artist": "50 Cent", "year": 2003, "info": "Le beat le plus iconique du hip-hop des années 2000", "youtube_id": "5qm8PH4xAss"},
            {"title": "Lose Yourself", "artist": "Eminem", "year": 2002, "info": "Oscar de la meilleure chanson - film '8 Mile'", "youtube_id": "xFYQQPAOz7Y"},
            {"title": "Still D.R.E.", "artist": "Dr. Dre ft. Snoop Dogg", "year": 1999, "info": "Le piano iconique a été joué par Scott Storch", "youtube_id": "_CL6n0FJZpk"},
            {"title": "Nuthin' but a 'G' Thang", "artist": "Dr. Dre ft. Snoop Dogg", "year": 1992, "info": "L'hymne de la côte ouest", "youtube_id": "6xjRdBjmePQ"},
            {"title": "Not Afraid", "artist": "Eminem", "year": 2010, "info": "Co-produit avec Boi-1da", "youtube_id": "j5-yKhDd64s"},
            {"title": "Compton", "artist": "Kendrick Lamar", "year": 2012, "info": "Beat de Dre pour le classique 'good kid, m.A.A.d city'", "youtube_id": "10yrPDf92hY"}
        ]
    },
    "jack antonoff": {
        "anecdotes": [
            "Jack est le leader du groupe Bleachers et l'ancien guitariste de fun.",
            "Il a remporté le Grammy du producteur de l'année 4 fois consécutives (2022-2025).",
            "Il travaille presque exclusivement avec des artistes féminines et est leur collaborateur de confiance.",
            "Sa soeur jumelle est décédée d'un cancer du cerveau quand ils avaient 18 ans."
        ],
        "songs_written_for_others": [
            {"title": "Style", "artist": "Taylor Swift", "year": 2014, "info": "Leur première collaboration sur '1989'", "youtube_id": "l-nMkTSjNog"},
            {"title": "Out of the Woods", "artist": "Taylor Swift", "year": 2014, "info": "Inspirée par la relation de Taylor avec Harry Styles"},
            {"title": "Green Light", "artist": "Lorde", "year": 2017, "info": "Le retour triomphal de Lorde", "youtube_id": "dMK_npDG12Q"},
            {"title": "Liability", "artist": "Lorde", "year": 2017, "info": "Ballade piano minimaliste et déchirante"},
            {"title": "Don't Delete the Kisses", "artist": "Wolf Alice", "year": 2017, "info": "Jack a produit cette pépite indie"},
            {"title": "Rollercoaster", "artist": "Bleachers ft. Lana Del Rey", "year": 2021, "info": "Collaboration avec Lana"},
            {"title": "Anti-Hero", "artist": "Taylor Swift", "year": 2022, "info": "Plus gros hit de Midnights, #1 pendant 8 semaines", "youtube_id": "b1kbLwvqugk"},
            {"title": "Cruel Summer", "artist": "Taylor Swift", "year": 2019, "info": "Devenu un hit tardif en 2023, 4 ans après sa sortie", "youtube_id": "ic8j13piAhQ"},
            {"title": "Supercut", "artist": "Lorde", "year": 2017, "info": "Célèbre pour son bridge épique"}
        ]
    },
    "finneas": {
        "anecdotes": [
            "Finneas a produit l'intégralité du premier album de Billie Eilish dans sa petite chambre.",
            "Il est le frère aîné de Billie Eilish de 4 ans.",
            "Il a remporté 8 Grammy Awards avant ses 25 ans.",
            "Il a aussi joué dans la série 'Glee' comme acteur avant de se consacrer à la musique."
        ],
        "songs_written_for_others": [
            {"title": "Bad Guy", "artist": "Billie Eilish", "year": 2019, "info": "Produit et co-écrit dans sa chambre, devenu #1 mondial", "youtube_id": "DyDfgMOUjCI"},
            {"title": "Ocean Eyes", "artist": "Billie Eilish", "year": 2015, "info": "La chanson qui a tout lancé, uploadée sur SoundCloud", "youtube_id": "viimfQi_pUw"},
            {"title": "Lovely", "artist": "Billie Eilish & Khalid", "year": 2018, "info": "Utilisée dans '13 Reasons Why'", "youtube_id": "V1Pl8CzNzCw"},
            {"title": "No Time to Die", "artist": "Billie Eilish", "year": 2020, "info": "Thème de James Bond composé par Finneas", "youtube_id": "BboMpayJomw"},
            {"title": "Used to This", "artist": "Camila Cabello", "year": 2020, "info": "Finneas a co-produit pour Camila"},
            {"title": "Let's Fall in Love for the Night", "artist": "Finneas", "year": 2018, "info": "Son propre single solo", "youtube_id": "ZFjjBHOVOAM"},
            {"title": "What Was I Made For?", "artist": "Billie Eilish", "year": 2023, "info": "Oscar pour le film Barbie", "youtube_id": "JlqVKQd3YhQ"}
        ]
    },
    "benny blanco": {
        "anecdotes": [
            "Benny Blanco a produit 30 singles dans le top 10 du Billboard Hot 100.",
            "Son vrai nom est Benjamin Joseph Levin.",
            "Il a commencé à produire à 16 ans après avoir envoyé des beats à Dr. Luke.",
            "Benny est aussi connu pour ses vidéos de cuisine sur les réseaux sociaux."
        ],
        "songs_written_for_others": [
            {"title": "Tik Tok", "artist": "Kesha", "year": 2009, "info": "Premier single de Kesha, #1 pendant 9 semaines", "youtube_id": "iP6XpLQM2Cs"},
            {"title": "Teenage Dream", "artist": "Katy Perry", "year": 2010, "info": "Co-produit avec Dr. Luke et Max Martin", "youtube_id": "98WtmW-lfeE"},
            {"title": "Moves Like Jagger", "artist": "Maroon 5 ft. Christina Aguilera", "year": 2011, "info": "A relancé Maroon 5", "youtube_id": "iEPTlhBmwRg"},
            {"title": "Lonely", "artist": "Justin Bieber & Benny Blanco", "year": 2020, "info": "Ballade émouvante sur la solitude de la célébrité", "youtube_id": "xQOO2xGQ1Pc"},
            {"title": "Eastside", "artist": "Benny Blanco, Halsey & Khalid", "year": 2018, "info": "Son premier single en tant qu'artiste principal", "youtube_id": "56WBK4ZK_cw"},
            {"title": "Dynamite", "artist": "Taio Cruz", "year": 2010, "info": "Hit dance-pop international", "youtube_id": "Vysgv7qVYTo"},
            {"title": "Beautiful Girls", "artist": "Sean Kingston", "year": 2007, "info": "Une de ses premières productions majeures", "youtube_id": "MrTz5xjmso4"}
        ]
    },
    "diplo": {
        "anecdotes": [
            "Diplo est le co-fondateur de Major Lazer et la moitié de Jack Ü avec Skrillex.",
            "Son vrai nom est Thomas Wesley Pentz.",
            "Il a été professeur d'école avant de devenir DJ.",
            "Il a aidé à populariser le dancehall et le baile funk à l'international."
        ],
        "songs_written_for_others": [
            {"title": "Lean On", "artist": "Major Lazer & DJ Snake ft. MØ", "year": 2015, "info": "La chanson la plus streamée au monde en 2015", "youtube_id": "YqeW9_5kURI"},
            {"title": "Where Are Ü Now", "artist": "Jack Ü ft. Justin Bieber", "year": 2015, "info": "Grammy de la meilleure production dance", "youtube_id": "nntGTK2Fhb0"},
            {"title": "Cold Water", "artist": "Major Lazer ft. Justin Bieber & MØ", "year": 2016, "info": "Co-écrite avec Ed Sheeran", "youtube_id": "a59gmGkq_pw"},
            {"title": "Paper Planes", "artist": "M.I.A.", "year": 2007, "info": "Diplo a produit ce hit culte", "youtube_id": "ewRjZoRtu0Y"},
            {"title": "Electricity", "artist": "Silk City & Dua Lipa", "year": 2018, "info": "Grammy de la meilleure production dance (avec Mark Ronson)", "youtube_id": "AD1VnPlGaio"}
        ]
    },
    "skrillex": {
        "anecdotes": [
            "Skrillex était le chanteur du groupe post-hardcore 'From First to Last' avant de devenir DJ.",
            "Son vrai nom est Sonny John Moore.",
            "Il a remporté 8 Grammy Awards, dont 3 en une seule soirée.",
            "Il a produit pour Beyoncé, Justin Bieber et même les Rolling Stones."
        ],
        "songs_written_for_others": [
            {"title": "Where Are Ü Now", "artist": "Jack Ü ft. Justin Bieber", "year": 2015, "info": "A relancé la carrière de Bieber", "youtube_id": "nntGTK2Fhb0"},
            {"title": "Sorry", "artist": "Justin Bieber", "year": 2015, "info": "Co-produit par Skrillex et Blood", "youtube_id": "fRh_vgS2dFE"},
            {"title": "Humble", "artist": "Kendrick Lamar", "year": 2017, "info": "Skrillex était impliqué dans les sessions de production"},
            {"title": "Don't Go", "artist": "Skrillex, Justin Bieber & Don Toliver", "year": 2023, "info": "Collaboration surprise"}
        ]
    },

    # ===================== HIP-HOP LEGENDS =====================
    "kanye west": {
        "anecdotes": [
            "Kanye a survécu à un accident de voiture en 2002 et a enregistré 'Through the Wire' avec la mâchoire câblée.",
            "Il a été refusé par plusieurs labels car ils ne voyaient pas un producteur devenir rappeur.",
            "'My Beautiful Dark Twisted Fantasy' est souvent classé parmi les meilleurs albums de tous les temps.",
            "Il a changé son nom légal en 'Ye' en 2021."
        ],
        "songs_written_for_others": [
            {"title": "You Don't Know My Name", "artist": "Alicia Keys", "year": 2003, "info": "Premier hit produit par Kanye pour une autre artiste", "youtube_id": "ByS-JzuJNtc"},
            {"title": "Lucifer", "artist": "Jay-Z", "year": 2003, "info": "Sample soul signature de Kanye sur 'The Black Album'"},
            {"title": "Encore", "artist": "Jay-Z", "year": 2003, "info": "Produit pour 'The Black Album'"},
            {"title": "Stand Up", "artist": "Ludacris", "year": 2003, "info": "Production emblématique"},
            {"title": "Talk About Our Love", "artist": "Brandy", "year": 2004, "info": "Single à succès du R&B"},
            {"title": "Run This Town", "artist": "Jay-Z ft. Rihanna & Kanye", "year": 2009, "info": "Collaboration épique de trois superstars", "youtube_id": "tPGc9Fg80jI"},
            {"title": "FourFiveSeconds", "artist": "Rihanna, Kanye & Paul McCartney", "year": 2015, "info": "Trio improbable mais génial", "youtube_id": "kt0g4dWxEBo"}
        ]
    },
    "jay-z": {
        "anecdotes": [
            "Jay-Z est devenu le premier rappeur milliardaire en 2019.",
            "Son vrai nom est Shawn Corey Carter - 'Jay-Z' vient de son surnom 'Jazzy'.",
            "Il a écrit la plupart de 'Reasonable Doubt' sans stylo ni papier, uniquement de mémoire.",
            "Il est propriétaire de Roc Nation, du champagne Armand de Brignac et du cognac D'Ussé."
        ],
        "songs_written_for_others": [
            {"title": "Crazy in Love", "artist": "Beyoncé ft. Jay-Z", "year": 2003, "info": "Le début de la relation musicale (et personnelle) la plus puissante", "youtube_id": "ViwtNLUqkMY"},
            {"title": "Umbrella", "artist": "Rihanna ft. Jay-Z", "year": 2007, "info": "Son couplet d'intro est devenu iconique", "youtube_id": "CvBfHwUxHIk"},
            {"title": "Déjà Vu", "artist": "Beyoncé ft. Jay-Z", "year": 2006, "info": "Suite spirituelle de 'Crazy in Love'"},
            {"title": "Monster", "artist": "Kanye West ft. Jay-Z & Nicki Minaj", "year": 2010, "info": "Mais c'est le couplet de Nicki qui a volé la vedette", "youtube_id": "Ona42jz8w0k"}
        ]
    },
    "eminem": {
        "anecdotes": [
            "Eminem a été élu 'Roi du Hip-Hop' par Rolling Stone en 2011.",
            "Il écrit toutes ses propres paroles et est connu pour remplir des pages entières de rimes.",
            "Il a survécu à une overdose de méthadone en 2007 qui a failli le tuer.",
            "'Lose Yourself' est la première chanson de rap à remporter un Oscar."
        ],
        "songs_written_for_others": [
            {"title": "Lose Yourself", "artist": "Eminem", "year": 2002, "info": "Écrite à la main sur un plateau de tournage de '8 Mile'", "youtube_id": "xFYQQPAOz7Y"},
            {"title": "Love the Way You Lie", "artist": "Eminem ft. Rihanna", "year": 2010, "info": "Co-écrite avec Skylar Grey qui avait la mélodie originale", "youtube_id": "uelHwf8o7_U"},
            {"title": "Airplanes Part II", "artist": "B.o.B ft. Eminem", "year": 2010, "info": "Son couplet est considéré comme un des meilleurs jamais rappés"},
            {"title": "No Love", "artist": "Eminem ft. Lil Wayne", "year": 2010, "info": "Deux légendes du rap ensemble"}
        ]
    },
    "kendrick lamar": {
        "anecdotes": [
            "Kendrick est le premier artiste non-classique/jazz à remporter un Prix Pulitzer pour la musique (DAMN., 2018).",
            "Il a grandi à Compton et a vu Tupac tourner un clip dans son quartier quand il avait 8 ans.",
            "Il est connu pour écrire ses paroles sur son téléphone, partout et tout le temps.",
            "Son album 'To Pimp a Butterfly' mélange jazz, funk et rap politique."
        ],
        "songs_written_for_others": [
            {"title": "Pray for Me", "artist": "The Weeknd & Kendrick Lamar", "year": 2018, "info": "Pour le film Black Panther", "youtube_id": "XR8LFNUr3vw"},
            {"title": "Sidewalks", "artist": "The Weeknd ft. Kendrick Lamar", "year": 2016, "info": "Sur l'album 'Starboy'"},
            {"title": "Bad Blood Remix", "artist": "Taylor Swift ft. Kendrick Lamar", "year": 2015, "info": "Collaboration inattendue entre pop et hip-hop", "youtube_id": "QcIy9NiNbmo"},
            {"title": "Freedom", "artist": "Beyoncé ft. Kendrick Lamar", "year": 2016, "info": "Hymne puissant sur l'album 'Lemonade'", "youtube_id": "VL8H1YcmhXM"}
        ]
    },
    "nicki minaj": {
        "anecdotes": [
            "Nicki Minaj est originaire de Trinidad-et-Tobago et a grandi dans le Queens à New York.",
            "Elle a créé plusieurs alter egos : Roman Zolanski, Harajuku Barbie et Martha Zolanski.",
            "Elle est la rappeuse la plus vendeuse de tous les temps avec plus de 100 millions de ventes.",
            "Son vrai nom est Onika Tanya Maraj."
        ],
        "songs_written_for_others": [
            {"title": "Monster", "artist": "Kanye West ft. Jay-Z & Nicki Minaj", "year": 2010, "info": "Son couplet a changé l'histoire du rap féminin", "youtube_id": "Ona42jz8w0k"},
            {"title": "Bottoms Up", "artist": "Trey Songz ft. Nicki Minaj", "year": 2010, "info": "Son featuring a propulsé la chanson au top"},
            {"title": "Bang Bang", "artist": "Jessie J, Ariana Grande & Nicki Minaj", "year": 2014, "info": "Trio de superstars", "youtube_id": "0HDdjwpPM3Y"},
            {"title": "Side to Side", "artist": "Ariana Grande ft. Nicki Minaj", "year": 2016, "info": "Leur chimie musicale est légendaire", "youtube_id": "SXiSVQZLje8"}
        ]
    },

    # ===================== ROCK & ALTERNATIVE =====================
    "coldplay": {
        "anecdotes": [
            "Chris Martin écrit souvent des chansons sur un vieux piano droit dans son studio.",
            "'Yellow' a été inspiré par les étoiles que Chris voyait en regardant le ciel au studio.",
            "Le nom 'Coldplay' a été donné par un ami qui ne le voulait plus pour son propre groupe.",
            "Ils sont le groupe le plus vendu du 21ème siècle au Royaume-Uni."
        ],
        "songs_written_for_others": [
            {"title": "Hymn for the Weekend", "artist": "Coldplay ft. Beyoncé", "year": 2015, "info": "Le clip a été filmé en Inde", "youtube_id": "YykjpeuMNEk"},
            {"title": "Something Just Like This", "artist": "Coldplay & The Chainsmokers", "year": 2017, "info": "Fusion rock-EDM massive", "youtube_id": "FM7MFYoylVs"},
            {"title": "Princess of China", "artist": "Coldplay ft. Rihanna", "year": 2011, "info": "Premier featuring féminin de Coldplay"},
            {"title": "My Universe", "artist": "Coldplay x BTS", "year": 2021, "info": "Collaboration historique K-pop/rock", "youtube_id": "3YqPKLZF_WU"}
        ]
    },
    "imagine dragons": {
        "anecdotes": [
            "Le nom 'Imagine Dragons' est un anagramme, mais les membres ne révèlent pas de quels mots.",
            "'Radioactive' est resté 87 semaines dans le Billboard Hot 100, un record à l'époque.",
            "Le chanteur Dan Reynolds souffre de spondylarthrite ankylosante.",
            "Ils sont originaires de Las Vegas et ont joué dans des casinos avant de percer."
        ],
        "songs_written_for_others": [
            {"title": "Warriors", "artist": "Imagine Dragons", "year": 2014, "info": "Écrite pour le championnat du monde de League of Legends", "youtube_id": "fmI_Ndrxy14"},
            {"title": "Believer", "artist": "Imagine Dragons", "year": 2017, "info": "Inspirée par la douleur physique de Dan Reynolds", "youtube_id": "7wtfhZwyrcc"},
            {"title": "Enemy", "artist": "Imagine Dragons & JID", "year": 2021, "info": "Pour la série animée 'Arcane' de Netflix", "youtube_id": "D9G1VOjN_84"}
        ]
    },

    # ===================== LATIN & INTERNATIONAL =====================
    "shakira": {
        "anecdotes": [
            "Shakira parle couramment l'espagnol, l'anglais, le français, le portugais, l'italien et l'arabe.",
            "Elle a fondé la Fundación Pies Descalzos pour l'éducation des enfants en Colombie.",
            "Son nom vient de l'arabe 'shakir' qui signifie 'reconnaissante'.",
            "'Waka Waka' est la chanson officielle de la Coupe du Monde FIFA 2010."
        ],
        "songs_written_for_others": [
            {"title": "Waka Waka", "artist": "Shakira", "year": 2010, "info": "Hymne officiel de la Coupe du Monde, basé sur un chant camerounais", "youtube_id": "pRpeEdMmmQ0"},
            {"title": "Hips Don't Lie", "artist": "Shakira ft. Wyclef Jean", "year": 2006, "info": "#1 dans 55 pays", "youtube_id": "DUT5rEU6pqM"},
            {"title": "Loca", "artist": "Shakira ft. El Cata", "year": 2010, "info": "Chanson écrite en espagnol et en anglais"},
            {"title": "Beautiful Liar", "artist": "Beyoncé & Shakira", "year": 2007, "info": "Duo de deux reines de la pop latine et R&B", "youtube_id": "QrOe2h9RtWI"},
            {"title": "BZRP Music Sessions #53", "artist": "Shakira & Bizarrap", "year": 2023, "info": "Chanson de rupture virale visant Piqué, 500M+ de vues en une semaine", "youtube_id": "CocEMWdc7Ck"}
        ]
    },
    "bad bunny": {
        "anecdotes": [
            "Bad Bunny a commencé en tant qu'emballeur dans un supermarché au Porto Rico.",
            "Il est l'artiste le plus streamé au monde sur Spotify en 2020, 2021 et 2022 - 3 ans de suite.",
            "Son vrai nom est Benito Antonio Martínez Ocasio.",
            "Il a joué dans le film 'Bullet Train' avec Brad Pitt et dans la série WWE."
        ],
        "songs_written_for_others": [
            {"title": "I Like It", "artist": "Cardi B ft. Bad Bunny & J Balvin", "year": 2018, "info": "Premier #1 latin depuis 'Macarena' en 1996", "youtube_id": "xTlNMmZKwpA"},
            {"title": "MIA", "artist": "Bad Bunny ft. Drake", "year": 2018, "info": "Drake chante en espagnol pour la première fois", "youtube_id": "OSUxrSMYqMk"},
            {"title": "Dákiti", "artist": "Bad Bunny & Jhay Cortez", "year": 2020, "info": "Hit mondial du reggaeton", "youtube_id": "TmKh7lAwnBI"},
            {"title": "YONAGUNI", "artist": "Bad Bunny", "year": 2021, "info": "Mélange reggaeton et J-pop inattendu", "youtube_id": "doLMt10ytHY"}
        ]
    },

    # ===================== R&B LEGENDS =====================
    "the neptunes": {
        "anecdotes": [
            "The Neptunes (Pharrell Williams et Chad Hugo) ont produit 43% des chansons à la radio US en 2003.",
            "Ils se sont rencontrés au camp de band en 7ème année.",
            "Le duo a produit pour plus de 100 artistes différents.",
            "Leur signature sonore inclut toujours un clap distinctif."
        ],
        "songs_written_for_others": [
            {"title": "Superthug", "artist": "Noreaga", "year": 1998, "info": "Leur premier hit en tant que producteurs"},
            {"title": "I Just Wanna Love U", "artist": "Jay-Z", "year": 2000, "info": "Collaboration avec Hov qui a tout changé", "youtube_id": "SOGlSYyRVZk"},
            {"title": "Pass the Courvoisier", "artist": "Busta Rhymes ft. P. Diddy & Pharrell", "year": 2002, "info": "Hit de fête par excellence"},
            {"title": "Hot in Herre", "artist": "Nelly", "year": 2002, "info": "Un des plus grands hits de l'été 2002", "youtube_id": "GeZZr_p6vB8"},
            {"title": "Excuse Me Miss", "artist": "Jay-Z", "year": 2003, "info": "Production smooth du 'Blueprint 2'"},
            {"title": "Rock Your Body", "artist": "Justin Timberlake", "year": 2003, "info": "Tube dansant de l'album 'Justified'", "youtube_id": "TSKizLRFbTo"},
            {"title": "Snoop Dogg", "artist": "Drop It Like It's Hot", "year": 2004, "info": "Beat minimaliste devenu légendaire"}
        ]
    },
    "ne-yo": {
        "anecdotes": [
            "Ne-Yo a écrit 'Let Me Love You' pour Mario avant de lancer sa propre carrière.",
            "Son nom de scène vient d'un ami qui pensait qu'il voyait la musique comme Neo voit la Matrice.",
            "Il a écrit des chansons pour plus de 30 artistes avant de sortir son premier album.",
            "Il est considéré comme l'un des meilleurs auteurs R&B de sa génération."
        ],
        "songs_written_for_others": [
            {"title": "Let Me Love You", "artist": "Mario", "year": 2004, "info": "#1 pendant 9 semaines - la chanson qui l'a rendu célèbre comme auteur", "youtube_id": "H64QG4UsrGI"},
            {"title": "Irreplaceable", "artist": "Beyoncé", "year": 2006, "info": "Écrite en seulement 10 minutes, #1 pendant 10 semaines", "youtube_id": "2EwViQxSJJQ"},
            {"title": "Take a Bow", "artist": "Rihanna", "year": 2008, "info": "Ne-Yo a écrit cette ballade pour Rihanna", "youtube_id": "J3UjJ4wKLkg"},
            {"title": "Fabulous", "artist": "Jaheim", "year": 2003, "info": "Un de ses premiers crédits d'écriture en R&B"},
            {"title": "Sexy Love", "artist": "Ne-Yo", "year": 2006, "info": "Sa propre chanson mais il l'avait d'abord proposée à d'autres"},
            {"title": "Miss Independent", "artist": "Ne-Yo", "year": 2008, "info": "A été proposée à Mary J. Blige avant qu'il la garde"},
            {"title": "Spotlight", "artist": "Jennifer Hudson", "year": 2008, "info": "Ne-Yo a écrit le premier single de l'album de J-Hud"}
        ]
    },

    # ===================== POP ICONS =====================
    "michael jackson": {
        "anecdotes": [
            "Michael Jackson a inventé le moonwalk lors des Motown 25 en 1983.",
            "'Thriller' est l'album le plus vendu de tous les temps avec 70 millions d'exemplaires.",
            "Il achetait régulièrement les droits de chansons et possédait le catalogue des Beatles.",
            "Son gant à une main était un hommage à son père qui portait un gant similaire."
        ],
        "songs_written_for_others": [
            {"title": "Thriller", "artist": "Michael Jackson", "year": 1982, "info": "L'album le plus vendu de tous les temps, clips révolutionnaires", "youtube_id": "sOnqjkJTMaA"},
            {"title": "We Are the World", "artist": "USA for Africa", "year": 1985, "info": "Co-écrite avec Lionel Richie pour la famine en Éthiopie", "youtube_id": "9AjkUyj0rVc"},
            {"title": "Billie Jean", "artist": "Michael Jackson", "year": 1982, "info": "Michael a écrit cette chanson entièrement seul", "youtube_id": "Zi_XLOBDo_Y"},
            {"title": "Don't Stop 'Til You Get Enough", "artist": "Michael Jackson", "year": 1979, "info": "Sa première chanson auto-écrite, début de son indépendance artistique", "youtube_id": "yURRmWtbTbo"}
        ]
    },
    "prince": {
        "anecdotes": [
            "Prince jouait de 27 instruments différents et a enregistré la quasi-totalité de ses albums seul.",
            "Il a changé son nom en un symbole imprononçable en 1993 pour protester contre son label.",
            "Il a écrit des tubes pour de nombreux artistes sous des pseudonymes.",
            "Son coffre-fort à Paisley Park contiendrait assez de musique inédite pour sortir un album par an pendant 100 ans."
        ],
        "songs_written_for_others": [
            {"title": "Nothing Compares 2 U", "artist": "Sinéad O'Connor", "year": 1990, "info": "Écrite par Prince pour The Family en 1985, devenue #1 mondial avec Sinéad", "youtube_id": "0-EF60neguk"},
            {"title": "Manic Monday", "artist": "The Bangles", "year": 1986, "info": "Écrite sous le pseudonyme 'Christopher' - Prince voulait rester anonyme", "youtube_id": "SsmVgoXDq2w"},
            {"title": "I Feel for You", "artist": "Chaka Khan", "year": 1984, "info": "Prince avait enregistré sa propre version en 1979, Chaka Khan en a fait un hymne funk", "youtube_id": "R_aUMIRpdHk"},
            {"title": "Stand Back", "artist": "Stevie Nicks", "year": 1983, "info": "Prince a joué les synthés anonymement sur cette chanson de Fleetwood Mac's Stevie Nicks"},
            {"title": "Sugar Walls", "artist": "Sheena Easton", "year": 1984, "info": "Écrite sous le pseudonyme 'Alexander Nevermind'"},
            {"title": "Love Song", "artist": "Madonna & Prince", "year": 1989, "info": "Collaboration rare entre les deux icônes de la pop"}
        ]
    },
    "madonna": {
        "anecdotes": [
            "Madonna est arrivée à New York avec 35$ en poche en 1977.",
            "Elle est la femme artiste la plus vendeuse de tous les temps avec 300+ millions de ventes.",
            "Elle a été intronisée au Rock and Roll Hall of Fame en 2008.",
            "Chaque ère de sa carrière réinvente complètement son image."
        ],
        "songs_written_for_others": [
            {"title": "Material Girl", "artist": "Madonna", "year": 1984, "info": "Écrite par Peter Brown et Robert Rans, pas par Madonna elle-même"},
            {"title": "Vogue", "artist": "Madonna", "year": 1990, "info": "Co-écrite avec Shep Pettibone, inspirée par la culture ballroom de New York", "youtube_id": "GuJQSAiODqI"},
            {"title": "Like a Prayer", "artist": "Madonna", "year": 1989, "info": "Co-écrite avec Patrick Leonard, le clip a provoqué un scandale mondial", "youtube_id": "79fzeNUqQbQ"},
            {"title": "Justify My Love", "artist": "Madonna", "year": 1990, "info": "Co-écrite avec Lenny Kravitz", "youtube_id": "Np_Y740aReI"}
        ]
    },
    "dua lipa": {
        "anecdotes": [
            "Dua Lipa a quitté le Kosovo pour Londres à 14 ans pour poursuivre sa carrière musicale.",
            "Son nom signifie 'amour' en albanais.",
            "'Future Nostalgia' a été inspiré par la disco des années 70-80 et enregistré pendant le confinement.",
            "Elle a lancé le podcast 'Dua Lipa: At Your Service' devenu très populaire."
        ],
        "songs_written_for_others": [
            {"title": "New Rules", "artist": "Dua Lipa", "year": 2017, "info": "Co-écrite avec Caroline Ailin et Emily Warren, son premier #1 UK", "youtube_id": "k2qgadSvNyU"},
            {"title": "One Kiss", "artist": "Calvin Harris & Dua Lipa", "year": 2018, "info": "Chanson de l'été 2018", "youtube_id": "DkeiKbqa02g"},
            {"title": "Levitating", "artist": "Dua Lipa", "year": 2020, "info": "L'une des chansons les plus streamées de 2021", "youtube_id": "TUVcZfQe-Kw"},
            {"title": "Electricity", "artist": "Silk City & Dua Lipa", "year": 2018, "info": "Grammy du meilleur enregistrement dance", "youtube_id": "AD1VnPlGaio"},
            {"title": "Sweetest Pie", "artist": "Megan Thee Stallion & Dua Lipa", "year": 2022, "info": "Collaboration pop-rap explosive"}
        ]
    },
    "harry styles": {
        "anecdotes": [
            "Harry Styles a auditionné seul à X Factor et a été regroupé dans One Direction par Simon Cowell.",
            "Il a refusé le rôle du Prince Eric dans 'La Petite Sirène' live action.",
            "'As It Was' a été #1 dans 35 pays et est son plus grand succès solo.",
            "Il est connu pour casser les normes de genre avec ses choix vestimentaires."
        ],
        "songs_written_for_others": [
            {"title": "Just a Little Bit of Your Heart", "artist": "Ariana Grande", "year": 2014, "info": "Harry a écrit cette ballade pour Ariana pendant l'ère One Direction", "youtube_id": "cjMBJFR0bIQ"},
            {"title": "Someday", "artist": "Michael Bublé", "year": 2018, "info": "Co-écrite avec Michael pour son album 'Love'"},
            {"title": "Perfect", "artist": "One Direction", "year": 2015, "info": "Co-écrite par Harry, Louis Tomlinson et Jesse Shatkin"}
        ]
    },
    "post malone": {
        "anecdotes": [
            "Post Malone a appris à jouer de la guitare grâce à Guitar Hero.",
            "Son vrai nom est Austin Richard Post et son nom de scène vient d'un générateur de noms de rappeurs.",
            "Il a plus de 70 tatouages sur le visage et le corps.",
            "Il est aussi un passionné de beer-pong et a participé à des tournois professionnels."
        ],
        "songs_written_for_others": [
            {"title": "Sunflower", "artist": "Post Malone & Swae Lee", "year": 2018, "info": "Pour le film 'Spider-Man: Into the Spider-Verse'", "youtube_id": "ApXoWvfEYVU"},
            {"title": "Rockstar", "artist": "Post Malone ft. 21 Savage", "year": 2017, "info": "#1 pendant 8 semaines", "youtube_id": "UceaB4D0jpo"},
            {"title": "Congratulations", "artist": "Post Malone ft. Quavo", "year": 2017, "info": "Sur sa réussite après avoir été sous-estimé", "youtube_id": "SC4xMk98Pdc"}
        ]
    },

    # ===================== FRENCH ARTISTS =====================
    "stromae": {
        "anecdotes": [
            "Stromae est un anagramme de 'maestro' en verlan.",
            "Son vrai nom est Paul Van Haver - il est belge d'origine rwandaise.",
            "Son père a été tué lors du génocide au Rwanda, ce qui influence profondément sa musique.",
            "Il a disparu pendant 5 ans entre 'Racine Carrée' et 'Multitude' à cause d'effets secondaires d'un médicament."
        ],
        "songs_written_for_others": [
            {"title": "Alors on danse", "artist": "Stromae", "year": 2009, "info": "#1 dans 19 pays européens", "youtube_id": "VHoT4N43jK8"},
            {"title": "Papaoutai", "artist": "Stromae", "year": 2013, "info": "Sur l'absence de son père, le clip est le plus vu de la musique francophone", "youtube_id": "oiKj0Z_Xnjc"},
            {"title": "Formidable", "artist": "Stromae", "year": 2013, "info": "Le clip a été filmé en caméra cachée dans les rues de Bruxelles", "youtube_id": "S_xB3eu6mGA"},
            {"title": "Défiler", "artist": "Stromae", "year": 2014, "info": "Écrite pour le défilé de mode de Jean-Paul Gaultier"},
            {"title": "L'enfer", "artist": "Stromae", "year": 2022, "info": "Chanson bouleversante sur la dépression, présentée en direct au JT de TF1", "youtube_id": "mUqeRLFpOMA"}
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
            {"title": "Starboy", "artist": "The Weeknd", "year": 2016, "info": "Collaboration surprise avec le chanteur canadien", "youtube_id": "34Na4j8AVgA"},
            {"title": "I Feel It Coming", "artist": "The Weeknd", "year": 2016, "info": "Deuxième collaboration sur l'album 'Starboy'", "youtube_id": "qFLhGq0060w"},
            {"title": "TRON: Legacy OST", "artist": "Daft Punk", "year": 2010, "info": "Bande originale complète du film Disney"},
            {"title": "Lose Yourself to Dance", "artist": "Daft Punk ft. Pharrell", "year": 2013, "info": "Tout l'album RAM est une collaboration avec des musiciens live"}
        ]
    },
    "angele": {
        "anecdotes": [
            "Angèle est la soeur du rappeur Roméo Elvis.",
            "Son premier album 'Brol' signifie 'bazar' en bruxellois.",
            "Elle a collaboré avec Dua Lipa sur 'Fever' en 2020.",
            "Angèle est une militante féministe et LGBT+."
        ],
        "songs_written_for_others": [
            {"title": "Tout oublier", "artist": "Angèle ft. Roméo Elvis", "year": 2018, "info": "Duo frère-soeur devenu hymne francophone", "youtube_id": "Fy1xQSiLx8U"},
            {"title": "Fever", "artist": "Dua Lipa ft. Angèle", "year": 2020, "info": "Premier single international d'Angèle", "youtube_id": "T2Jl-DlG0iI"},
            {"title": "Balance ton quoi", "artist": "Angèle", "year": 2019, "info": "Hymne féministe devenu viral", "youtube_id": "Hi7Rx3En7-k"}
        ]
    },

    # ===================== K-POP =====================
    "bts": {
        "anecdotes": [
            "BTS a commencé avec un petit label (Big Hit) et a été rejeté par toutes les grandes agences.",
            "Leur fanbase 'ARMY' est considérée comme la plus puissante communauté musicale au monde.",
            "'Dynamite' est la première chanson en anglais à atteindre le #1 du Hot 100 pour un groupe coréen.",
            "Ils ont parlé aux Nations Unies à trois reprises."
        ],
        "songs_written_for_others": [
            {"title": "Dynamite", "artist": "BTS", "year": 2020, "info": "Première chanson #1 aux USA pour un groupe K-pop", "youtube_id": "gdZLi9oWNZg"},
            {"title": "Butter", "artist": "BTS", "year": 2021, "info": "#1 pendant 10 semaines aux USA", "youtube_id": "WMweEpGlu_U"},
            {"title": "My Universe", "artist": "Coldplay x BTS", "year": 2021, "info": "Co-écrite entre les deux groupes", "youtube_id": "3YqPKLZF_WU"},
            {"title": "Left and Right", "artist": "Charlie Puth ft. Jungkook", "year": 2022, "info": "Collaboration du membre de BTS avec Charlie Puth", "youtube_id": "Aw3MxUmE_YQ"}
        ]
    },
    "blackpink": {
        "anecdotes": [
            "BLACKPINK est le girl group K-pop le plus suivi sur YouTube avec 90M+ abonnés.",
            "Elles ont été les premières artistes K-pop à jouer au Coachella (2019).",
            "Les 4 membres parlent couramment le coréen et l'anglais, et Lisa parle aussi le thaï.",
            "'DDU-DU DDU-DU' a été le clip K-pop le plus vu de l'histoire."
        ],
        "songs_written_for_others": [
            {"title": "DDU-DU DDU-DU", "artist": "BLACKPINK", "year": 2018, "info": "Un des clips K-pop les plus vus de l'histoire", "youtube_id": "IHNzOHi8sJs"},
            {"title": "How You Like That", "artist": "BLACKPINK", "year": 2020, "info": "A battu 5 records Guinness le jour de sa sortie", "youtube_id": "ioNng23DkIM"},
            {"title": "Ice Cream", "artist": "BLACKPINK ft. Selena Gomez", "year": 2020, "info": "Collaboration sucrée entre K-pop et pop", "youtube_id": "vRXZj0DzXIA"},
            {"title": "Kiss and Make Up", "artist": "Dua Lipa & BLACKPINK", "year": 2018, "info": "Fusion pop occidentale et K-pop", "youtube_id": "8dGFe4MlaZU"}
        ]
    },

    # ===================== REGGAETON & LATIN =====================
    "j balvin": {
        "anecdotes": [
            "J Balvin est considéré comme le 'Prince du Reggaeton'.",
            "Il est de Medellín, Colombie, une ville qui a vu naître le reggaeton colombien.",
            "Il a ouvertement parlé de sa lutte contre la dépression et l'anxiété.",
            "Son vrai nom est José Álvaro Osorio Balvín."
        ],
        "songs_written_for_others": [
            {"title": "Mi Gente", "artist": "J Balvin & Willy William", "year": 2017, "info": "Beyoncé a fait un remix surprise qui a tout cassé", "youtube_id": "wnJ6LuUFpMo"},
            {"title": "I Like It", "artist": "Cardi B ft. Bad Bunny & J Balvin", "year": 2018, "info": "Le trio Latin Trap qui a dominé l'été", "youtube_id": "xTlNMmZKwpA"},
            {"title": "Ginza", "artist": "J Balvin", "year": 2015, "info": "A défini le son du reggaeton moderne", "youtube_id": "M1HgFbN0FXA"}
        ]
    },

    # ===================== COUNTRY & CROSSOVER =====================
    "dolly parton": {
        "anecdotes": [
            "Dolly Parton a écrit 'Jolene' et 'I Will Always Love You' le même jour.",
            "Elle a refusé la Médaille Présidentielle de la Liberté à deux reprises.",
            "Elle a investi ses royalties de Whitney Houston dans un quartier noir de Nashville.",
            "Son programme 'Imagination Library' a distribué plus de 200 millions de livres aux enfants."
        ],
        "songs_written_for_others": [
            {"title": "I Will Always Love You", "artist": "Whitney Houston", "year": 1992, "info": "Dolly a écrit la chanson en 1973, Whitney l'a rendue mondiale dans 'Bodyguard'", "youtube_id": "3JWTaaS7LdU"},
            {"title": "Jolene", "artist": "Dolly Parton", "year": 1973, "info": "Écrite le même jour que 'I Will Always Love You'", "youtube_id": "Ixrje2rXLMA"},
            {"title": "9 to 5", "artist": "Dolly Parton", "year": 1980, "info": "Écrite en tapant sur ses ongles pour imiter une machine à écrire", "youtube_id": "UbxUSsFXYo4"}
        ]
    },

    # ===================== ELECTRONIC =====================
    "avicii": {
        "anecdotes": [
            "Avicii (Tim Bergling) a commencé à produire de la musique à 16 ans dans sa chambre.",
            "Son nom de scène vient du mot bouddhiste 'Avici', le niveau le plus bas de l'enfer.",
            "Il a arrêté les tournées en 2016 à cause de problèmes de santé chroniques (pancréatite).",
            "Il est décédé en 2018 à 28 ans, laissant un héritage musical immense."
        ],
        "songs_written_for_others": [
            {"title": "Wake Me Up", "artist": "Avicii", "year": 2013, "info": "Mélange EDM-folk unique, #1 dans 22 pays", "youtube_id": "IcrbM1l_BoI"},
            {"title": "Levels", "artist": "Avicii", "year": 2011, "info": "La chanson qui a lancé la révolution EDM", "youtube_id": "_ovdm2yX4MA"},
            {"title": "Hey Brother", "artist": "Avicii", "year": 2013, "info": "Inspirée par ses propres relations familiales", "youtube_id": "6Cp6mKbRTQY"},
            {"title": "Waiting for Love", "artist": "Avicii", "year": 2015, "info": "Message d'espoir et de persévérance", "youtube_id": "cHHLHGNpCSA"},
            {"title": "Without You", "artist": "Avicii ft. Sandro Cavazza", "year": 2017, "info": "L'un de ses derniers singles officiels", "youtube_id": "WoYCsB0s2RU"},
            {"title": "The Nights", "artist": "Avicii", "year": 2014, "info": "Hymne sur le fait de vivre pleinement", "youtube_id": "UtF6Jej8yb4"}
        ]
    },
    "marshmello": {
        "anecdotes": [
            "Personne ne connaissait l'identité de Marshmello pendant des années (c'est Chris Comstock).",
            "Son casque en forme de marshmallow est devenu une icône de la culture pop.",
            "Il a organisé un concert virtuel dans le jeu Fortnite avec 10 millions de joueurs connectés.",
            "Il est aussi DJ et producteur pour des artistes pop et hip-hop."
        ],
        "songs_written_for_others": [
            {"title": "Happier", "artist": "Marshmello ft. Bastille", "year": 2018, "info": "Le clip a fait pleurer des millions de personnes", "youtube_id": "m7Bc3pLyij0"},
            {"title": "Wolves", "artist": "Selena Gomez & Marshmello", "year": 2017, "info": "Collaboration pop-EDM", "youtube_id": "cH4E_t3m3xM"},
            {"title": "Friends", "artist": "Marshmello & Anne-Marie", "year": 2018, "info": "Hymne de la friendzone", "youtube_id": "CY8E6N5Nzec"},
            {"title": "Alone", "artist": "Marshmello", "year": 2016, "info": "Sa chanson qui a tout lancé", "youtube_id": "ALZHF5UqnU4"}
        ]
    },

    # ===================== MORE PRODUCERS =====================
    "mark ronson": {
        "anecdotes": [
            "Mark Ronson a produit l'intégralité de 'Back to Black' d'Amy Winehouse.",
            "Il est le beau-frère de Samantha Ronson, DJ célèbre.",
            "'Uptown Funk' a mis 2 ans à produire et a été réécrite plusieurs fois.",
            "Il a été anobli pour ses contributions à la musique britannique."
        ],
        "songs_written_for_others": [
            {"title": "Uptown Funk", "artist": "Mark Ronson ft. Bruno Mars", "year": 2014, "info": "14 semaines #1, inspiré par le funk des années 80", "youtube_id": "OPf0YbXqDm0"},
            {"title": "Rehab", "artist": "Amy Winehouse", "year": 2006, "info": "Mark a produit le hit qui a défini l'ère d'Amy", "youtube_id": "KUmZp8pR1uc"},
            {"title": "Valerie", "artist": "Amy Winehouse", "year": 2007, "info": "Reprise mythique devenue classique"},
            {"title": "Shallow", "artist": "Lady Gaga & Bradley Cooper", "year": 2018, "info": "Co-produit pour 'A Star Is Born'", "youtube_id": "bo_efYhYU2A"},
            {"title": "Nothing Breaks Like a Heart", "artist": "Mark Ronson ft. Miley Cyrus", "year": 2018, "info": "Collaboration country-dance", "youtube_id": "A9hcJgtnm6Q"},
            {"title": "Electricity", "artist": "Silk City & Dua Lipa", "year": 2018, "info": "Grammy du meilleur enregistrement dance (avec Diplo)", "youtube_id": "AD1VnPlGaio"}
        ]
    },
    "stargate": {
        "anecdotes": [
            "Stargate est un duo norvégien composé de Tor Erik Hermansen et Mikkel Storleer Eriksen.",
            "Ils ont produit 9 singles #1 au Billboard Hot 100.",
            "Ils travaillent principalement depuis la Norvège, prouvant qu'on peut réussir sans être à LA.",
            "Leur son signature mélange pop scandinave et R&B américain."
        ],
        "songs_written_for_others": [
            {"title": "Irreplaceable", "artist": "Beyoncé", "year": 2006, "info": "Co-écrite avec Ne-Yo, #1 pendant 10 semaines", "youtube_id": "2EwViQxSJJQ"},
            {"title": "Don't Stop the Music", "artist": "Rihanna", "year": 2007, "info": "Sample de Michael Jackson 'Wanna Be Startin' Somethin'", "youtube_id": "yd8jh9QYfEs"},
            {"title": "So Sick", "artist": "Ne-Yo", "year": 2006, "info": "Leur première collaboration avec Ne-Yo", "youtube_id": "IxszlJppRQI"},
            {"title": "Firework", "artist": "Katy Perry", "year": 2010, "info": "Hymne d'empowerment co-produit avec Sandy Vee", "youtube_id": "QGJuMBdaqIw"},
            {"title": "S&M", "artist": "Rihanna", "year": 2011, "info": "Hit pop provocateur", "youtube_id": "KdS6HFQ_LUc"},
            {"title": "Only Girl (In the World)", "artist": "Rihanna", "year": 2010, "info": "Grammy de la meilleure chanson dance", "youtube_id": "pa14VNsdSYM"}
        ]
    },
    "dr. luke": {
        "anecdotes": [
            "Dr. Luke (Lukasz Gottwald) a commencé comme guitariste de Saturday Night Live.",
            "Il a écrit et produit plus de 30 singles #1.",
            "Sa carrière a été marquée par un procès très médiatisé avec Kesha.",
            "Il produit souvent sous le pseudonyme 'Tyson Trax' depuis les controverses."
        ],
        "songs_written_for_others": [
            {"title": "Since U Been Gone", "artist": "Kelly Clarkson", "year": 2004, "info": "Co-écrite avec Max Martin, le hit qui a tout lancé", "youtube_id": "R7UrFYvl5TE"},
            {"title": "Tik Tok", "artist": "Kesha", "year": 2009, "info": "#1 pendant 9 semaines", "youtube_id": "iP6XpLQM2Cs"},
            {"title": "California Gurls", "artist": "Katy Perry ft. Snoop Dogg", "year": 2010, "info": "Hit de l'été 2010", "youtube_id": "F57P9C4SAW4"},
            {"title": "Roar", "artist": "Katy Perry", "year": 2013, "info": "Avec Max Martin", "youtube_id": "CevxZvSJLk8"},
            {"title": "Wrecking Ball", "artist": "Miley Cyrus", "year": 2013, "info": "Le clip controversé le plus vu de 2013", "youtube_id": "My2FRPA3Gf8"}
        ]
    },

    # ===================== SOUL & R&B CLASSICS =====================
    "stevie wonder": {
        "anecdotes": [
            "Stevie Wonder est aveugle depuis sa naissance et a signé avec Motown à 11 ans.",
            "Il joue du piano, de l'harmonica, de la batterie et chante - il est multi-instrumentiste.",
            "Il a remporté 25 Grammy Awards, un record pour un artiste solo.",
            "Il a été un acteur clé dans la création du Martin Luther King Jr. Day aux USA."
        ],
        "songs_written_for_others": [
            {"title": "Superstition", "artist": "Stevie Wonder", "year": 1972, "info": "Initialement écrite pour Jeff Beck mais Stevie l'a gardée", "youtube_id": "0CFuCYNx-1g"},
            {"title": "I Just Called to Say I Love You", "artist": "Stevie Wonder", "year": 1984, "info": "Oscar de la meilleure chanson originale", "youtube_id": "1bGOgY1CmiU"},
            {"title": "Signed, Sealed, Delivered", "artist": "Stevie Wonder", "year": 1970, "info": "Un classique intemporel de la soul", "youtube_id": "pUj9frKY46E"},
            {"title": "Tell Me Something Good", "artist": "Rufus ft. Chaka Khan", "year": 1974, "info": "Écrite et offerte à Rufus par Stevie", "youtube_id": "PubiRn6Al4U"}
        ]
    }
}
