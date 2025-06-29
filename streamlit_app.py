import asyncio
import streamlit as st
from chatstream.ingest import from_url
from chatstream.summarize import RollingSummary

st.set_page_config(page_title="Chat Stream", layout="wide")

st.title("Chat Stream – Live Summary")
url = st.text_input("YouTube or Twitch URL")
twitch_token = st.text_input("Twitch OAuth Token", type="password")
start = st.button("Start")

placeholder = st.empty()
summary_box = st.empty()
sentiment_bar = st.progress(0.0)
conf_box = st.empty()

async def run():
    summary = RollingSummary()
    if not url:
        st.warning("Enter a URL to start")
        return
    gen = await from_url(url, twitch_token if twitch_token else None)
    async for msg in gen:
        summary.add(msg)
        head, sentiment, conf = summary.compute()
        placeholder.markdown(f"**Latest:** {msg}")
        size = 1 + conf * 2
        summary_box.markdown(f"<div style='font-size:{size}em'>{head}</div>", unsafe_allow_html=True)
        sentiment_bar.progress((sentiment + 1) / 2)
        conf_box.markdown(f"Confidence: {conf:.2f}")

if start:
    asyncio.run(run())
