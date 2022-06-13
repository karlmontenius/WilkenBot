import discord
from discord.ext import commands
from discord.utils import get

class Roles(commands.Cog, description="Supportive cog for roles."):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

#---------------------------------------------------------------------------------------------------------------------------
    async def roles(self, ctx):
        Overwatch = get(ctx.guild.roles, name="Overwatch")
        League = get(ctx.guild.roles, name="League of Legends")
        Elden = get(ctx.guild.roles, name="Elden Ring")
        Arma = get(ctx.guild.roles, name="Arma Reforger")
        CSGO = get(ctx.guild.roles, name="Counter Strike: Global Offensive")
        channel = get(ctx.guild.text_channels, name="get-your-roles")
        class Select(discord.ui.Select):
            def __init__(self):
                options=[
                    discord.SelectOption(label="League of Legends"),
                    discord.SelectOption(label="Overwatch"),
                    discord.SelectOption(label="Arma Reforger"),
                    discord.SelectOption(label="Elden Ring"),
                    discord.SelectOption(label="Counter Strike: Global Offensive")
                    ]
                super().__init__(placeholder="Select your roles!",max_values=1,min_values=1,options=options)

            async def callback(self, interaction: discord.Interaction):
                user = interaction.user
                if self.values[0] == "League of Legends":
                    if Overwatch in user.roles:
                        await user.remove_roles(League)
                        await interaction.response.send_message(content="Removed League of Legends!", ephemeral=True)
                    else:
                        await user.add_roles(League)
                        await interaction.response.send_message(content="Added League of Legends!", ephemeral=True)

                if self.values[0] == "Overwatch":
                    if Overwatch in user.roles:
                        await user.remove_roles(Overwatch)
                        await interaction.response.send_message(content="Removed Overwatch!", ephemeral=True)
                    else:
                        await user.add_roles(Overwatch)
                        await interaction.response.send_message(content="Added Overwatch!", ephemeral=True)

                if self.values[0] == "Elden Ring":
                    if Elden in user.roles:
                        await user.remove_roles(Elden)
                        await interaction.response.send_message(content="Removed Elden Ring!", ephemeral=True)
                    else:
                        await user.add_roles(Elden)
                        await interaction.response.send_message(content="Added Elden Ring!", ephemeral=True)

                if self.values[0] == "Arma Reforger":
                    if Arma in user.roles:
                        await user.remove_roles(Arma)
                        await interaction.response.send_message(content="Removed Arma Reforger!", ephemeral=True)
                    else:
                        await user.add_roles(Arma)
                        await interaction.response.send_message(content="Added Arma Reforger!", ephemeral=True)

                if self.values[0] == "Counter Strike: Global Offensive":
                    if CSGO in user.roles:
                        await user.remove_roles(CSGO)
                        await interaction.response.send_message(content="Removed Counter Strike: Global Offensive!", ephemeral=True)
                    else:
                        await user.add_roles(CSGO)
                        await interaction.response.send_message(content="Added Counter Strike: Global Offensive!", ephemeral=True)
                         
        class SelectView(discord.ui.View):
            def __init__(self, *, timeout=180):
                super().__init__(timeout=timeout)
                self.add_item(Select())

        await channel.send(content="Choose your role!",view=SelectView())

#-----------------------------------------------------------------------------------------------------------------------------------------------
    async def colors(self, ctx):
        channel = get(ctx.guild.text_channels, name="colors")
        class colorView(discord.ui.View):
                @discord.ui.button(label = "Green", style=discord.ButtonStyle.gray, emoji="🟢", row = 1, custom_id = "Green")
                async def green(self, interaction: discord.Interaction, button: discord.ui.Button):
                    user = interaction.user
                    userRoles = interaction.user.roles
                    Green = get(ctx.guild.roles, name="Green")
                    if Green in userRoles:
                        await user.remove_roles(Green)
                        await interaction.response.send_message("Removed green!", ephemeral=True)
                    else:
                        await user.add_roles(Green)
                        await interaction.response.send_message("Your color is now green!", ephemeral=True)

                @discord.ui.button(label = "Orange", style=discord.ButtonStyle.gray, emoji="🟠", row = 1, custom_id = "Orange")
                async def orange(self, interaction: discord.Interaction, button: discord.ui.Button):
                    user = interaction.user
                    Orange = get(ctx.guild.roles, name="Orange")
                    userRoles = interaction.user.roles
                    if Orange in userRoles:
                        await user.remove_roles(Orange)
                        await interaction.response.send_message("Removed orange!", ephemeral=True)
                    else:
                        await user.add_roles(Orange)
                        await interaction.response.send_message("Your color is now orange!", ephemeral=True)

                @discord.ui.button(label = "Purple", style=discord.ButtonStyle.gray, emoji="🟣", row = 1, custom_id = "Purple")
                async def purple(self, interaction: discord.Interaction, button: discord.ui.Button):
                    user = interaction.user
                    Purple = get(ctx.guild.roles, name="Purple")
                    userRoles = interaction.user.roles
                    if Purple in userRoles:
                        await user.remove_roles(Purple)
                        await interaction.response.send_message("Removed purple!", ephemeral=True)
                    else:
                        await user.add_roles(Purple)
                        await interaction.response.send_message("Your color is now purple!", ephemeral=True)

                @discord.ui.button(label = "Yellow", style=discord.ButtonStyle.gray, emoji="🟡", row = 1, custom_id = "Yellow")
                async def yellow(self, interaction: discord.Interaction, button: discord.ui.Button):
                    user = interaction.user
                    Yellow = get(ctx.guild.roles, name="Yellow")
                    userRoles = interaction.user.roles
                    if Yellow in userRoles:
                        await user.remove_roles(Yellow)
                        await interaction.response.send_message("Removed yellow!", ephemeral=True)
                    else:
                        await user.add_roles(Yellow)
                        await interaction.response.send_message("Your color is now yellow!", ephemeral=True)

                @discord.ui.button(label = "Red", style=discord.ButtonStyle.gray, emoji="🔴", row = 2, custom_id = "Red")
                async def red(self, interaction: discord.Interaction, button: discord.ui.Button):
                    user = interaction.user
                    Red = get(ctx.guild.roles, name="Red")
                    userRoles = interaction.user.roles
                    if Red in userRoles:
                        await user.remove_roles(Red)
                        await interaction.response.send_message("Removed red!", ephemeral=True)
                    else:
                        await user.add_roles(Red)
                        await interaction.response.send_message("Your color is now red!", ephemeral=True)

                @discord.ui.button(label = "Blue", style=discord.ButtonStyle.gray, emoji="🔵", row = 2, custom_id = "Blue")
                async def blue(self, interaction: discord.Interaction, button: discord.ui.Button):
                    user = interaction.user
                    Blue = get(ctx.guild.roles, name="Blue")
                    userRoles = interaction.user.roles
                    if Blue in userRoles:
                        await user.remove_roles(Blue)
                        await interaction.response.send_message("Removed blue!", ephemeral=True)
                    else:
                        await user.add_roles(Blue)
                        await interaction.response.send_message("Your color is now blue!", ephemeral=True)

                @discord.ui.button(label = "Teal", style=discord.ButtonStyle.gray, emoji="💠", row = 2, custom_id = "Teal")
                async def teal(self, interaction: discord.Interaction, button: discord.ui.Button):
                    user = interaction.user
                    Teal = get(ctx.guild.roles, name="Teal")
                    userRoles = interaction.user.roles
                    if Teal in userRoles:
                        await user.remove_roles(Teal)
                        await interaction.response.send_message("Removed teal!", ephemeral=True)
                    else:
                        await user.add_roles(Teal)
                        await interaction.response.send_message("Your color is now teal!", ephemeral=True)

                @discord.ui.button(label = "Pink", style=discord.ButtonStyle.gray, emoji="💗", row = 2, custom_id = "Pink")
                async def pink(self, interaction: discord.Interaction, button: discord.ui.Button):
                    user = interaction.user
                    Pink = get(ctx.guild.roles, name="Pink")
                    userRoles = interaction.user.roles
                    if Pink in userRoles:
                        await user.remove_roles(Pink)
                        await interaction.response.send_message("Removed pink!", ephemeral=True)
                    else:
                        await user.add_roles(Pink)
                        await interaction.response.send_message("Your color is now pink!", ephemeral=True)

        await channel.send(content="Choose the color of your name!\nClick the button again to remove the color.",view=colorView())


        
async def setup(bot):
    await bot.add_cog(Roles(bot))