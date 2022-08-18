import discord
import os
import json
import aiohttp
import asyncio
import requests

from discord.ext import commands, tasks
from pytz import timezone
from datetime import datetime
from pymongo import MongoClient


if os.path.exists((os.getcwd() + "/config.json")):
    with open("config.json") as f:
        configData = json.load(f)
