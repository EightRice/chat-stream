import asyncio
import pytest
from chatstream import ingest

@pytest.mark.asyncio
async def test_from_url_youtube():
    gen = await ingest.from_url("https://www.youtube.com/watch?v=abc123")
    assert hasattr(gen, "__anext__")

@pytest.mark.asyncio
async def test_from_url_twitch_requires_token():
    with pytest.raises(RuntimeError):
        await ingest.from_url("https://twitch.tv/somechan")
