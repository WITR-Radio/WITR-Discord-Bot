from nextcord import FFmpegPCMAudio
import os, asyncio
from dotenv import load_dotenv
from nextcord.ext import commands

load_dotenv()

bot = commands.Bot()

async def music():
    channel = await bot.fetch_channel(os.getenv("UDG_STREAM_CHANNEL"))
    print(channel)
    vc = await channel.connect(reconnect=True)
    vc.play(FFmpegPCMAudio(os.getenv("UDG_STREAM_LINK")))
    await asyncio.sleep(3600)
    print('sleep')
    await vc.disconnect()
    await music()


@bot.event
async def on_ready():   
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    await music()

bot.run(os.getenv("EVIL_WITR_BOT_TOKEN"))   