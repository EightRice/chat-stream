import asyncio
from typing import AsyncGenerator, Optional
import re

# We use pytchat for YouTube and twitchio for Twitch
try:
    import pytchat
except ImportError:
    pytchat = None

try:
    from twitchio.ext import commands
except ImportError:
    commands = None

YOUTUBE_REGEX = re.compile(r"(?:youtube\.com/watch\?v=|youtu\.be/)([\w-]+)")
TWITCH_REGEX = re.compile(r"twitch\.tv/([\w-]+)")

async def youtube_chat(video_id: str) -> AsyncGenerator[str, None]:
    if pytchat is None:
        raise RuntimeError("pytchat not installed")
    chat = pytchat.create(video_id=video_id)
    while chat.is_alive():
        for c in chat.get().items:
            yield c.message
        await asyncio.sleep(0.5)

class TwitchBot(commands.Bot):
    def __init__(self, channel: str, token: str):
        super().__init__(token=token, prefix='!', initial_channels=[channel])
        self.queue = asyncio.Queue()

    async def event_message(self, message):
        if message.echo:
            return
        await self.queue.put(message.content)

async def twitch_chat(channel: str, token: str) -> AsyncGenerator[str, None]:
    if commands is None:
        raise RuntimeError("twitchio not installed")
    bot = TwitchBot(channel, token)
    asyncio.create_task(bot.start())
    while True:
        msg = await bot.queue.get()
        yield msg

async def from_url(url: str, twitch_token: Optional[str] = None) -> AsyncGenerator[str, None]:
    yt_match = YOUTUBE_REGEX.search(url)
    if yt_match:
        return youtube_chat(yt_match.group(1))
    tw_match = TWITCH_REGEX.search(url)
    if tw_match:
        if not twitch_token:
            raise RuntimeError("Twitch token required")
        return twitch_chat(tw_match.group(1), twitch_token)
    raise ValueError("Unsupported URL")
