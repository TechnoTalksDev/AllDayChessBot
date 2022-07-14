import discord, time, psutil, sys, traceback, logging, coloredlogs, datetime
from discord.ext import commands
from colorama import Fore
from psutil._common import bytes2human
import src.utilities as utilities
import src.extensions.general as general
#create bot status
status = discord.Activity(type=discord.ActivityType.watching, name=f"Coming Soon!")
#intents
intents = discord.Intents().default()
intents.message_content = True
intents.members = True
#accent color of bot
color=0xCBC395
#bot version
version = "v1.0"
#bot process
process = psutil.Process()
#create bot
bot = discord.Bot(description="The bot that runs the AllDayChess Discord!", activity=status, debug_guilds=[846192394214965268], intents=intents)

#Logging setup
coloredlogs.install(level="INFO", fmt="%(asctime)s %(name)s[%(process)d] %(levelname)s %(message)s")
logger = logging.getLogger("AllDayChess")
file_handler = logging.FileHandler("SEVERE.log")
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(logging.Formatter(fmt="%(asctime)s %(name)s[%(process)d] %(levelname)s %(message)s"))
logger.addHandler(file_handler)

@bot.event
async def on_ready():
    print(Fore.LIGHTBLUE_EX+
""".-. .-. .-. . . . . .-.   .-. .-. .   . . .-. 
 |  |-  |   |-| |\| | |    |  |-| |   |<  `-. 
 '  `-' `-' ' ` ' ` `-'    '  ` ' `-' ' ` `-'
presents: """+Fore.RESET)
    logger.info(f"Logged in as {bot.user}")
    global startTime
    startTime=time.time()

    bot.add_view(general.General.rrmView())


bot.load_extension("src.extensions.general")

@bot.slash_command(description="Gives stats of the bot.")
async def ping(ctx):
    uptime = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
    embed = discord.Embed(title=f"{bot.user.display_name} Stats", color=color)
    embed.set_author(name="Pong! 🏓")
    embed.add_field(name="Ping",value=f"`{round(bot.latency * 1000)}ms`",inline=True)
    embed.add_field(name="Uptime", value=f"`{uptime}`", inline=True)
    users = 0
    for guild in bot.guilds:
        users += guild.member_count
    embed.add_field(name="Users", value=f"`{users}`", inline=True)
    embed.add_field(name="Version", value=f"`{version}`", inline=True)
    embed.add_field(name="RAM", value=f"`{bytes2human(process.memory_info().rss)} used`", inline=True)
    await ctx.respond(embed=embed)