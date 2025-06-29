# Chat Stream

A minimal demo that summarizes live chat messages from YouTube or Twitch. It collects chat messages, generates a short rolling summary with sentiment, and displays the result in a small Streamlit dashboard.

## Features

- Fetch chat messages from a YouTube or Twitch livestream
- Two‑sentence summary computed with a lightweight LSA model
- Average sentiment using VADER
- Confidence score based on message repetition
- Streamlit UI showing the latest message, summary and sentiment bar

## Project Layout

```
src/chatstream/
    __init__.py
    ingest.py     # utilities for fetching live chat
    summarize.py  # rolling summarization logic
streamlit_app.py  # Streamlit dashboard
tests/            # small unit tests
```

## Quick Start

1. Install dependencies:
   ```bash
   pip install streamlit pytchat twitchio nltk sumy
   ```
   NLTK will download some data on first run.
2. Launch the dashboard:
   ```bash
   streamlit run streamlit_app.py
   ```
3. Paste a live YouTube or Twitch URL and (for Twitch) an OAuth token.

Run `pytest` to execute the unit tests.
