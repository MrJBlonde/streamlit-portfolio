# ──────────────────────────────────────────────
# config.py — V3 Business Analyst Portfolio
# Marine & Cuivre | Poppins | Dark/Light toggle
# ──────────────────────────────────────────────

# ── Palette ───────────────────────────────────
COLORS = {
    "light": {
        "bg": "#FAF7F2",
        "bg_card": "#FFFFFF",
        "bg_sidebar": "#1E3A5F",
        "text": "#1E3A5F",
        "text_muted": "#5A6E82",
        "accent": "#C47D4E",
        "accent_hover": "#A8643A",
        "border": "#E4DDD3",
    },
    "dark": {
        "bg": "#0E1F33",
        "bg_card": "#162B45",
        "bg_sidebar": "#0A1628",
        "text": "#E8E0D4",
        "text_muted": "#9AABBF",
        "accent": "#C47D4E",
        "accent_hover": "#D99A6C",
        "border": "#253D58",
    },
}

# ── Contact ───────────────────────────────────
CONTACT = {
    "phone": "07 50 97 03 53",
    "email": "pro.gauthier.julien@gmail.com",
    "linkedin_url": "https://www.linkedin.com/in/julien-gauthier-299b59211",
    "linkedin_label": "julien-gauthier",
    "github_url": "https://github.com/MrJBLONDE",
    "github_label": "MrJBLONDE",
    "location_fr": "Orléans & France",
    "location_en": "Orléans & France",
}

# ── Texts ─────────────────────────────────────
TEXTS = {
    "fr": {
        # Nav
        "nav_about": "Qui suis-je",
        "nav_cv": "Mon CV",
        "nav_projects": "Mes projets",
        "nav_contact": "Contact",
        # About page
        "hello": "Bonjour, moi c'est",
        "name": "Julien GAUTHIER",
        "title": "Business Analyst · Data Analyst",
        "pitch": "Après 3 ans dans le management RH — coordination d'équipes de 7 à 200 personnes, 2 000+ entretiens, pilotage de KPIs — j'ai fait le choix de la data. Aujourd'hui je cadre le besoin métier, je structure la donnée et je livre des analyses qui servent la décision.",
        "cta_cv": "Mon CV",
        "cta_projects": "Mes projets",
        "cta_contact": "Me contacter",
        # CV page
        "cv_title": "Mon CV",
        "cv_download": "📥 Télécharger le PDF",
        "cv_placeholder": "📄 Ajouter cv_julien.pdf dans assets/",
        "soft_title": "Ce que j'apporte au-delà de la technique",
        # Projects page
        "projects_title": "Mes projets",
        "projects_intro": "Du cadrage au déploiement — voici ce que je sais faire.",
        "tag_flagship": "PROJET PHARE",
        "tag_perso": "PROJET PERSO",
        "tag_formation": "FORMATION",
        "btn_github": "Voir sur GitHub",
        # Contact page
        "contact_title": "On échange ?",
        "contact_intro": "Je suis disponible pour une alternance Business Analyst à partir de septembre 2026, sur le bassin Orléans / Tours / Blois et en France.",
    },
    "en": {
        # Nav
        "nav_about": "About me",
        "nav_cv": "My resume",
        "nav_projects": "My projects",
        "nav_contact": "Contact",
        # About page
        "hello": "Hi, I'm",
        "name": "Julien GAUTHIER",
        "title": "Business Analyst · Data Analyst",
        "pitch": "After 3 years in HR management — coordinating teams of 7 to 200 people, 2,000+ interviews, KPI monitoring — I chose to move into data. Today I scope business needs, structure data, and deliver insights that drive decisions.",
        "cta_cv": "My resume",
        "cta_projects": "My projects",
        "cta_contact": "Get in touch",
        # CV page
        "cv_title": "My resume",
        "cv_download": "📥 Download PDF",
        "cv_placeholder": "📄 Add cv_julien.pdf to assets/",
        "soft_title": "What I bring beyond technical skills",
        # Projects page
        "projects_title": "My projects",
        "projects_intro": "From scoping to deployment — here's what I can do.",
        "tag_flagship": "FLAGSHIP",
        "tag_perso": "PERSONAL",
        "tag_formation": "TRAINING",
        "btn_github": "View on GitHub",
        # Contact page
        "contact_title": "Let's talk",
        "contact_intro": "I'm available for a Business Analyst apprenticeship starting September 2026, in the Orléans / Tours / Blois area and across France.",
    },
}

