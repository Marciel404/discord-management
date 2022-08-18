from outhers.info.fi import *

class tasks(commands.Cog):

    def __init__(self, bot:commands.Bot):

        self.bot = bot

    @tasks.loop(minutes = 1)
    async def times(self):

        guild = self.bot.get_guild(configData['guild'])

        data_e_hora_atuais = datetime.now()

        fuso_horario = timezone('America/Sao_Paulo')

        x = data_e_hora_atuais.astimezone(fuso_horario)

        if x.weekday() == 0:

            channel = self.bot.get_channel(configData['chats']['resumsemana'])

            verifi = discord.utils.get(guild.roles, id = configData['roles']['outras']['verificado'])

            naoverifi = discord.utils.get(guild.roles, id = configData['roles']['outras']['naoverificado'])

            mod = discord.utils.get(guild.roles, id = configData['roles']['staff']['mod'])

            overwrites = {

                verifi: discord.PermissionOverwrite(send_messages=True),

                mod: discord.PermissionOverwrite(send_messages=True),

                naoverifi: discord.PermissionOverwrite(read_messages=False),

            }

            if channel.overwrites == overwrites:

                None
            
            else:

                await channel.edit(overwrites = overwrites)

                await channel.send(
    f'''
Chat aberto!!! 
Vem contar algo sobre o que rolou na sua semana 😃 
||{verifi.mention}||
    ''')

        else:

            channel = self.bot.get_channel(configData['chats']['resumsemana'])

            verifi = discord.utils.get(guild.roles, id = configData['roles']['outras']['verificado'])

            naoverifi = discord.utils.get(guild.roles, id = configData['roles']['outras']['naoverificado'])

            mod = discord.utils.get(guild.roles, id = configData['roles']['staff']['mod'])

            overwrites = {

                verifi: discord.PermissionOverwrite(send_messages=False),

                naoverifi: discord.PermissionOverwrite(read_messages=False),

                mod: discord.PermissionOverwrite(send_messages=True),

            }

            if channel.overwrites == overwrites:

                None
            
            else:

                await channel.edit(overwrites = overwrites)

                await channel.send(f'E o chat está fechado novamente galera, deixando claro q próxima segunda ele volta😁')

    @commands.Cog.listener()
    async def on_ready(self):
        
        self.times.start()

def setup(bot:commands.Bot):
    bot.add_cog(tasks(bot))