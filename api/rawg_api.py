"""RAWG Video Games API wrapper.

Importable:
    from api.rawg_api import get_game_recommendations

Standalone CLI:
    python api/rawg_api.py --genre indie --count 5
"""

import argparse
import os

import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://api.rawg.io/api/games"


def get_game_recommendations(genre=None, platform=None, ordering="-rating", page_size=10):
    """
    Fetch games from RAWG API filtered by genre/platform.

    Args:
        genre: RAWG genre slug (e.g. "action", "rpg", "indie").
        platform: RAWG platform id (e.g. "4" for PC, "187" for PS5).
        ordering: RAWG ordering field, defaults to highest rated first.
        page_size: number of results to return.

    Returns:
        A list of dicts with name, rating, released, image, and genres.
    """
    api_key = os.environ.get("RAWG_API_KEY")
    if not api_key:
        raise ValueError("Missing RAWG_API_KEY environment variable")

    params = {
        "key": api_key,
        "ordering": ordering,
        "page_size": page_size,
    }
    if genre:
        params["genres"] = genre
    if platform:
        params["platforms"] = platform

    response = requests.get(BASE_URL, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()

    games = []
    for g in data.get("results", []):
        games.append({
            "name": g.get("name"),
            "rating": g.get("rating"),
            "released": g.get("released"),
            "image": g.get("background_image"),
            "genres": [genre["name"] for genre in g.get("genres", [])],
        })
    return games


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get game recommendations from RAWG")
    parser.add_argument("--genre", type=str, help="e.g. action, rpg, indie")
    parser.add_argument("--platform", type=str, help="e.g. 4 (PC), 187 (PS5)")
    parser.add_argument("--count", type=int, default=10)
    args = parser.parse_args()

    results = get_game_recommendations(genre=args.genre, platform=args.platform, page_size=args.count)
    for game in results:
        print(f"{game['name']} — ⭐ {game['rating']} — {game['released']}")
