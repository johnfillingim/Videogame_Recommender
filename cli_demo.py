"""Standalone CLI demo for the video game recommender.

Run with:
    python cli_demo.py
"""

from api.rawg_api import get_game_recommendations


def main():
    print("=== Video Game Recommender (CLI Demo) ===")
    genre = input("Enter a genre (e.g. action, rpg, indie) or leave blank: ").strip() or None
    games = get_game_recommendations(genre=genre, page_size=5)

    print(f"\nTop {len(games)} results:\n")
    for g in games:
        print(f"- {g['name']} | Rating: {g['rating']} | Released: {g['released']}")


if __name__ == "__main__":
    main()
