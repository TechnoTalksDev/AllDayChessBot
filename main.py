from tabnanny import verbose
import os
from colorama import Fore
from dotenv import load_dotenv

try:
    from src.bot import bot
except Exception as error:
    print(f"{Fore.RED}Something fatal occured while loading the bot...{Fore.RESET}")
    raise error

load_dotenv(verbose=False)

token = os.getenv("TOKEN")

bot.run(token)