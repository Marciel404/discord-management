import discord, asyncio
from Outhers.info.fi import configData

class adonticket2(discord.ui.View):

    def __init__(self, membro):

        self.membro = membro

        super().__init__(timeout = None)

    @discord.ui.button(label = '🔓 Abrir ticket', style = discord.ButtonStyle.blurple)
    async def abrir(self,  button: discord.ui.Button, interaction: discord.Interaction):

        member = self.membro

        guild = interaction.guild

        admin = discord.utils.get(guild.roles, id = configData['roles']['admin'])
            
        mod = discord.utils.get(guild.roles, id = configData['roles']['mod'])

        submod = discord.utils.get(guild.roles, id = configData['roles']['submod'])

        overwrites = {

            member: discord.PermissionOverwrite(read_messages=True),

            guild.default_role: discord.PermissionOverwrite(read_messages=False),

            admin: discord.PermissionOverwrite(read_messages=True),

            mod: discord.PermissionOverwrite(read_messages=True),

            submod: discord.PermissionOverwrite(read_messages=True),

        }

        await interaction.channel.edit(overwrites = overwrites)

        await interaction.message.delete()

        await interaction.channel.send('Ticket aberto 🔓', view = adonticket(self.membro))

    @discord.ui.button(label = '🛑 Deletar Ticket', style = discord.ButtonStyle.blurple)
    async def delete(self,  button: discord.ui.Button, interaction: discord.Interaction):

        await interaction.response.send_message('O ticket sera deletado em segundos')

        await asyncio.sleep(5)

        await interaction.channel.delete()

class adonticket(discord.ui.View):
    
    def __init__(self, membro):

        self.membro = membro

        super().__init__(timeout = None)

    @discord.ui.button(label = '🔒 Fechar ticket', style = discord.ButtonStyle.blurple)
    async def close(self,  button: discord.ui.Button, interaction: discord.Interaction):

        if interaction.user.id == self.membro.id:
            return

        member = self.membro

        guild = interaction.guild

        admin = discord.utils.get(guild.roles, id = configData['roles']['admin'])
            
        mod = discord.utils.get(guild.roles, id = configData['roles']['mod'])

        submod = discord.utils.get(guild.roles, id = configData['roles']['submod'])

        overwrites = {

            member: discord.PermissionOverwrite(read_messages=False),

            guild.default_role: discord.PermissionOverwrite(read_messages=False),

            admin: discord.PermissionOverwrite(read_messages=True),

            mod: discord.PermissionOverwrite(read_messages=True),

            submod: discord.PermissionOverwrite(read_messages=True),

        }

        e = discord.Embed(description = f'🔒Ticket fechado por {interaction.user.mention} \nClique no 🔓 para abrir')

        await interaction.channel.edit(overwrites = overwrites)
        await interaction.message.delete()
        await interaction.channel.send(embed = e, view = adonticket2(member))

        self.stop()

class ticket(discord.ui.View):
    
    def __init__(self):

        super().__init__(timeout = None)
        
    @discord.ui.button(label = '🛎 Criar ticket', style = discord.ButtonStyle.blurple)
    async def confirm(self,  button: discord.ui.Button, interaction: discord.Interaction):

        guild = interaction.guild

        Chat = discord.utils.get(guild.channels, name=f'ticket-{interaction.user.id}')

        if Chat is None:

            guild = interaction.guild

            ticket = f'ticket-{interaction.user.id}'

            member = interaction.user

            admin = discord.utils.get(guild.roles, id = configData['roles']['admin'])
            
            mod = discord.utils.get(guild.roles, id = configData['roles']['mod'])

            submod = discord.utils.get(guild.roles, id = configData['roles']['submod'])

            overwrites = {

                guild.default_role: discord.PermissionOverwrite(read_messages=False),

                member: discord.PermissionOverwrite(read_messages=True),

                admin: discord.PermissionOverwrite(read_messages=True),

                mod: discord.PermissionOverwrite(read_messages=True),

                submod: discord.PermissionOverwrite(read_messages=True),

                }

            channel = await guild.create_text_channel(name=ticket, overwrites = overwrites)

            await interaction.response.send_message('Ticket criado com sucesso', ephemeral = True)

            await channel.send(view=adonticket(member))

            await channel.send(f'{interaction.user.mention} {submod.mention}')
        
        else:

            await interaction.response.send_message('Ticket já existente, encerre o ultimo para criar outro', ephemeral = True)

