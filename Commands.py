import discord
from discord.ext import commands
from discord.utils import get
from os import chdir, listdir, path
from discord import File
import random
import datetime

#--------------DEFINITIONS-------------------------------------------------------------
jokes = [
        "What's the difference  between Windows 95 and a virus? A virus does something.",
        "What's the speed limit of sex? 68; at 69 you have to turn around.",
        "What did the egg say to the  boiling water? ""How can you expect me to get hard so fast? I just got laid a minute ago.""",
        "What do computers eat when they get hungry?  Chips.",
        "What's the difference between Windows 95 and a virus? A virus does something.",
        "What is uglier than an aardvark? Two aardvarks!",
        "What does the aardvark call his dog? Aard-bark!",
        "What is the difference between an aardvark and a coyote? One has a long smeller the other a loud yeller!",
        "Who loves hamburgers French fries and ants? Ronald MacAardvark!",
        "What does an aardvark keep in his aquarium? An aard-shark!",
        "What will fall on the lawn first? An  autumn leaf or a Christmas catalogue?",
        "Do steam rollers really roll  steam?",
        "Why do you need a driver's licence to buy liquor when you can't drink and drive?",
        "Why is it that when you transport something by car it's called ship-ment but when you transport something by ship it's called cargo?",
        "Why do accountants make good lovers? They're great with figures.",
        "Why don't anteaters get sick ? Because they are full of antibodies!",
        "Why did the ant-elope ? Nobody gnu !",
        "Who is the most famous French ant ? Napoleant !",
        "What do you call an and with frogs legs ? An antphibian !",
        "What do you call an ant who can't play the piano ? Discordant !",
        "What did one maggot say to the other who was stuck in an apple? Worm your way out of that one then!",
        "Why didn't the two worms go into Noah's ark in an apple? Because everyone had to go in pairs !",
        "What lives in apples and is an avid reader?  A bookworm !",
        "First apple: You look down in the dumps. What's eating you? Second apple: Worms I think.",
        "Why are bananas never lonely? Because they hang around in bunches.",
        "How do you catch King Kong? Hang upside down and make a noise like a banana.",
        "Time flies like an arrow but fruit flies like a banana.",
        "Tom: What did the banana say to the elephant?  Nick: I don't know. Tom: Nothing. Bananas can't talk.",
        "Mandy: Our teacher went on a special banana diet. Andy: Did she lose weight? Mandy: No but she sure could climb trees well!",
        "What does a baby computer call his father? Data.",
]
Hugs = path.join(path.dirname(__file__), "images/")
hug_list = [Hugs + h for h in listdir(Hugs)]
Slaps = path.join(path.dirname(__file__), "slapimages/")
slap_list = [Slaps + s for s in listdir(Slaps)]
class Commands(commands.Cog, description="General commands, such as !slap, and !joke!"):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None


