import discord, time, datetime, psutil
from discord.ext import commands
from colorama import Fore
from psutil._common import bytes2human

status = discord.Activity(type=discord.ActivityType.watching, name="Coming Soon!")

intents = discord.Intents.default()

intents.message_content = True

bot = discord.Bot(description="The bot that runs the AllDayChess Discord!", activity=status, debug_guilds=[846192394214965268, 796157315174498324], intents=intents)

color=0xCBC395

version = "v1.0"

process = psutil.Process()

@bot.event
async def on_ready():
    print(Fore.LIGHTBLUE_EX+
""".-. .-. .-. . . . . .-.   .-. .-. .   . . .-. 
 |  |-  |   |-| |\| | |    |  |-| |   |<  `-. 
 '  `-' `-' ' ` ' ` `-'    '  ` ' `-' ' ` `-'
presents: """+Fore.RESET)
    print(f"[AllDayChess] Logged in as {bot.user}")
    global startTime
    startTime=time.time()

@bot.slash_command(description="Get stats about the bot!")
async def ping(ctx):
    await ctx.defer()

    embed = discord.Embed(title=f"{bot.user.name} Stats", color=color)
    embed.set_author(name="Pong 🏓", url="https://en.wikipedia.org/wiki/Network_delay")
    embed.set_thumbnail(url="https://www.technotalks.net/static/main/images/alldaychess.gif")
    embed.add_field(name="Ping", value=f"`{round(bot.latency*1000)}ms`")
    embed.add_field(name="Uptime", value=f"`{datetime.timedelta(seconds=int(time.time()-startTime))}`")
    embed.add_field(name="Version", value=f"`{version}`")
    embed.add_field(name="RAM", value=f"`{bytes2human(process.memory_info().rss)}`")

    await ctx.respond(embed=embed)