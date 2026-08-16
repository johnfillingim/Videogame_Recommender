"""Streamlit UI for the video game recommender."""

import pandas as pd
import streamlit as st
from dotenv import load_dotenv

from api.rawg_api import get_game_recommendations

load_dotenv()

st.set_page_config(page_title="Game Recommender", page_icon="🎮")
st.title("🎮 Video Game Recommender")

genres = ["action", "rpg", "indie", "strategy", "shooter", "puzzle", "adventure", "sports"]
genre = st.selectbox("Pick a genre", genres)
count = st.slider("How many recommendations?", 5, 20, 10)

if st.button("Get Recommendations"):
    with st.spinner("Fetching games..."):
        games = get_game_recommendations(genre=genre, page_size=count)

    if not games:
        st.warning("No games found for that genre. Try another one.")
    else:
        df = pd.DataFrame(games)
        st.subheader("Ratings comparison")
        st.bar_chart(df.set_index("name")["rating"])

        st.subheader("Top picks")
        for g in games:
            col1, col2 = st.columns([1, 3])
            with col1:
                if g["image"]:
                    st.image(g["image"], width=120)
            with col2:
                st.markdown(f"**{g['name']}**")
                st.markdown(f"⭐ {g['rating']} · Released: {g['released']}")
                st.markdown(f"Genres: {', '.join(g['genres'])}")
            st.divider()
