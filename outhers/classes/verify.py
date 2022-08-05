from outhers.db.mod import *

async def verfyadv(self, member):

    myquery = { "_id": member.id}

    role1 = discord.utils.get(member.guild.roles, id = configData['roles']['adv']['adv1'])

    role2 = discord.utils.get(member.guild.roles, id = configData['roles']['adv']['adv2'])

    role3 = discord.utils.get(member.guild.roles, id = configData['roles']['adv']['adv3'])

    if (mute.count_documents(myquery) == 1):

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