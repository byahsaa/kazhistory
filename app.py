from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="KazHistory", page_icon="📜", layout="wide")

st.markdown(
    "<style>#MainMenu,header,footer{visibility:hidden}"
    ".block-container{padding:0!important;max-width:100%!important}</style>",
    unsafe_allow_html=True,
)

here = Path(__file__).parent
for name in ("index.html", "index33.html"):
    page = here / name
    if page.exists():
        components.html(page.read_text(encoding="utf-8"), height=950, scrolling=True)
        break
else:
    st.error("index.html not found in the repository.")
