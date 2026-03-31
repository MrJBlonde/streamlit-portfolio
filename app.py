import streamlit as st
from config import TEXTS, SOFT_SKILLS, PROJECTS, CONTACT
from styles import inject_custom_css

# ──────────────────────────────────────────────
# Page config
# ──────────────────────────────────────────────
st.set_page_config(
    page_title="Julien GAUTHIER — Business Analyst",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ──────────────────────────────────────────────
# Sidebar
# ──────────────────────────────────────────────
with st.sidebar:
    # Dark mode toggle
    dark = st.toggle("🌙 Dark mode", value=False, key="dark_toggle")

    # Language toggle
    lang = st.toggle("🇬🇧 English", value=False, key="lang_toggle")
    L = "en" if lang else "fr"

    st.markdown("---")

    page = st.radio(
        label="Navigation",
        options=[
            TEXTS[L]["nav_about"],
            TEXTS[L]["nav_cv"],
            TEXTS[L]["nav_projects"],
            TEXTS[L]["nav_contact"],
        ],
        label_visibility="collapsed",
    )

    st.markdown("---")
    st.markdown(
        f"""
        <div style="font-size:0.75rem; opacity:0.7; line-height:1.6;">
            📍 {CONTACT['location_fr'] if L == 'fr' else CONTACT['location_en']}<br>
            ✉️ {CONTACT['email']}
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div style="text-align:center; opacity:0.4; font-size:0.7rem; margin-top:2rem;">'
        "Built with Streamlit · © 2026</div>",
        unsafe_allow_html=True,
    )

# Inject CSS after sidebar choices
inject_custom_css(dark_mode=dark)


# ══════════════════════════════════════════════
# PAGE 1 — QUI SUIS-JE
# ══════════════════════════════════════════════
if page == TEXTS[L]["nav_about"]:

    col_photo, col_text = st.columns([1, 3], gap="large")

    with col_photo:
        try:
            st.image("assets/photo_julien.jpg", width=160)
        except Exception:
            st.markdown(
                '<div style="display:flex; justify-content:center; padding-top:0.5rem;">'
                '<div class="photo-placeholder">JG</div></div>',
                unsafe_allow_html=True,
            )

    with col_text:
        st.markdown(f'<p class="hero-hello">{TEXTS[L]["hello"]}</p>', unsafe_allow_html=True)
        st.markdown(f'<h1 class="hero-name">{TEXTS[L]["name"]}</h1>', unsafe_allow_html=True)
        st.markdown(f'<p class="hero-title">{TEXTS[L]["title"]}</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="hero-pitch">{TEXTS[L]["pitch"]}</p>', unsafe_allow_html=True)

        st.markdown(
            f"""
            <div class="cta-row">
                <a class="cta-btn cta-primary" href="#" onclick="return false;">
                    {TEXTS[L]["cta_cv"]}
                </a>
                <a class="cta-btn cta-secondary" href="#" onclick="return false;">
                    {TEXTS[L]["cta_projects"]}
                </a>
                <a class="cta-btn cta-secondary" href="#" onclick="return false;">
                    {TEXTS[L]["cta_contact"]}
                </a>
            </div>
            """,
            unsafe_allow_html=True,
        )


# ══════════════════════════════════════════════
# PAGE 2 — MON CV
# ══════════════════════════════════════════════
elif page == TEXTS[L]["nav_cv"]:

    st.markdown(f'<h1 class="section-title">{TEXTS[L]["cv_title"]}</h1>', unsafe_allow_html=True)

    col_cv, col_dl = st.columns([3, 1], gap="large")

    with col_cv:
        # Try to show CV image preview
        try:
            st.image("assets/cv_preview.png", use_container_width=True)
        except Exception:
            st.markdown(
                '<div class="cv-preview-container">'
                '<p style="padding:3rem 1rem; opacity:0.5;">Aperçu du CV<br>'
                '<small>Ajouter cv_preview.png dans assets/</small></p></div>',
                unsafe_allow_html=True,
            )

    with col_dl:
        # Download button
        try:
            with open("assets/cv_julien.pdf", "rb") as f:
                cv_bytes = f.read()
            st.download_button(
                label=TEXTS[L]["cv_download"],
                data=cv_bytes,
                file_name="CV_Julien_GAUTHIER_Business_Analyst.pdf",
                mime="application/pdf",
            )
        except FileNotFoundError:
            st.info(TEXTS[L]["cv_placeholder"])

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    # ── Soft Skills ───────────────────────────
    st.markdown(
        f'<h2 class="section-title">{TEXTS[L]["soft_title"]}</h2>',
        unsafe_allow_html=True,
    )

    soft_html = '<div class="soft-grid">'
    for skill in SOFT_SKILLS[L]:
        soft_html += f"""
        <div class="soft-card">
            <div class="soft-icon">{skill['icon']}</div>
            <div class="soft-name">{skill['title']}</div>
            <div class="soft-desc">{skill['desc']}</div>
        </div>
        """
    soft_html += "</div>"

    st.markdown(soft_html, unsafe_allow_html=True)


# ══════════════════════════════════════════════
# PAGE 3 — MES PROJETS
# ══════════════════════════════════════════════
elif page == TEXTS[L]["nav_projects"]:

    st.markdown(f'<h1 class="section-title">{TEXTS[L]["projects_title"]}</h1>', unsafe_allow_html=True)
    st.markdown(f'<p class="section-intro">{TEXTS[L]["projects_intro"]}</p>', unsafe_allow_html=True)

    for project in PROJECTS[L]:
        # Card class
        card_class = "project-card-flagship" if project["tag"] == "flagship" else "project-card"

        # Tag
        tag_map = {
            "flagship": ("tag-flagship", TEXTS[L]["tag_flagship"]),
            "perso": ("tag-perso", TEXTS[L]["tag_perso"]),
            "formation": ("tag-formation", TEXTS[L]["tag_formation"]),
        }
        tag_cls, tag_label = tag_map[project["tag"]]

        # Stack tags
        stack_html = "".join(f'<span class="stack-tag">{t}</span>' for t in project["stack"])

        # Metrics
        metrics_html = ""
        if project["metrics"]:
            metrics_html = '<div class="metrics-row">'
            for label, val in project["metrics"].items():
                metrics_html += f"""
                <div class="metric-item">
                    <div class="metric-val">{val}</div>
                    <div class="metric-lbl">{label}</div>
                </div>
                """
            metrics_html += "</div>"

        # GitHub link
        github_html = (
            f'<a href="{project["github"]}" target="_blank" class="cta-btn cta-secondary" '
            f'style="font-size:0.8rem; padding:0.4rem 1rem;">'
            f'{TEXTS[L]["btn_github"]}</a>'
        )

        st.markdown(
            f"""
            <div class="{card_class}">
                <span class="project-tag {tag_cls}">{tag_label}</span>
                <div class="project-title">{project["title"]}</div>
                <div class="project-subtitle">{project["subtitle"]}</div>
                <div class="project-desc">{project["desc"]}</div>
                <div class="stack-tags">{stack_html}</div>
                {metrics_html}
                {github_html}
            </div>
            """,
            unsafe_allow_html=True,
        )


# ══════════════════════════════════════════════
# PAGE 4 — CONTACT
# ══════════════════════════════════════════════
elif page == TEXTS[L]["nav_contact"]:

    st.markdown(f'<h1 class="section-title">{TEXTS[L]["contact_title"]}</h1>', unsafe_allow_html=True)
    st.markdown(f'<p class="section-intro">{TEXTS[L]["contact_intro"]}</p>', unsafe_allow_html=True)

    st.markdown(
        f"""
        <div class="contact-grid">
            <a href="mailto:{CONTACT['email']}" class="contact-card">
                <span class="contact-icon">✉️</span>
                <div>
                    <div class="contact-label">Email</div>
                    <div class="contact-value">{CONTACT['email']}</div>
                </div>
            </a>
            <a href="tel:{CONTACT['phone'].replace(' ', '')}" class="contact-card">
                <span class="contact-icon">📞</span>
                <div>
                    <div class="contact-label">{"Téléphone" if L == "fr" else "Phone"}</div>
                    <div class="contact-value">{CONTACT['phone']}</div>
                </div>
            </a>
            <a href="{CONTACT['linkedin_url']}" target="_blank" class="contact-card">
                <span class="contact-icon">💼</span>
                <div>
                    <div class="contact-label">LinkedIn</div>
                    <div class="contact-value">{CONTACT['linkedin_label']}</div>
                </div>
            </a>
            <a href="{CONTACT['github_url']}" target="_blank" class="contact-card">
                <span class="contact-icon">🐙</span>
                <div>
                    <div class="contact-label">GitHub</div>
                    <div class="contact-value">{CONTACT['github_label']}</div>
                </div>
            </a>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div style="text-align:center; margin-top:2rem;">
            <span style="font-size:0.85rem; opacity:0.6;">
                📍 {CONTACT['location_fr'] if L == 'fr' else CONTACT['location_en']}
            </span>
        </div>
        """,
        unsafe_allow_html=True,
    )
