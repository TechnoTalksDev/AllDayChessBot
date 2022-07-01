import discord, coloredlogs, logging
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

    @user_command()
    async def greet(self, ctx, member: discord.Member):
        await ctx.respond(f"{ctx.author.mention} says hello to {member.mention}!")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel=discord.utils.get(member.guild.channels, name="welcome")
        await channel.send(f"Hey <@{member.id}>, **welcome to Official AllDayChess Discord!** Make sure to **read the rules** and __abide by them__! We hope that you **__have fun here__** in the Official AllDayChess Discord server!")

    @commands.Cog.listener()
    async def on_message(self, message):
        if "drill" in message.content.lower() and message.author != self.bot.user:
            await message.delete()
            await message.channel.send(f"**We don't talk about the drill around these parts...**")

def setup(bot):
    bot.add_cog(General(bot))
    logger.info("Loaded extension General...")

def teardown(bot):
    logger.info("Unloaded extension General...")