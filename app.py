from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Three Uluses", layout="wide")

# Прячем меню, шапку и подвал Streamlit, убираем отступы вокруг страницы
st.markdown(
    """
    <style>
      #MainMenu, header, footer {visibility: hidden;}
      .block-container {padding: 0 !important; max-width: 100% !important;}
      iframe {display: block;}
    </style>
    """,
    unsafe_allow_html=True,
)

html = Path(__file__).with_name("index33.html").read_text(encoding="utf-8")

# Страница прокручивается внутри окна, поэтому шапка с таймером остаётся закреплённой
components.html(html, height=950, scrolling=True)
