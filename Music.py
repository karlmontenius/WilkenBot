import discord
from discord.ext import commands
import youtube_dl
from youtube_search import YoutubeSearch
import json
from dpymenus import Page, ButtonMenu
import datetime

secs = 0
songs = 0
vc = ()
queue = []

class Music(commands.Cog, description="Commands that control the music from the bot."):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    @commands.command(name='Connect', aliases=["c"], brief="Makes the bot join vc")
    async def connect(self, ctx):
        channel = ctx.author.voice.channel
        global vc
        if channel != None:
            vc = await channel.connect()

    @commands.command(name='Play', brief="Search for the song that you want to play.")
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

        async def playmusic(self, ctx, url, duration):
            YDL_OPTIONS = {'format': 'bestaudio/best', 'noplaylist':'True'}
            FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
            global vc
            global queue
            with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(url, download=False)
                I_URL = info['formats'][0]['url']
                title = info['title']
                embed = discord.Embed(title="Now playing", description="")
                embed.add_field(name="Title", value=title, inline=False)
                embed.add_field(name='Duration', value=duration, inline=False)
                embed.set_footer(text=f"Queued by: {ctx.author}")
                source = await discord.FFmpegOpusAudio.from_probe(I_URL, **FFMPEG_OPTIONS)
                if vc.is_playing():
                    queue.append(I_URL)
                    global secs
                    global songs
                    songs += 1
                    ts = duration
                    secs += sum(int(x) * 60 ** i for i, x in enumerate(reversed(ts.split(':'))))
                    totalduration = (datetime.timedelta(seconds=secs))
                    embedq = discord.Embed(title="Queue", description="")
                    embedq.add_field(name="Added to queue", value=title, inline=False)
                    embedq.add_field(name="Songs in queue", value=songs, inline=False)
                    embedq.add_field(name='Queue time', value=totalduration, inline=False)
                    embedq.set_footer(text=f"Command run by: {ctx.author}")
                    print(queue)
                    await ctx.send(embed=embedq)
                else:
                    vc.play(source)
                    vc.is_playing()
                    await ctx.send(embed=embed)

        async def first(menu):
            if menu.button_pressed(one):
                await menu.close()
                url = "https://youtube.com" + parsedUrl1
                duration = parsedDuration1
                await playmusic(self, ctx, url, duration)

            if menu.button_pressed(two):
                await menu.close()
                url = "https://youtube.com" + parsedUrl2
                duration = parsedDuration2
                await playmusic(self, ctx, url, duration)

            if menu.button_pressed(stop):
                await menu.close()

            elif menu.button_pressed(three):
                await menu.close()
                url = "https://youtube.com" + parsedUrl3
                duration = parsedDuration3
                await playmusic(self, ctx, url, duration)

        page1 = Page(title='Song results | Music', description='Which song do you want to play?')
        page1.add_field(name="1 - " + parsedTitle1, value=parsedDuration1, inline=False)
        page1.add_field(name="2 - " + parsedTitle2, value=parsedDuration2, inline=False)
        page1.add_field(name="3 - " + parsedTitle3, value=parsedDuration3, inline=False)
        page1.buttons([one, two, three, stop]).on_next(first)
        menu = ButtonMenu(ctx)
        menu.add_pages([page1])
        await menu.open()

    @commands.command(name='Pause', aliases=["p"], brief="Pauses music in vc.")
    async def pause(self, ctx):
        global vc
        vc.pause()
        vc.is_paused()

    @commands.command(name='Resume', aliases=["r"], brief="Resumes playing music in vc.")
    async def resume(self, ctx):
        global vc
        vc.resume()
        vc.is_playing()

    @commands.command(name='Disconnect',aliases=["dc"], brief="Disconnects the bot from current vc.")
    async def disconnect(self, ctx):
        global vc
        await vc.disconnect()

    @commands.command(name='Skip',aliases=["s"], brief="Skips the current song playing.")
    async def skip(self, ctx):
        global vc
        vc.stop()
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        source = await discord.FFmpegOpusAudio.from_probe(queue[0], **FFMPEG_OPTIONS)
        del queue[0]
        vc.play(source)
        vc.is_playing()
        await ctx.send("Skipped current song, playing next song in queue.")

async def setup(bot):
    await bot.add_cog(Music(bot))