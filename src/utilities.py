from inspect import Traceback
import colorama, discord, motor, asyncio, os, motor.motor_asyncio
from colorama import Fore
from dotenv import load_dotenv

colorama.init(True)

load_dotenv()

class ErrorMessage():
    def default():
        defaultMessage = "Sorry for the inconvenience, my developer has been notified!"
        
        embed = discord.Embed(title = "❤️‍🔥 Uh oh something went wrong!", color=0xff1a1a)
        embed.add_field(name = "Please try again!", value = defaultMessage)

        return embed

class Mongo():
    def __init__(self):
        mongo_link=os.getenv("MONGO_LINK")
        
        cluster = motor.motor_asyncio.AsyncIOMotorClient(mongo_link, connect=True, serverSelectionTimeoutMS=5000, connectTimeoutMS=5000)

        self.db = cluster.alldaychess

    def get_collection(self, collection_name:str):
        try: 
            coll = self.db[collection_name]
            return coll
        except:
            return None
    