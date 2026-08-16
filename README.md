# 🎮 Video Game Recommender

A Streamlit web app that recommends video games by genre using the [RAWG Video Games API](https://rawg.io/apidocs). Includes a standalone CLI demo and a reusable API module. Deployed live on Hugging Face Spaces, mirrored from this public GitHub repo.

**Live demo:** [Hugging Face Space](https://huggingface.co/spaces/YOUR_HF_USERNAME/YOUR_SPACE_NAME) _(update this link after deploying)_

![Demo](assets/demo.gif)
_(add `assets/demo.gif` showing the app in action)_

## Features

- Pick a genre and a result count, get live recommendations from RAWG
- Bar chart comparing ratings across results
- Game cover images and metadata (rating, release date, genres)
- API layer usable on its own from the command line

## Project structure

```
video-game-recommender/
├── README.md
├── requirements.txt
├── cli_demo.py
├── app.py                 # Streamlit UI
├── api/
│   └── rawg_api.py        # standalone-usable API module
├── utils/
│   └── helpers.py         # formatting helpers
├── .env.example            # documents expected env var, no real key
├── .gitignore              # excludes .env
└── assets/
    └── demo.gif            # for README
```

## Requirements

- Python 3.11
- A free RAWG API key: https://rawg.io/apidocs

## Setup

1. Clone the repo and install dependencies:

   ```bash
   git clone https://github.com/johnfillingim/video-game-recommender.git
   cd video-game-recommender
   pip install -r requirements.txt
   ```

2. Copy `.env.example` to `.env` and add your RAWG API key:

   ```bash
   cp .env.example .env
   # then edit .env and set RAWG_API_KEY=your_actual_key
   ```

## Run locally (Streamlit app)

```bash
streamlit run app.py
```

Open the URL Streamlit prints (usually `http://localhost:8501`).

## Run the CLI demo

```bash
python cli_demo.py
```

You'll be prompted for a genre, then shown the top 5 matching games.

The API module can also be run standalone with arguments:

```bash
python api/rawg_api.py --genre indie --count 5
```

## Deployment (Hugging Face Spaces)

This repo is mirrored to a Hugging Face Space so the app runs live. The RAWG API key is stored as an HF **Repository secret** (`RAWG_API_KEY`) — never committed to the repo.

**Sync approach:** _(document whichever your team uses)_

- **Manual mirror push** — after merging to `main` on GitHub, push the same commit to the HF Space's git remote:
  ```bash
  git push https://huggingface.co/spaces/YOUR_HF_USERNAME/YOUR_SPACE_NAME main
  ```
- **GitHub Actions auto-sync** — a workflow pushes to the HF Space on every push to `main`, using an HF write token stored as a GitHub Actions secret.

## Notes

- No API secrets are hard-coded anywhere in this repo. Locally, the key comes from `.env` (gitignored); on Hugging Face Spaces, it comes from Repository secrets.
- Deactivate the RAWG API key after the course/assignment ends.
