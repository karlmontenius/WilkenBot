import discord
from discord.ext import commands
from discord.utils import get
intents = discord.Intents.all()
client = discord.Client(intents = intents)

class Functions(commands.Cog, description="Functions."):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None


    @client.event
    async def on_member_join(self, ctx, member):
        colors = get(ctx.guild.roles, id=985612750145351720)
        games = get(ctx.guild.roles, id=985612805262696458)
        await member.add_roles(colors)
        await member.add_roles(games)


async def setup(bot):
    await bot.add_cog(Functions(bot))