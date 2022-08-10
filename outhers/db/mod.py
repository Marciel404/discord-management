from ..info.fi import *

cluster = MongoClient(configData['mongokey'])

db = cluster['HYG']

mute = db['adv']

ausen = db['ausente']

async def advdb(id, qnt, motivo):

    mute.update_one({"_id": id.id}, {"$set": {f"Adv{qnt}": motivo}}, upsert = True)

async def rmvadvdb(id, qnt, motivo):

    mute.update_one({"_id": id.id}, {"$set": {f"Adv{qnt}": motivo}}, upsert = True)



async def ausendb(id, motivo, data):

    ausen.update_one({"_id": id.id}, {"$set": {f"Nome": id.name, f"Motivo": motivo, f"Data": data, "Ausente?": True}}, upsert = True)

    if ausen.find_one({"_id": 'validador'})['valor'] == 0:

        ausen.update_one({"_id": 'validador'}, {"$set": {f"valor": 1}}, upsert = True)

async def desausendb(id):

    ausen.update_one({"_id": id.id}, {"$set": {f"Nome": id.name, f"Motivo": 'None', f"Data": 'None', "Ausente?": False}}, upsert = True)

    if (ausen.count_documents({'Ausente?': True}) == 0):

        ausen.update_one({"_id": 'validador'}, {"$set": {f"valor": 0}}, upsert = True)