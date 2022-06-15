import discord
from discord.ext import commands
import asyncio

#--------------DEFINITIONS-------------------------------------------------------------
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", case_insensitive=True, intents=intents)
bot.owner_ids = [238834157181075456]
startup_extensions = ["Music",
                      "Commands",
                      "Functions",
                      "Roles"]
#-------------------READY------------------------------------------------------------------------------------------
async def loader():
    if __name__ == "__main__":
        for extension in startup_extensions:
            try:
                await bot.load_extension(extension)
                print(f"{extension} loaded")
            except Exception as e:
                exc = '{}: {}'.format(type(e).__name__, e)
                print('Failed to load extension {}\n{}'.format(extension, exc))

async def main():
    await loader()
    await bot.start('BOT_TOKEN')

asyncio.run(main())
