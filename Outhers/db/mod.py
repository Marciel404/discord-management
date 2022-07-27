from Outhers.info.fi import *

cluster = MongoClient('mongodb+srv://Marciel:açucar@markuus.c1awv.mongodb.net/test?')

db = cluster['HYG']

mute = db['adv']

async def advdb(id, qnt, motivo):

    mute.update_one({"_id": id.id}, {"$set": {f"Adv{qnt}": motivo}}, upsert = True)


async def rmvadvdb(id, qnt, motivo):

    mute.update_one({"_id": id.id}, {"$set": {f"Adv{qnt}": motivo}}, upsert = True)