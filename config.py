from os import environ 

class Config:
    API_ID = environ.get("API_ID", "7786548")
    API_HASH = environ.get("API_HASH", "76234c15c4db04d048a910e938acb087")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7108939020:AAEpTVPazl5Bgg_UvXypFKUYiQ19ZU2icg0") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://cluster0.z3blbfz.mongodb.net/?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "mbox")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '6747805034').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
