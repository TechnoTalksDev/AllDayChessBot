import os, discord, psutil, coloredlogs, logging, traceback 
import src.utilities as utilities
from colorama import Fore
from dotenv import load_dotenv

#Logging setup
coloredlogs.install(level="INFO", fmt="%(asctime)s %(name)s[%(process)d] %(levelname)s %(message)s")
logger = logging.getLogger()
file_handler = logging.FileHandler("SEVERE.log")
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(logging.Formatter(fmt="%(asctime)s %(name)s[%(process)d] %(levelname)s %(message)s"))
logger.addHandler(file_handler)

try:
    from src.bot import bot
except Exception as error:
    logger.critical("Something fatal occured while loading the bot...")
    logger.error(traceback.format_exc())

load_dotenv()

token = os.getenv("TOKEN")

#Run bot
if __name__ == "__main__":
    try: 
        bot.run(token)
    except:
        pass