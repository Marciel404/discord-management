from utils.configs import configData
from pymongo import MongoClient
#-----------------------------------------------------------------------------------------------------#
cluster = MongoClient(configData['mongokey'])

db = cluster["HYG"]

bank = db['bank']
#-----------------------------------------------------------------------------------------------------#
async def update_bank(id, HYGCOINS: int):

    if id is not None:

        bank.update_one({"_id": id.id}, {"$inc": {"HYGCOINS": HYGCOINS}}, upsert = True)
#-----------------------------------------------------------------------------------------------------#