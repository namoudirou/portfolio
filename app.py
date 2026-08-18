import streamlit as st

# Variables de contact (À personnaliser)
EMAIL = "sakanamoudirou@gmail.com"
PHONE = "+229 01 53 74 39 83"
LOCATION = "Bénin, Abomey-calavi"
GITHUB_URL = "https://github.com/namoudirou"
LINKEDIN_URL = "https://linkedin.com"

# 1. Configuration de la page
st.set_page_config(
    page_title="SAKA BAGOU Namoudirou | Portfolio",
    page_icon="᭚",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Design Minimaliste, CSS, Carousel & Footer
st.markdown("""
<style>
    /* Défilement fluide pour la navigation */
    html {
        scroll-behavior: smooth;
    }

    /* Reset & Palette Minimaliste */
    .stApp {
        background-color: #0b0c0e;
        color: #cecece;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }

    #MainMenu, footer, header {visibility: hidden;}

    /* Conteneur principal */
    .block-container {
        max-width: 1150px !important;
        padding-top: 1rem !important;
        padding-bottom: 2rem !important;
    }

    /* Navigation Fixe */
    .navbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 20px 0;
        border-bottom: 1px solid #1a1d21;
        background-color: #0b0c0e;
        position: sticky;
        top: 0;
        z-index: 999;
    }
    .nav-brand {
        color: #ffffff;
        font-weight: 600;
        font-size: 2rem;
        text-decoration: none;
    }
    .nav-links {
        display: flex;
        gap: 28px;
    }
    .nav-link {
        color: #888888;
        text-decoration: none;
        font-size: 0.88rem;
        font-weight: 500;
        transition: color 0.2s ease;
    }
    .nav-link:hover {
        color: #ffffff;
    }

    /* En-tête / Hero */
    .hero-container {
        padding: 60px 0 50px 0;
        border-bottom: 1px solid #1a1d21;
    }
    .hero-title {
        font-size: 2.4rem;
        font-weight: 600;
        color: #ffffff;
        letter-spacing: -0.02em;
        margin-bottom: 8px;
    }
    .hero-name {
        font-size: 4rem;
        font-weight: 900;
        color: #ffffff;
        letter-spacing: -0.02em;
        margin-bottom: 8px;
    }
    .hero-subtitle {
        font-size: 1.15rem;
        color: #888888;
        font-weight: 400;
        margin: 0;
    }

    /* Titres de Sections */
    .section-label {
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 0.12em;
        color: #666666;
        margin-top: 60px;
        margin-bottom: 25px;
        font-weight: 600;
        scroll-margin-top: 80px;
    }

    /* Cartes Services */
    .minimal-card {
        background-color: #111317;
        border: 1px solid #1c1f26;
        border-radius: 8px;
        overflow: hidden;
        margin-bottom: 20px;
        transition: transform 0.3s ease, border-color 0.3s ease;
        display: flex;
        flex-direction: column;
        height: 100%;
    }
    .minimal-card:hover {
        transform: translateY(-4px);
        border-color: #2e3440;
    }

    .card-body {
        padding: 22px;
        display: flex;
        flex-direction: column;
        flex-grow: 1;
    }
    .card-title {
        color: #ffffff;
        font-size: 1.05rem;
        font-weight: 600;
        margin-top: 0;
        margin-bottom: 8px;
    }
    .card-desc {
        color: #888888;
        font-size: 0.9rem;
        line-height: 1.5;
        margin-bottom: 16px;
        flex-grow: 1;
    }

    .tech-tag {
        display: inline-block;
        background: #181b20;
        color: #a0a0a0;
        border: 1px solid #282c35;
        padding: 3px 10px;
        border-radius: 4px;
        font-size: 0.78rem;
        margin-right: 6px;
        margin-bottom: 6px;
    }

    /* Style Carte de Contact */
    .contact-card {
        background-color: #111317;
        border: 1px solid #1c1f26;
        border-radius: 8px;
        padding: 10px 24px;
        max-width: 650px;
    }
    .contact-row {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 16px 0;
        border-bottom: 1px solid #1a1d21;
        font-size: 0.92rem;
    }
    .contact-row:last-child {
        border-bottom: none;
    }
    .contact-label-group {
        display: flex;
        align-items: center;
        gap: 12px;
    }
    .contact-icon {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        color: #888888;
    }
    .contact-row .label {
        color: #888888;
        font-weight: 500;
        text-transform: capitalize;
    }
    .contact-row a, .contact-row span:not(.label) {
        color: #ffffff;
        text-decoration: none;
        font-weight: 500;
        transition: color 0.2s ease;
    }
    .contact-row a:hover {
        color: #58a6ff;
    }

    /* Pied de Page / Footer */
    .footer {
        margin-top: 80px;
        padding: 30px 0;
        border-top: 1px solid #1a1d21;
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-size: 0.85rem;
        color: #666666;
    }
    .footer a {
        color: #888888;
        text-decoration: none;
        transition: color 0.2s ease;
    }
    .footer a:hover {
        color: #ffffff;
    }
    .btn-voir-plus {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 100%;
            padding: 8px 14px;
            background-color: #181b20;
            color: #cecece;
            border: 1px solid #282c35;
            border-radius: 6px;
            font-size: 0.82rem;
            font-weight: 500;
            text-decoration: none;
            box-sizing: border-box;
            transition: all 0.25s ease;
        }
        .btn-voir-plus:hover {
            background-color: #ffffff;
            color: #0b0c0e;
            border-color: #ffffff;
        }
</style>
""", unsafe_allow_html=True)

# 3. Navigation Fixe
st.markdown("""
<nav class="navbar">
    <a href="https://github.com/namoudirou" style="text-decoration: none;" class="nav-brand">᭚</a>
    <div class="nav-links">
        <a href="#services" style="text-decoration: none;" class="btn-voir-plus">Services</a>
        <a href="#realisations" style="text-decoration: none;"  class="btn-voir-plus">Réalisations</a>
        <a href="#contact" style="text-decoration: none;"  class="btn-voir-plus">Contact</a>
    </div>
</nav>
""", unsafe_allow_html=True)

# 4. En-tête
st.markdown("""
<div class="hero-container">
    <div class="hero-title">Bonjour ,  je suis</div>
    <div class="hero-name">SAKA BAGOU Namoudirou</div>
    <div class="hero-subtitle">Développeur Web</div>
</div>
""", unsafe_allow_html=True)

# 5. Section : Services
st.markdown('<div id="services" class="section-label">Compétences & Services</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="minimal-card">
        <div class="card-body">
            <div class="card-title">Frontend et Interfaces</div>
            <div class="card-desc">Si vous avez besoin de développer une application dynamique et réactive, je maitrise le framework React.</div>
            <div>
                <span class="tech-tag">React</span>
                <span class="tech-tag">HTMX</span>
                <span class="tech-tag">JQuery</span>
            </div>
        </div>
    </div>
    <div class="minimal-card">
        <div class="card-body">
            <div class="card-title">Bases de Données</div>
            <div class="card-desc">Modélisation de données, optimisation des schémas et administration.</div>
            <div>
                <span class="tech-tag">MySQL</span>
                <span class="tech-tag">PostgreSQL</span>
                <span class="tech-tag">Oracle</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="minimal-card">
        <div class="card-body">
            <div class="card-title">Backend et APIs</div>
            <div class="card-desc">Développement d'APIs REST performantes et mise en place de logiques métiers robustes.</div>
            <div>
                <span class="tech-tag">Laravel</span>
                <span class="tech-tag">Django</span>
                <span class="tech-tag">Spring Boot</span>
                <span class="tech-tag">Adonisjs</span>
            </div>
        </div>
    </div>
    <div class="minimal-card">
        <div class="card-body">
            <div class="card-title">Environnement et Outils</div>
            <div class="card-desc">Je suis à laise avec l'environnement linux et github</div>
            <div>
                <span class="tech-tag">Git</span>
                <span class="tech-tag">Linux</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 6. Section : Réalisations (Carousel interactif)
st.markdown('<div id="realisations" class="section-label">Réalisations</div>', unsafe_allow_html=True)


carousel_html = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body {
            margin: 0;
            background: transparent;
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            color: #cecece;
        }
        .carousel-container {
            position: relative;
            width: 100%;
            overflow: hidden;
            padding: 10px 0;
        }
        .carousel-track {
            display: flex;
            gap: 20px;
            transition: transform 0.4s cubic-bezier(0.25, 1, 0.5, 1);
        }
        .card {
            min-width: 320px;
            max-width: 320px;
            background-color: #111317;
            border: 1px solid #1c1f26;
            border-radius: 8px;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            box-sizing: border-box;
            transition: border-color 0.3s ease, transform 0.3s ease;
        }
        .card:hover {
            border-color: #2e3440;
            transform: translateY(-4px);
        }
        .card-img {
            width: 100%;
            height: 170px;
            object-fit: cover;
        }
        .card-body {
            padding: 18px;
            display: flex;
            flex-direction: column;
            flex-grow: 1;
        }
        .card-title {
            color: #ffffff;
            font-size: 1rem;
            font-weight: 600;
            margin: 0 0 8px 0;
        }
        .card-desc {
            color: #888888;
            font-size: 0.85rem;
            line-height: 1.4;
            margin-bottom: 14px;
            flex-grow: 1;
        }
        .tech-tag {
            display: inline-block;
            background: #181b20;
            color: #a0a0a0;
            border: 1px solid #282c35;
            padding: 2px 8px;
            border-radius: 4px;
            font-size: 0.75rem;
            margin-right: 4px;
            margin-bottom: 12px;
        }
        .btn-voir-plus {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 100%;
            padding: 8px 14px;
            background-color: #181b20;
            color: #cecece;
            border: 1px solid #282c35;
            border-radius: 6px;
            font-size: 0.82rem;
            font-weight: 500;
            text-decoration: none;
            box-sizing: border-box;
            transition: all 0.25s ease;
        }
        .btn-voir-plus:hover {
            background-color: #ffffff;
            color: #0b0c0e;
            border-color: #ffffff;
        }
        .nav-controls {
            display: flex;
            justify-content: flex-end;
            gap: 10px;
            margin-bottom: 12px;
        }
        .nav-btn {
            background: #111317;
            border: 1px solid #1c1f26;
            color: #ffffff;
            width: 36px;
            height: 36px;
            border-radius: 50%;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1rem;
            transition: background 0.2s ease, border-color 0.2s ease;
        }
        .nav-btn:hover {
            background: #181b20;
            border-color: #444;
        }
    </style>
</head>
<body>
    <div class="nav-controls">
        <button class="nav-btn" onclick="moveSlide(-1)">←</button>
        <button class="nav-btn" onclick="moveSlide(1)">→</button>
    </div>
    <div class="carousel-container">
        <div class="carousel-track" id="track">
            <!-- Carte 1 -->
            <div class="card">
                <img class="card-img" src="/img/qrpaye.png" alt="Service numérique et paiement">
                <div class="card-body">
                    <h3 class="card-title">QRPAYE et QRSERVICES</h3>
                    <p class="card-desc">Application de service numérique et de paiement.</p>
                    <div>
                        <span class="tech-tag">LARAVEL</span>
                        <span class="tech-tag">JQUERY</span>
                        <span class="tech-tag">Bootstrap</span>
                    </div>
                    <a href="https://qrpaye.com/" target="_blank" class="btn-voir-plus">Voir le projet ↗</a>
                </div>
            </div>
            <!-- Carte 2 -->
            <div class="card">
                <img class="card-img" src="/img/lorago.png" alt="Vente magasins">
                <div class="card-body">
                    <h3 class="card-title">LORAGO DISTRIBUTION</h3>
                    <p class="card-desc">Système de gestions de magasins.</p>
                    <div>
                        <span class="tech-tag">LARAVEL</span>
                        <span class="tech-tag">JQUERY</span>
                        <span class="tech-tag">Bootstrap</span>
                    </div>
                    <a href="https://loragodistribution.com/" target="_blank" class="btn-voir-plus">Voir le projet ↗</a>
                </div>
            </div>
            <!-- Carte 3 -->
            <div class="card">
                <img class="card-img" src="/img/aeroport.png" alt="Point de vente en ligne">
                <div class="card-body">
                    <h3 class="card-title">LORAGO DISTRIBUTION</h3>
                    <p class="card-desc">Application E-commerce.</p>
                    <div>
                        <span class="tech-tag">LARAVEL</span>
                        <span class="tech-tag">JQUERY</span>
                        <span class="tech-tag">Bootstrap</span>
                    </div>
                    <a href="https://aeropnr.loragodistribution.com/" target="_blank" class="btn-voir-plus">Voir le projet ↗</a>
                </div>
            </div>
            <!-- Carte 4 (Supplémentaire pour carousel) -->
            <div class="card">
                <img class="card-img" src="" alt="Gestions des assets">
                <div class="card-body">
                    <h3 class="card-title">ASSET4ALL</h3>
                    <p class="card-desc">Application de gestions des assets pour la cité interministérielle du Bénin</p>
                    <div>
                        <span class="tech-tag">LARAVEL</span>
                        <span class="tech-tag">JQUERY</span>
                        <span class="tech-tag">Bootstrap</span>
                    </div>
                    <a href="https://asset4all.webentite.com/" target="_blank" class="btn-voir-plus">Voir le projet ↗</a>
                </div>
            </div>
        </div>
    </div>

    <script>
        let currentIndex = 0;
        const track = document.getElementById('track');
        const cards = document.querySelectorAll('.card');
        const cardWidth = 340; // width + gap

        function moveSlide(direction) {
            const maxIndex = cards.length - Math.floor(window.innerWidth / cardWidth);
            currentIndex += direction;
            if (currentIndex < 0) currentIndex = 0;
            if (currentIndex > maxIndex) currentIndex = maxIndex > 0 ? maxIndex : 0;
            
            track.style.transform = `translateX(-${currentIndex * cardWidth}px)`;
        }
    </script>
</body>
</html>
"""

st.components.v1.html(carousel_html, height=430)

# 7. Section : Me Contacter
st.markdown('<div id="contact" class="section-label">Me Contacter</div>', unsafe_allow_html=True)

col_info, _ = st.columns([1.5, 0.5])

with col_info:
    st.markdown(
        f"""
        <div class="contact-card">
            <div class="contact-row">
                <div class="contact-label-group">
                    <span class="contact-icon">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
                    </span>
                    <span class="label">email</span>
                </div>
                <a href="mailto:{EMAIL}">{EMAIL}</a>
            </div>
            <div class="contact-row">
                <div class="contact-label-group">
                    <span class="contact-icon">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
                    </span>
                    <span class="label">téléphone</span>
                </div>
                <a href="tel:{PHONE}">{PHONE}</a>
            </div>
            <div class="contact-row">
                <div class="contact-label-group">
                    <span class="contact-icon">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
                    </span>
                    <span class="label">localisation</span>
                </div>
                <span>{LOCATION}</span>
            </div>
            <div class="contact-row">
                <div class="contact-label-group">
                    <span class="contact-icon">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path></svg>
                    </span>
                    <span class="label">github</span>
                </div>
                <a href="{GITHUB_URL}" target="_blank">voir le profil ↗</a>
            </div>
            <div class="contact-row">
                <div class="contact-label-group">
                    <span class="contact-icon">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg>
                    </span>
                    <span class="label">linkedin</span>
                </div>
                <a href="{LINKEDIN_URL}" target="_blank">voir le profil ↗</a>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# 8. Pied de page (Footer)
st.markdown("""
<div class="footer">
    <div>© SAKA BAGOU Namoudirou — Développeur Web FullStack</div>
    <div>Conçu avec Streamlit</div>
</div>
""", unsafe_allow_html=True)