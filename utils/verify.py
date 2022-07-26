import discord

from utils.configs import  configData
from classes.ticket import adonticket, adonticket2, ticket
from classes.buttonsstaff import cmdstf
from db.mod import tick, adv
from db.evento import points
#-----------------------------------------------------------------------------------------------------#
async def verfyadv(self, member):

    role1 = discord.utils.get(member.guild.roles, id = configData['roles']['adv']['adv1'])

    role2 = discord.utils.get(member.guild.roles, id = configData['roles']['adv']['adv2'])

    role3 = discord.utils.get(member.guild.roles, id = configData['roles']['adv']['adv3'])

    if adv.count_documents({ "_id": member.id}) == 1:

        ad = adv.find_one({"_id": member.id})

        adv1 = ad['Adv1']

        adv2 = ad['Adv2']

        adv3 = ad['Adv3']

        if adv3 != 'None':

            await  member.add_roles(role1, role2, role3)

            return

        if adv2 != 'None':

            await  member.add_roles(role1, role2)

            return

        if adv1 != 'None':

            await  member.add_roles(role1)

            return
#-----------------------------------------------------------------------------------------------------#
async def verfypoints(self, member):

    if points.count_documents({ "_id": member.id}) == 1:

        p = points.find_one({"_id": member.id})

        if discord.utils.get(member.guild.roles, name = f'{p["pontos"]}🏆') in member.guild.roles:

            await member.add_roles(discord.utils.get(member.guild.roles, name = f'{p["pontos"]}🏆'))
#-----------------------------------------------------------------------------------------------------#
async def bottonstaffloader(self):

    channel = self.get_channel(configData['chats']['cmdstf'])

    mensagem = await channel.fetch_message(int(configData['chats']['ids']['cmdstf']))

    await mensagem.edit(view = cmdstf(self))
#-----------------------------------------------------------------------------------------------------#
async def ticketloader(self):

    channel = self.get_channel(configData['chats']['ticket'])

    mensagem = await channel.fetch_message(int(configData['chats']['ids']['tck']))

    await mensagem.edit(view = ticket())
#-----------------------------------------------------------------------------------------------------#
async def verifyticket(self):

    if tick.find_one({"_id": 'validador'})['valor'] == 1:

        for x in tick.find({'aberto?': True}):

            channel = discord.utils.get(self.get_guild(configData['guild']).channels, name = f'ticket-{x["_id"]}')

            msg = await channel.fetch_message(x['msgid'])

            await msg.edit(view = adonticket(self.get_user(x["_id"])))

        for x in tick.find({'fechado?': True}):

            channel = discord.utils.get(self.get_guild(configData['guild']).channels, name = f'ticket-{x["_id"]}')

            msg = await channel.fetch_message(x['msgid'])

            await msg.edit(view = adonticket2(self.get_user(x["_id"])))
#-----------------------------------------------------------------------------------------------------#