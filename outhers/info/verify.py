import discord
from config import  configData

from ..db.mod import *
from ..db.evento import *

async def verfyadv(self, member):

    role1 = discord.utils.get(member.guild.roles, id = configData['roles']['adv']['adv1'])

    role2 = discord.utils.get(member.guild.roles, id = configData['roles']['adv']['adv2'])

    role3 = discord.utils.get(member.guild.roles, id = configData['roles']['adv']['adv3'])

    if (mute.count_documents({ "_id": member.id}) == 1):

        adv = mute.find_one({"_id": member.id})

        adv1 = adv['Adv1']

        adv2 = adv['Adv2']

        adv3 = adv['Adv3']

        if adv3 != 'None':

            await  member.add_roles(role1, role2, role3)

            return

        if adv2 != 'None':

            await  member.add_roles(role1, role2)

            return

        if adv1 != 'None':

            await  member.add_roles(role1)

            return

async def verfypoints(self, member):

    if (points.count_documents({ "_id": member.id}) == 1):

        p = points.find_one({"_id": member.id})

        if discord.utils.get(member.guild.roles, name = f'{p["pontos"]}🏆') in member.guild.roles:

            await member.add_roles(discord.utils.get(member.guild.roles, name = f'{p["pontos"]}🏆'))