import discord
from discord.ext import commands
from pretty_help import DefaultMenu, PrettyHelp

#--------------DEFINITIONS-------------------------------------------------------------
bot = commands.Bot(command_prefix="!", case_insensitive=True)
bot.owner_ids = [238834157181075456]
startup_extensions = ["Commands",
                      "Music"]

menu = DefaultMenu('◀️', '▶️', '❌')
bot.help_command = PrettyHelp(navigation=menu, color=discord.Colour.green()) 
#-------------------READY------------------------------------------------------------------------------------------
if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    await bot.change_presence(activity=discord.Game(name="Made by: MiniMonty"))

#-------START----------------------------------------------------------------------------------
bot.run('OTY2Njc5NDcwMjU5OTY2MDky.YmFQaQ.MDXz8e7dz5-leNdpOZrZrPSEqCU')