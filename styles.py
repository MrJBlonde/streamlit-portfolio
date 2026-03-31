import streamlit as st


def inject_custom_css(dark_mode=False):
    if dark_mode:
        bg = "#0E1F33"
        bg_card = "#162B45"
        text = "#E8E0D4"
        text_muted = "#9AABBF"
        accent = "#C47D4E"
        accent_hover = "#D99A6C"
        border = "#253D58"
        sidebar_bg = "#0A1628"
        sidebar_text = "#C9D6E3"
        tag_bg = "#253D58"
    else:
        bg = "#FAF7F2"
        bg_card = "#FFFFFF"
        text = "#1E3A5F"
        text_muted = "#5A6E82"
        accent = "#C47D4E"
        accent_hover = "#A8643A"
        border = "#E4DDD3"
        sidebar_bg = "#1E3A5F"
        sidebar_text = "#D4E5F7"
        tag_bg = "#F0EBE3"

    st.markdown(
        f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

        html, body, [class*="st-"] {{
            font-family: 'Poppins', sans-serif !important;
        }}

        .stApp {{
            background: {bg};
        }}

        /* ── Hero ───────────────────────────── */
        .hero-hello {{
            font-size: 1.1rem;
            color: {text_muted};
            font-weight: 400;
            margin-bottom: 0;
        }}

        .hero-name {{
            font-family: 'Poppins', sans-serif !important;
            font-weight: 700;
            font-size: 2.8rem;
            color: {text};
            margin: 0;
            letter-spacing: -0.02em;
            line-height: 1.1;
        }}

        .hero-title {{
            font-family: 'Poppins', sans-serif !important;
            font-weight: 500;
            font-size: 1.15rem;
            color: {accent};
            margin-top: 0.3rem;
            margin-bottom: 0.8rem;
        }}

        .hero-pitch {{
            font-size: 0.95rem;
            color: {text_muted};
            line-height: 1.7;
            max-width: 600px;
        }}

        /* ── Section titles ─────────────────── */
        .section-title {{
            font-family: 'Poppins', sans-serif !important;
            font-weight: 600;
            font-size: 1.6rem;
            color: {text};
            margin-top: 1rem;
            margin-bottom: 0.3rem;
        }}

        .section-intro {{
            font-size: 0.95rem;
            color: {text_muted};
            margin-bottom: 1.5rem;
        }}

        /* ── Divider ────────────────────────── */
        .divider {{
            height: 1px;
            background: linear-gradient(90deg, transparent, {border}, transparent);
            margin: 2rem 0;
        }}

        /* ── CTA buttons ────────────────────── */
        .cta-row {{
            display: flex;
            gap: 0.8rem;
            flex-wrap: wrap;
            margin-top: 1.2rem;
        }}

        .cta-btn {{
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
            padding: 0.6rem 1.3rem;
            border-radius: 8px;
            font-family: 'Poppins', sans-serif;
            font-weight: 500;
            font-size: 0.85rem;
            text-decoration: none !important;
            transition: all 0.2s ease;
        }}

        .cta-primary {{
            background: {accent};
            color: #FFFFFF !important;
            border: none;
        }}

        .cta-primary:hover {{
            background: {accent_hover};
            transform: translateY(-2px);
            box-shadow: 0 4px 16px rgba(196,125,78,0.3);
        }}

        .cta-secondary {{
            background: transparent;
            color: {accent} !important;
            border: 2px solid {accent};
        }}

        .cta-secondary:hover {{
            background: {accent};
            color: #FFFFFF !important;
            transform: translateY(-2px);
        }}

        /* ── Soft skill cards ───────────────── */
        .soft-grid {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 12px;
            margin-top: 1rem;
        }}

        .soft-card {{
            background: {bg_card};
            border-radius: 10px;
            padding: 1.1rem;
            border: 1px solid {border};
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }}

        .soft-card:hover {{
            transform: translateY(-3px);
            box-shadow: 0 6px 20px rgba(0,0,0,0.08);
        }}

        .soft-icon {{
            font-size: 1.5rem;
            margin-bottom: 0.4rem;
        }}

        .soft-name {{
            font-weight: 600;
            font-size: 0.85rem;
            color: {text};
            margin-bottom: 0.2rem;
        }}

        .soft-desc {{
            font-size: 0.75rem;
            color: {text_muted};
            line-height: 1.4;
        }}

        /* ── Project cards ──────────────────── */
        .project-card {{
            background: {bg_card};
            border-radius: 12px;
            padding: 1.4rem;
            border: 1px solid {border};
            margin-bottom: 1rem;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }}

        .project-card:hover {{
            transform: translateY(-3px);
            box-shadow: 0 8px 24px rgba(0,0,0,0.08);
        }}

        .project-card-flagship {{
            background: {bg_card};
            border-radius: 12px;
            padding: 1.4rem;
            border: 2px solid {accent};
            margin-bottom: 1rem;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }}

        .project-card-flagship:hover {{
            transform: translateY(-3px);
            box-shadow: 0 8px 24px rgba(196,125,78,0.15);
        }}

        .project-tag {{
            display: inline-block;
            padding: 2px 10px;
            border-radius: 20px;
            font-size: 0.65rem;
            font-weight: 600;
            letter-spacing: 0.05em;
            margin-bottom: 0.5rem;
        }}

        .tag-flagship {{
            background: {accent};
            color: #FFFFFF;
        }}

        .tag-perso {{
            background: {tag_bg};
            color: {accent};
        }}

        .tag-formation {{
            background: {tag_bg};
            color: {text_muted};
        }}

        .project-title {{
            font-weight: 600;
            font-size: 1.05rem;
            color: {text};
            margin-bottom: 0.15rem;
        }}

        .project-subtitle {{
            font-size: 0.8rem;
            color: {text_muted};
            margin-bottom: 0.6rem;
        }}

        .project-desc {{
            font-size: 0.85rem;
            color: {text_muted};
            line-height: 1.6;
            margin-bottom: 0.8rem;
        }}

        .stack-tags {{
            display: flex;
            flex-wrap: wrap;
            gap: 0.4rem;
            margin-bottom: 0.8rem;
        }}

        .stack-tag {{
            background: {tag_bg};
            color: {text_muted};
            padding: 2px 8px;
            border-radius: 4px;
            font-size: 0.7rem;
            font-weight: 500;
        }}

        .metrics-row {{
            display: flex;
            gap: 1rem;
            flex-wrap: wrap;
            margin-bottom: 0.8rem;
        }}

        .metric-item {{
            text-align: center;
        }}

        .metric-val {{
            font-weight: 700;
            font-size: 1.1rem;
            color: {accent};
        }}

        .metric-lbl {{
            font-size: 0.65rem;
            color: {text_muted};
        }}

        /* ── Contact cards ──────────────────── */
        .contact-grid {{
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 12px;
            margin-top: 1rem;
        }}

        .contact-card {{
            display: flex;
            align-items: center;
            gap: 12px;
            background: {bg_card};
            border-radius: 10px;
            padding: 1rem 1.2rem;
            border: 1px solid {border};
            text-decoration: none !important;
            color: {text} !important;
            transition: transform 0.2s ease, border-color 0.2s ease;
        }}

        .contact-card:hover {{
            transform: translateY(-2px);
            border-color: {accent};
        }}

        .contact-icon {{
            font-size: 1.3rem;
        }}

        .contact-label {{
            font-size: 0.75rem;
            color: {text_muted};
        }}

        .contact-value {{
            font-size: 0.9rem;
            font-weight: 500;
            color: {text};
        }}

        /* ── CV preview ─────────────────────── */
        .cv-preview-container {{
            background: {bg_card};
            border-radius: 12px;
            padding: 1rem;
            border: 1px solid {border};
            text-align: center;
        }}

        /* ── Photo ──────────────────────────── */
        .photo-placeholder {{
            width: 150px;
            height: 150px;
            border-radius: 50%;
            background: linear-gradient(135deg, #1E3A5F, #2C5282);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 42px;
            color: #FAF7F2;
            font-weight: 600;
            font-family: 'Poppins', sans-serif;
            border: 4px solid {accent};
        }}

        /* ── Download button override ───────── */
        .stDownloadButton > button {{
            background-color: {accent} !important;
            color: #FFFFFF !important;
            border: none !important;
            border-radius: 8px !important;
            font-family: 'Poppins', sans-serif !important;
            font-weight: 500 !important;
            padding: 0.5rem 1.5rem !important;
            transition: all 0.2s ease !important;
        }}

        .stDownloadButton > button:hover {{
            background-color: {accent_hover} !important;
            box-shadow: 0 4px 16px rgba(196,125,78,0.3) !important;
        }}

        /* ── Sidebar ────────────────────────── */
        section[data-testid="stSidebar"] {{
            background: {sidebar_bg} !important;
        }}

        section[data-testid="stSidebar"] * {{
            color: {sidebar_text} !important;
        }}

        section[data-testid="stSidebar"] .stRadio label {{
            font-weight: 500 !important;
        }}

        section[data-testid="stSidebar"] hr {{
            border-color: rgba(255,255,255,0.1) !important;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )
