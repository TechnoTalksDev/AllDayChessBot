import discord, coloredlogs, logging, time, datetime
from discord.ext import commands
from discord.commands import slash_command, user_command
from psutil._common import bytes2human

#Logging setup
coloredlogs.install(level="INFO", fmt="%(asctime)s %(name)s[%(process)d] %(levelname)s %(message)s")
logger = logging.getLogger("AllDayChess.general")
file_handler = logging.FileHandler("SEVERE.log")
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(logging.Formatter(fmt="%(asctime)s %(name)s[%(process)d] %(levelname)s %(message)s"))
logger.addHandler(file_handler)

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    async def hello(self, ctx):
        await ctx.respond("Hello!") 

    #Reaction roles
    #View for buttons
    class rrmView(discord.ui.View):
        def __init__(self):
            super().__init__(timeout=None)

        @discord.ui.button(label="Giveaway Alerts", row=1, style=discord.ButtonStyle.primary, emoji="<:giveaway:818912244464877678>", custom_id="GiveawayAlertsRRButton")
        async def give_button_callback(self, button, interaction):
            await interaction.response.send_message("Giveaway Alerts role added!", ephemeral=True)

        @discord.ui.button(label="Puzzle Solvers", row=1, style=discord.ButtonStyle.secondary, emoji="<:checkmate:801882670770421780>", custom_id="PuzzleSolversRRButton")
        async def puzzle_button_callback(self, button, interaction):
            await interaction.response.send_message("Giveaway Alerts role added!", ephemeral=True)

        @discord.ui.button(label="Twitter Notifications", row=2, style=discord.ButtonStyle.primary, emoji="<:twitter:817800730945388574>", custom_id="TwitterNotifsRRButton")
        async def twitter_button_callback(self, button, interaction):
            await interaction.response.send_message("Giveaway Alerts role added!", ephemeral=True)

        @discord.ui.button(label="Instagram Notifications", row=2, style=discord.ButtonStyle.danger, emoji="<:instagram:817800644009787424>", custom_id="InstaNotifsRRButton")
        async def insta_button_callback(self, button, interaction):
            await interaction.response.send_message("Giveaway Alerts role added!", ephemeral=True)

        @discord.ui.button(label="Facebook Notifications", row=2, style=discord.ButtonStyle.primary, emoji="<:facebook:817800644055531562>", custom_id="FacebookNotifsRRButton")
        async def face_button_callback(self, button, interaction):
            await interaction.response.send_message("Giveaway Alerts role added!", ephemeral=True)

        @discord.ui.button(label="Poll Notifications", row=3, style=discord.ButtonStyle.success, emoji="🛑", custom_id="PollNotifsRRButton")
        async def poll_button_callback(self, button, interaction):
            await interaction.response.send_message("Giveaway Alerts role added!", ephemeral=True)

        @discord.ui.button(label="Tournament Notifications", row=3, style=discord.ButtonStyle.secondary, emoji="🛑", custom_id="TournamentNotifsRRButton")
        async def tournament_button_callback(self, button, interaction):
            await interaction.response.send_message("Giveaway Alerts role added!", ephemeral=True)
    #Reactions role command
    @slash_command(description="Send the reaction role message in a specified channel...")
    async def rrm(self, ctx, channel: discord.Option(discord.TextChannel, "Channel")):
        embed=discord.Embed(title="Select your roles!", description="Use the buttons to add roles to yourself!", color=discord.Colour.random())
        embed.add_field(name="Get a role", value="To get a role please hit the respective button")
        embed.add_field(name="Remove a role", value="Hit the respective button of the role you want to remove")
        embed.set_footer(text="Discord Interactions depend on discord processing the interaction if your wondering why the buttons take a hot second to trigger!", icon_url="https://discord.com/assets/f9bb9c4af2b9c32a2c5ee0014661546d.png")
        await ctx.respond(f"Reaction role message sent to <#{channel.id}>")
        await channel.send(embed=embed, view=General.rrmView())
    #Reaction roles with reactions
    @slash_command(description="Send the reaction role message in a specified channel... (REACTIONs)")
    async def rrmr(self, ctx, channel: discord.Option(discord.TextChannel, "Channel")):
        #Send pretty embed
        embed=discord.Embed(title="Select your roles!", description="Use the buttons to add roles to yourself!", color=discord.Colour.from_rgb(54, 57, 63))
        embed.set_author(name="AllDayChess Roles", icon_url="https://media.discordapp.net/attachments/784462491240366101/852720699574452234/logo2.png")
        embed.set_thumbnail(url="https://cdn4.iconfinder.com/data/icons/business-team-work-outline-color-style-2/64/Roles-512.png")
        embed.set_image(url="attachment://ROLES.png")
        embed.add_field(name="Get a role", value="To get a role please hit the respective emoji")
        embed.add_field(name="Remove a role", value="Remove the reaction on the emoji of the role you want to remove")
        embed.add_field(name="Role list", value="• <:giveaway:818912244464877678> - Giveaway alerts\n• <:checkmate:801882670770421780> - Puzzle Solvers\n• <:twitter:817800730945388574> - Twitter Notifications\n• <:instagram:817800644009787424> - Instagram Notifications\n• <:facebook:817800644055531562> - Facebook Notifications\n• 🛑 - Poll Notifications\n• 🛑 - Tournament Notifications", inline=False)
        await ctx.respond(f"Reaction role message sent to <#{channel.id}>")
        #Add reactions
        message = await channel.send(embed=embed, file=discord.File("src/assets/ROLES.png", "ROLES.png"))
        await message.add_reaction("giveaway:818912244464877678")
        await message.add_reaction("checkmate:801882670770421780")
        await message.add_reaction("twitter:817800730945388574")
        await message.add_reaction("instagram:817800644009787424")
        await message.add_reaction("facebook:817800644055531562")
        await message.add_reaction("🛑")

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        reaction_channel = payload.channel_id
        roles_channel = discord.utils.get(payload.member.guild.channels, name="roles").id
        if reaction_channel == roles_channel:
            await self.bot.get_channel(roles_channel).send("> Nope... Yea... This dosen't work yet 🤷‍♂️ -> " + str(payload.emoji))

    #Join Message
    @commands.Cog.listener()
    async def on_member_join(self, member):
        logger.debug("Member join event triggered")
        channel=discord.utils.get(member.guild.channels, name="welcome")
        embed=discord.Embed(title="Welcome to the Official AllDayChess Discord!", color=discord.Colour.random())
        embed.set_author(name=f"{member.display_name}", icon_url=member.display_avatar.url)
        embed.set_thumbnail(url=member.display_avatar.url)
        rules = discord.utils.get(member.guild.channels, name="rules-and-info")
        try:
            general = discord.utils.get(member.guild.channels, name="general")
            logger.debug("Member joined in dev server")
        except:
            general = discord.utils.get(member.guild.channels, name="general-chat")
        embed.add_field(name="Read the rules!", value=f"Make sure to read the rules and abide by them at <#{rules.id}>!", inline=False)
        embed.add_field(name="Have fun!", value=f"We hope you have fun! Check out <#{general.id}> and start chatting!", inline=False)
        embed.add_field(name="\u200B", value=f"<@{member.id}> Joined on <t:{int(time.time())}>", inline=False)
        await channel.send(embed=embed)
        #await channel.send(f"Hey <@{member.id}>, **welcome to Official AllDayChess Discord!** Make sure to **read the rules** and __abide by them__! We hope that you **__have fun here__** in the Official AllDayChess Discord server!")
    #Member leave logging
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        logger.debug("Member remove event triggered")
        channel=discord.utils.get(member.guild.channels, name="mod-logs")
        embed=discord.Embed(title="Member left", color=discord.Colour.random())
        embed.set_author(name=f"{member.display_name}", icon_url=member.display_avatar.url)
        embed.add_field(name="Time", value=f"<t:{int(time.time())}>", inline=True)
        embed.add_field(name="Join Date", value=f"<t:{int(member.joined_at.timestamp())}>")
        embed.set_footer(text=f"ID: {member.id}")
        await channel.send(embed=embed)
    #bum bum bum
    @commands.Cog.listener()
    async def on_message(self, message):
        logger.debug("Message event triggered")
        if "drill" in message.content.lower() and message.author != self.bot.user:
            await message.delete()
            await message.channel.send(f"**We don't talk about the drill around these parts...**")
    #deleted message
    @commands.Cog.listener()
    async def on_message_delete(self, message):
        logger.debug("Message delete event triggered")
        channel=discord.utils.get(message.author.guild.channels, name="mod-logs")
        embed=discord.Embed(title="Message deleted", color=discord.Colour.random())
        embed.set_author(name=f"{message.author.display_name}", icon_url=message.author.display_avatar.url)
        embed.add_field(name="Message", value=message.content)
        embed.add_field(name="Channel", value=f"<#{message.channel.id}>")
        embed.add_field(name="Created", value=f"{message.created_at}")
        embed.add_field(name="Time", value=f"<t:{int(time.time())}>", inline=False)
        embed.set_footer(text=f"Author ID: {message.author.id}  Message ID: {message.id}")
        await channel.send(embed=embed)      

def setup(bot):
    bot.add_cog(General(bot))
    logger.info("Loaded extension General...")

def teardown(bot):
    logger.info("Unloaded extension General...")