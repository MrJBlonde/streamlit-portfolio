# 📊 Julien GAUTHIER — Business Analyst Portfolio

CV augmenté interactif & portfolio data.  
Bilingue FR/EN · Dark/Light mode · Déployé sur [Streamlit Community Cloud](https://julien-portfolio.streamlit.app).

## 🚀 Lancer en local

```bash
pip install -r requirements.txt
streamlit run app.py
```

## 📁 Structure

```
streamlit-portfolio/
├── app.py                  # App Streamlit (4 pages)
├── config.py               # Contenu bilingue, projets, contact
├── styles.py               # CSS (Marine & Cuivre, Poppins, dark/light)
├── requirements.txt
├── .streamlit/
│   └── config.toml
├── assets/
│   ├── cv_julien.pdf       # ← CV PDF
│   ├── cv_preview.png      # ← Capture d'écran du CV
│   └── photo_julien.jpg    # ← Photo pro
└── README.md
```

## ✅ Checklist

- [ ] `assets/photo_julien.jpg` — Ta photo pro
- [ ] `assets/cv_julien.pdf` — Ton CV PDF
- [ ] `assets/cv_preview.png` — Screenshot de ton CV (pour l'aperçu)
- [ ] Vérifier les liens GitHub de chaque projet dans `config.py`
- [ ] Déployer sur share.streamlit.io

## 🎨 Design

- **Palette** : Marine #1E3A5F · Cuivre #C47D4E · Crème #FAF7F2
- **Typo** : Poppins (Google Fonts)
- **Modes** : Light & Dark (toggle)

© 2026 Julien GAUTHIER