class kick(discord.ui.View):
    
    def __init__(self, bot, membro, motivo, ctx):

        self.membro = membro

        self.bot = bot

        self.motivo = motivo

        self.ctx = ctx

        super().__init__(timeout = 180)

    @discord.ui.button(label = '✅', style = discord.ButtonStyle.blurple)
    async def confirmkick(self, button: discord.ui.Button, interaction: discord.Interaction):

        if interaction.user.id != self.ctx.author.id:
            return
        
        l1 = self.bot.get_channel(configData['logs']['mod'])

        guild = interaction.guild

        E = discord.Embed(title = 'kick', description = f'Pessoa expulsa: {self.membro.name} \n Quem expulsou: {interaction.user.mention} \n motivo: {self.motivo}')

        await l1.send(embed = E)

        await interaction.response.send_message(f'{self.membro.name} expulso com sucesso', ephemeral = True)

        await guild.kick(user = self.membro ,reason = self.motivo)

        self.stop()

    @discord.ui.button(label = '❎', style = discord.ButtonStyle.blurple)
    async def denykick(self, button: discord.ui.Button, interaction: discord.Interaction):

        if interaction.user.id != self.ctx.author.id:
            return

        await interaction.response.send_message(f'Ufa, ainda bem que não tive que expulsar o {self.membro.mention}')

        self.stop()

class ban(discord.ui.View):
    
    def __init__(self, bot, membro, motivo, ctx):

        self.membro = membro

        self.bot = bot

        self.motivo = motivo

        self.ctx = ctx

        super().__init__(timeout = 180)

    @discord.ui.button(label = '✅', style = discord.ButtonStyle.blurple)
    async def confirmban(self, button: discord.ui.Button, interaction: discord.Interaction):

        if interaction.user.id != self.ctx.author.id:
            return
        
        l1 = self.bot.get_channel(configData['logs']['mod'])

        guild = interaction.guild

        E = discord.Embed(title = 'Ban', description = f'Pessoa banida: {self.membro.name} \n Quem baniu: {interaction.user.mention} \n motivo: {self.motivo}')

        await l1.send(embed = E)

        await interaction.response.send_message(f'{self.membro.name} banido com sucesso', ephemeral = True)

        await guild.ban(user = self.membro ,reason = self.motivo)

        self.stop()

    @discord.ui.button(label = '❎', style = discord.ButtonStyle.blurple)
    async def denyban(self, button: discord.ui.Button, interaction: discord.Interaction):

        if interaction.user.id != self.ctx.author.id:
            return

        await interaction.response.send_message(f'Ufa, ainda bem que não tive que banir o {self.membro.mention}')

        self.stop()

class banid(discord.ui.View):
    
    def __init__(self, bot, membro, motivo, ctx):

        self.membro = membro

        self.bot = bot

        self.motivo = motivo

        self.ctx = ctx

        super().__init__(timeout = 180)

    @discord.ui.button(label = '✅', style = discord.ButtonStyle.blurple)
    async def confirmban(self, button: discord.ui.Button, interaction: discord.Interaction):

        if interaction.user.id != self.ctx.author.id:
            return
        
        l1 = self.bot.get_channel(configData['logs']['mod'])

        member1 = await self.bot.fetch_user(self.membro)

        guild = interaction.guild

        E = discord.Embed(title = 'Ban', description = f'Pessoa banida: {self.membro.name} \n Quem baniu: {interaction.user.mention} \n motivo: {self.motivo}')

        await l1.send(embed = E)

        await interaction.response.send_message(f'{self.membro.name} banido com sucesso', ephemeral = True)

        await guild.ban(user = self.membro ,reason = self.motivo)

        self.stop()

    @discord.ui.button(label = '❎', style = discord.ButtonStyle.blurple)
    async def denyban(self, button: discord.ui.Button, interaction: discord.Interaction):

        if interaction.user.id != self.ctx.author.id:
            return

        await interaction.response.send_message(f'Ufa, ainda bem que não tive que banir o {self.membro.mention}')

        self.stop()