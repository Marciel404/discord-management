import discord
import os
import json
import aiohttp
import asyncio

from discord.ext import commands
from pytz import timezone
from datetime import datetime
from discord.ext import commands
from pymongo import MongoClient

data_e_hora_atuais = datetime.now()
fuso_horario = timezone('America/Sao_Paulo')
data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
dt = data_e_hora_sao_paulo.strftime('%H:%M %d/%m/%Y')

if os.path.exists((os.getcwd() + "/config.json")):
    with open("config.json") as f:
        configData = json.load(f)