#---------HUG-----------------------------------------------------------------------------------
    @commands.command(name='Hug', brief="Sends a hug to a user!")
    async def hug(self, ctx, *, member: discord.Member):
        user = ctx.author
        choice = random.choice
        await ctx.send(file=File((choice(hug_list))))
    
    @hug.error
    async def verify_error(self, ctx, param):
        if isinstance(param, commands.errors.MissingRequiredArgument):
            await ctx.send("You need to specify who to hug!")
    
    #---------SLAP-------------------------------------------------------------------------------
    @commands.command(name='Slap', brief='Slap the mentioned user!')
    async def slap(self, ctx, *, member: discord.Member):
        choice = random.choice
        await ctx.send(file=File((choice(slap_list))))
    
    @slap.error
    async def verify_error(self, ctx, param):
        if isinstance(param, commands.errors.MissingRequiredArgument):
            await ctx.send("You need to specify who to slap!")
    
    #---------ROLL-------------------------------------------------------------------------------
    @commands.command(name='Roll', brief='Rolls a random number between 1-100')
    async def roll(self, ctx):
        choice = random.choice
        number = choice(range(101))
        embed = discord.Embed(title="Roll | MiniBot", description=f"{ctx.author.mention} rolled {number}")
        await ctx.send(embed=embed)
    
    #---------FLIP-------------------------------------------------------------------------------
    @commands.command(name='Flip', brief="Flips a coin resulting in heads or tails.")
    async def coinflip(self, ctx):
        choice = random.choice
        determine_flip = [1, 0]
        if choice(determine_flip) == 1:
            embed = discord.Embed(title="Coinflip | MiniBot", description=f"{ctx.author.mention} flipped a coin, and got **Heads**!")
            await ctx.send(embed=embed)
    
        else:
            embed = discord.Embed(title="Coinflip | MiniBot", description=f"{ctx.author.mention} flipped a coin, and got **Tails**!")
            await ctx.send(embed=embed)
    
    #----------PURGE-------------------------------------------------------------------------------
    @commands.command(name='Purge', brief="Removes all messages sent by the userID provided.")
    @commands.has_any_role('Admin', 'Mod', 'Senior Mod')
    async def purge(self, ctx, member: discord.Member):
        msg = []
        counter = 0
        for channel in ctx.guild.text_channels:
            async for message in channel.history(limit = 100):
                if message.author == member:
                    msg.append(message)
                    counter += 1
                    await message.delete()
        await ctx.send(f'Deleted **{counter}** messages in this server.{ctx.author.mention}')
    
    @purge.error
    async def purgemember_error(self, ctx, error):
        if isinstance(error, commands.errors.MemberNotFound):
            await ctx.send("No member found with that ID!")
    
    @purge.error
    async def purgerank_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingAnyRole):
            await ctx.send("You are not authorized to use this command!")
    
    
    #----------JOKE--------------------------------------------------------------
    @commands.cooldown(1, 90, commands.BucketType.guild)
    @commands.command(name='Joke', brief='Tells a random joke.')
    async def joke(self, ctx,):
        joke = random.choice(jokes)
        await ctx.send(f"{joke}")
    
    @joke.error
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            remaining_time = str(datetime.timedelta(seconds=int(error.retry_after)))
            embed = discord.Embed(title=":clock1: Cooldown!", description=f'I just told a joke. I can tell one again in ' + str(remaining_time), color=0xE74C3C)
            await ctx.send(embed=embed)

    #---------GIVE ROLES-------------------------------------------------------------------
    @commands.command()
    async def menu(self, ctx):
        Overwatch = get(ctx.guild.roles, name="Overwatch")
        League = get(ctx.guild.roles, name="League of Legends")
        Elden = get(ctx.guild.roles, name="Elden Ring")
        Arma = get(ctx.guild.roles, name="Arma Reforger")
        class Select(discord.ui.Select):
            def __init__(self):
                options=[
                    discord.SelectOption(label="League of Legends"),
                    discord.SelectOption(label="Overwatch"),
                    discord.SelectOption(label="Arma Reforger"),
                    discord.SelectOption(label="Elden Ring")
                    ]
                super().__init__(placeholder="Select your role",max_values=1,min_values=1,options=options)

            async def callback(self, interaction: discord.Interaction):
                await interaction.response.send_message(content=f"You have selected {self.values[0]}!",ephemeral=True)
                print(self.values[0])
                user = interaction.user
                if self.values[0] == "League of Legends":
                    if Overwatch in user.roles:
                        await user.remove_roles(League)
                        print("Removed")
                    else:
                        await user.add_roles(League)
                        print(user.roles)
                        print("Added")
                if self.values[0] == "Overwatch":
                    if Overwatch in user.roles:
                        await user.remove_roles(Overwatch)
                        print("Removed")
                    else:
                        await user.add_roles(Overwatch)
                        print(user.roles)
                        print("Added OW")
                if self.values[0] == "Elden Ring":
                    if Elden in user.roles:
                        await user.remove_roles(Elden)
                        print("Removed")
                    else:
                        await user.add_roles(Elden)
                        print(user.roles)
                        print("Added")
                if self.values[0] == "Arma Reforger":
                    if Arma in user.roles:
                        await user.remove_roles(Arma)
                        print("Removed")
                    else:
                        await user.add_roles(Arma)
                        print(user.roles)
                        print("Added")

        class SelectView(discord.ui.View):
            def __init__(self, *, timeout = 180):
                super().__init__(timeout=timeout)
                self.add_item(Select())

        await ctx.send("Choose your role!",view=SelectView())

async def setup(bot):
    await bot.add_cog(Commands(bot))