import streamlit as st

st.set_page_config(page_title="Bad Bunny", page_icon="🎶")

st.title("🐰 Bad Bunny Project")
st.write("""
Este proyecto está dedicado a **Bad Bunny**, uno de los artistas más influyentes de la música urbana y el reguetón.
Aquí encontrarás información sobre su biografía, discografía y un análisis de sus logros.
""")

st.image(
    "https://upload.wikimedia.org/wikipedia/commons/f/fb/Bad_Bunny_2019.png",
    caption="Bad Bunny en concierto",
    use_container_width=True
)
