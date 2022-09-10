from config import  configData
from pymongo import MongoClient
from pytz import timezone
from datetime import datetime

cluster = MongoClient(configData['mongokey'])

db = cluster['HYG']

points = db['points']

async def addp(membro, pontos):

    points.update_one({"_id": membro.id}, {"$inc": {"pontos": pontos}}, upsert = True)

async def addp2(membro, ctx, up):

    data_e_hora_atuais = datetime.now()

    fuso_horario = timezone('America/Sao_Paulo')

    data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
    
    dt = data_e_hora_sao_paulo.strftime('%d/%m/%Y')

    points.update_one({"_id": membro.id}, {"$set": {f"ponto{up}": f"adicionado {dt} por {ctx.name}"}}, upsert = True)



async def rmvp(membro, pontos):

    points.update_one({"_id": membro.id}, {"$inc": {"pontos": pontos}}, upsert = True)

async def rmvp2(membro, up,rs):

    points.update_one({"_id": membro.id}, {"$unset":{f"ponto{up}": rs}}, upsert = True)