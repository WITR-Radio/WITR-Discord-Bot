import os, requests, asyncio
from nextcord import FFmpegPCMAudio
from dotenv import load_dotenv
from nextcord.ext import commands
import snscrape.modules.twitter as twitter
from instabot import Bot

load_dotenv()

bot = commands.Bot()

@bot.event
async def on_ready():   
    #login log message
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    await music()
    # await postinstagram()
    # await posttwitter()

async def music():
    #Music Bot that only plays WITR
    FMchannel = await bot.fetch_channel(os.getenv("FM_STREAM_CHANNEL"))
    print(FMchannel)
    vc = await FMchannel.connect(reconnect=True)
    vc.play(FFmpegPCMAudio(os.getenv("FM_STREAM_LINK")))
    await asyncio.sleep(3600)
    print('sleep')
    await vc.disconnect()
    await music()

async def postinstagram():
    Instachannel = await bot.fetch_channel(os.getenv("INSTAGRAM_CHANNEL_ID"))
    instabot = Bot()
    instabot.login(username=os.getenv("INSTAGRAM_USERNAME"), password=os.getenv("INSTAGRAM_PASSWORD"))
    posts = instabot.get_user_feed(os.getenv("INSTAGRAM_TARGET_USER"))

    latest_post = posts[0]
    await Instachannel.send(f"{latest_post['thumbnail_url']}: {latest_post['link']}")

    bot.logout()

    await asyncio.sleep(3600) # refresh every hour
    await postinstagram() 

async def posttwitter():
    return

bot.run(os.getenv("WITR_BOT_TOKEN"))   