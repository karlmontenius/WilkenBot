import discord
from discord.ext import commands
import youtube_dl
from youtube_search import YoutubeSearch
import json
from dpymenus import Page, ButtonMenu
from asyncio import sleep



class Music(commands.Cog, description="General commands, such as !slap, and !joke!"):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command(name='Play', brief="Searches for keyword on youtube")
    async def play(self, ctx, keyword):
        one = '1️⃣'
        two = '2️⃣'
        three = '3️⃣'
        stop = '❌'
        ydl_opts = {}
        results = YoutubeSearch(f"{keyword}", max_results=3).to_json()
        parsedJson = json.loads(results)
        parsedUrl1 = parsedJson["videos"][0]["url_suffix"]
        parsedTitle1 = parsedJson["videos"][0]["title"]
        parsedDuration1 = parsedJson["videos"][0]["duration"]
        parsedUrl2 = parsedJson["videos"][1]["url_suffix"]
        parsedTitle2 = parsedJson["videos"][1]["title"]
        parsedDuration2 = parsedJson["videos"][1]["duration"]
        parsedUrl3 = parsedJson["videos"][2]["url_suffix"]
        parsedTitle3 = parsedJson["videos"][2]["title"]
        parsedDuration3 = parsedJson["videos"][2]["duration"]
        
        async def first(menu):
            if menu.button_pressed(one):
                await menu.close()
                url = "https://youtube.com" + parsedUrl1
                await playmusic(self, ctx, url)

            if menu.button_pressed(two):
                await menu.close()
                url = "https://youtube.com" + parsedUrl2
                await playmusic(self, ctx, url)

            if menu.button_pressed(stop):
                await menu.close()

            elif menu.button_pressed(three):
                await menu.close()
                url = "https://youtube.com" + parsedUrl3
                await playmusic(self, ctx, url)

        async def playmusic(self, ctx, url):
            YDL_OPTIONS = {'format': 'bestaudio/best', 'noplaylist':'True'}
            FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
            channel = ctx.author.voice.channel
            if channel != None:
                vc = await channel.connect()
            with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(url, download=False)
                I_URL = info['formats'][0]['url']
                source = await discord.FFmpegOpusAudio.from_probe(I_URL, **FFMPEG_OPTIONS)
                vc.play(source)
                vc.is_playing()

        page1 = Page(title='Song results | Music', description='Which song do you want to play?')
        page1.add_field(name="1 - " + parsedTitle1, value=parsedDuration1, inline=False)
        page1.add_field(name="2 - " + parsedTitle2, value=parsedDuration2, inline=False)
        page1.add_field(name="3 - " + parsedTitle3, value=parsedDuration3, inline=False)
        page1.buttons([one, two, three, stop]).on_next(first)
        menu = ButtonMenu(ctx)
        menu.add_pages([page1])
        await menu.open()

    @commands.command(name='Stop', brief="Searches for keyword on youtube")
    async def stop(self, ctx):
        discord.VoiceClient.pause

def setup(bot):
    bot.add_cog(Music(bot))