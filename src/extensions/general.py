import discord, coloredlogs, logging, time, datetime
from discord.ext import commands
from discord.commands import slash_command, user_command

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

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        logger.debug("Member remove event triggered")
        channel=discord.utils.get(member.guild.channels, name="mod-logs")
        embed=discord.Embed(title="Member left", color=discord.Colour.random())
        embed.set_author(name=f"{member.display_name}", icon_url=member.display_avatar.url)
        embed.add_field(name="Time", value=f"<t:{int(time.time())}>", inline=True)
        embed.set_footer(text=f"ID: {member.id}")
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message(self, message):
        logger.debug("Message event triggered")
        if "drill" in message.content.lower() and message.author != self.bot.user:
            await message.delete()
            await message.channel.send(f"**We don't talk about the drill around these parts...**")

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