# ── Soft Skills ───────────────────────────────
SOFT_SKILLS = {
    "fr": [
        {
            "icon": "🔍",
            "title": "Analyse & esprit critique",
            "desc": "Décortiquer un besoin métier, challenger les hypothèses, prioriser les actions.",
        },
        {
            "icon": "🎯",
            "title": "Cadrage & rigueur",
            "desc": "Spécifications fonctionnelles, documentation, livrables structurés.",
        },
        {
            "icon": "💬",
            "title": "Communication & pédagogie",
            "desc": "Traduire la data en langage décideur. Restitution claire, sans jargon.",
        },
        {
            "icon": "👥",
            "title": "Management & coordination",
            "desc": "3 ans d'encadrement (7 à 200 pers.), interface métier-tech, gestion des priorités.",
        },
        {
            "icon": "📐",
            "title": "Qualité & conformité",
            "desc": "RGPD, contrôle qualité données, traçabilité des traitements.",
        },
        {
            "icon": "🔄",
            "title": "Curiosité & apprentissage",
            "desc": "Reconversion choisie, veille active, montée en compétences continue.",
        },
    ],
    "en": [
        {
            "icon": "🔍",
            "title": "Analytical thinking",
            "desc": "Break down business needs, challenge assumptions, prioritize actions.",
        },
        {
            "icon": "🎯",
            "title": "Scoping & rigor",
            "desc": "Functional specifications, documentation, structured deliverables.",
        },
        {
            "icon": "💬",
            "title": "Communication & teaching",
            "desc": "Translate data into decision-maker language. Clear reporting, no jargon.",
        },
        {
            "icon": "👥",
            "title": "Management & coordination",
            "desc": "3 years leading teams (7 to 200), business-tech interface, priority management.",
        },
        {
            "icon": "📐",
            "title": "Quality & compliance",
            "desc": "GDPR, data quality control, processing traceability.",
        },
        {
            "icon": "🔄",
            "title": "Curiosity & learning",
            "desc": "Deliberate career switch, active monitoring, continuous upskilling.",
        },
    ],
}

