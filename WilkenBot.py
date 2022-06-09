import discord
from discord.ext import commands
import asyncio
#from pretty_help import DefaultMenu, PrettyHelp

#--------------DEFINITIONS-------------------------------------------------------------
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", case_insensitive=True, intents=intents)
bot.owner_ids = [238834157181075456]
startup_extensions = ["Commands",
                      "Music"]

# menu = DefaultMenu('◀️', '▶️', '❌')
# bot.help_command = PrettyHelp(navigation=menu, color=discord.Colour.green()) 
#-------------------READY------------------------------------------------------------------------------------------
async def loader():
    if __name__ == "__main__":
        for extension in startup_extensions:
            try:
                await bot.load_extension(extension)
                print("loaded")
            except Exception as e:
                exc = '{}: {}'.format(type(e).__name__, e)
                print('Failed to load extension {}\n{}'.format(extension, exc))

async def main():
    await loader()
    async with bot:
        await bot.start('OTY2Njc5NDcwMjU5OTY2MDky.YmFQaQ.MDXz8e7dz5-leNdpOZrZrPSEqCU')

asyncio.run(main())