# ── Projects ──────────────────────────────────
PROJECTS = {
    "fr": [
        {
            "id": "labyrinthe",
            "title": "🌽 Labyrinthe de Beaugency",
            "subtitle": "Stage — Infrastructure data complète",
            "tag": "flagship",
            "desc": "Conception et déploiement d'une infra data from scratch pour un site touristique saisonnier (6 ha, Loiret). Ingestion API, transformation, ML prédictif (fréquentation J+1 à J+5), dashboard Power BI 6 pages.",
            "stack": ["Python", "pandas", "scikit-learn", "SQL", "Supabase", "Power BI", "Streamlit", "Railway", "Git"],
            "metrics": {"Pages dashboard": "6", "Sources de données": "5", "Effort estimé": "~148h", "Coût infra": "0€"},
            "github": "https://github.com/MrJBLONDE",
        },
        {
            "id": "ygo",
            "title": "🎴 YGO Proxy FR",
            "subtitle": "Projet perso — Générateur de proxys Yu-Gi-Oh!",
            "tag": "perso",
            "desc": "Application web de génération de proxys Yu-Gi-Oh! en français avec dashboard analytics. API YGOProDeck, traduction DeepL avec cache Supabase, génération PDF.",
            "stack": ["Python", "Streamlit", "PostgreSQL", "Supabase", "DeepL API", "reportlab", "Git"],
            "metrics": {},
            "github": "https://github.com/MrJBLONDE",
        },
        {
            "id": "p8",
            "title": "📊 Profils sociodémographiques — ETL Snowflake",
            "subtitle": "P8 — Pipeline ETL/ELT complet",
            "tag": "formation",
            "desc": "Pipeline ETL/ELT complet sur Snowflake avec dbt Cloud : extraction, transformation et analyse de profils sociodémographiques d'étudiants OpenClassrooms.",
            "stack": ["dbt Cloud", "Snowflake", "SQL", "Git"],
            "metrics": {},
            "github": "https://github.com/MrJBLONDE",
        },
        {
            "id": "p7",
            "title": "📈 Profils sociodémographiques — SQL/dbt",
            "subtitle": "P7 — Collecte, nettoyage, agrégation",
            "tag": "formation",
            "desc": "Collecte, nettoyage et agrégation de données via le workflow dbt : définition des règles de transformation, vérification de la cohérence et fiabilité des données.",
            "stack": ["SQL", "dbt", "ETL/ELT", "Git"],
            "metrics": {},
            "github": "https://github.com/MrJBLONDE",
        },
        {
            "id": "p6",
            "title": "📉 Dashboard Power BI — Suivi de projets",
            "subtitle": "P6 — Tableau de bord décisionnel",
            "tag": "formation",
            "desc": "Création d'un tableau de bord dynamique Power BI pour visualiser l'avancement de projets et les KPI associés. Power Query pour la préparation des données.",
            "stack": ["Power BI", "Power Query", "DAX"],
            "metrics": {},
            "github": "https://github.com/MrJBLONDE",
        },
        {
            "id": "p5",
            "title": "🛒 Optimisation données boutique",
            "subtitle": "P5 — Modélisation dbt",
            "tag": "formation",
            "desc": "Optimisation de la gestion des données d'une boutique via dbt : modélisation, tests automatisés et documentation des transformations.",
            "stack": ["Python", "dbt", "SQL", "Git"],
            "metrics": {},
            "github": "https://github.com/MrJBLONDE",
        },
        {
            "id": "p4",
            "title": "🏠 Base de données immobilière",
            "subtitle": "P4 — Conception & requêtage SQL",
            "tag": "formation",
            "desc": "Conception, création et requêtage d'une base de données immobilière structurée. Modélisation relationnelle, requêtes complexes.",
            "stack": ["SQL", "MySQL", "PostgreSQL"],
            "metrics": {},
            "github": "https://github.com/MrJBLONDE",
        },
    ],
    "en": [
        {
            "id": "labyrinthe",
            "title": "🌽 Labyrinthe de Beaugency",
            "subtitle": "Internship — Full data infrastructure",
            "tag": "flagship",
            "desc": "Design and deployment of a complete data infrastructure from scratch for a seasonal tourist site (6 ha corn maze, Loiret). API ingestion, transformation, predictive ML (attendance D+1 to D+5), 6-page Power BI dashboard.",
            "stack": ["Python", "pandas", "scikit-learn", "SQL", "Supabase", "Power BI", "Streamlit", "Railway", "Git"],
            "metrics": {"Dashboard pages": "6", "Data sources": "5", "Estimated effort": "~148h", "Infra cost": "€0"},
            "github": "https://github.com/MrJBLONDE",
        },
        {
            "id": "ygo",
            "title": "🎴 YGO Proxy FR",
            "subtitle": "Personal — Yu-Gi-Oh! proxy generator",
            "tag": "perso",
            "desc": "French-language Yu-Gi-Oh! proxy generator web app with analytics dashboard. YGOProDeck API, DeepL translation with Supabase caching, PDF generation.",
            "stack": ["Python", "Streamlit", "PostgreSQL", "Supabase", "DeepL API", "reportlab", "Git"],
            "metrics": {},
            "github": "https://github.com/MrJBLONDE",
        },
        {
            "id": "p8",
            "title": "📊 Sociodemographic profiles — Snowflake ETL",
            "subtitle": "P8 — Full ETL/ELT pipeline",
            "tag": "formation",
            "desc": "Complete ETL/ELT pipeline on Snowflake with dbt Cloud: extraction, transformation and analysis of OpenClassrooms student sociodemographic profiles.",
            "stack": ["dbt Cloud", "Snowflake", "SQL", "Git"],
            "metrics": {},
            "github": "https://github.com/MrJBLONDE",
        },
        {
            "id": "p7",
            "title": "📈 Sociodemographic profiles — SQL/dbt",
            "subtitle": "P7 — Collection, cleaning, aggregation",
            "tag": "formation",
            "desc": "Data collection, cleaning and aggregation via dbt workflow: transformation rules, consistency checks and data reliability.",
            "stack": ["SQL", "dbt", "ETL/ELT", "Git"],
            "metrics": {},
            "github": "https://github.com/MrJBLONDE",
        },
        {
            "id": "p6",
            "title": "📉 Power BI Dashboard — Project tracking",
            "subtitle": "P6 — Decision-making dashboard",
            "tag": "formation",
            "desc": "Dynamic Power BI dashboard to visualize project progress and associated KPIs. Power Query for data preparation.",
            "stack": ["Power BI", "Power Query", "DAX"],
            "metrics": {},
            "github": "https://github.com/MrJBLONDE",
        },
        {
            "id": "p5",
            "title": "🛒 Store data optimization",
            "subtitle": "P5 — dbt modeling",
            "tag": "formation",
            "desc": "Store data management optimization via dbt: modeling, automated testing and transformation documentation.",
            "stack": ["Python", "dbt", "SQL", "Git"],
            "metrics": {},
            "github": "https://github.com/MrJBLONDE",
        },
        {
            "id": "p4",
            "title": "🏠 Real estate database",
            "subtitle": "P4 — SQL design & querying",
            "tag": "formation",
            "desc": "Design, creation and querying of a structured real estate database. Relational modeling, complex queries.",
            "stack": ["SQL", "MySQL", "PostgreSQL"],
            "metrics": {},
            "github": "https://github.com/MrJBLONDE",
        },
    ],
}
