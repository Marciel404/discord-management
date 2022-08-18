from ..info.fi import configData
from ..db.mod import *
from .selectmenus import *

class adonticket2(discord.ui.View):

    def __init__(self, membro):

        self.membro = membro

        super().__init__(timeout = None)

    @discord.ui.button(label = '🔓 Abrir ticket', style = discord.ButtonStyle.blurple)
    async def abrir(self,  button: discord.ui.Button, interaction: discord.Interaction):

        member = self.membro

        guild = interaction.guild

        admin = discord.utils.get(guild.roles, id = configData['roles']['staff']['admin'])
            
        mod = discord.utils.get(guild.roles, id = configData['roles']['staff']['mod'])

        suporte = discord.utils.get(guild.roles, id = configData['roles']['staff']['suporte'])

        overwrites = {

            member: discord.PermissionOverwrite(read_messages=True),

            guild.default_role: discord.PermissionOverwrite(read_messages=False),

            admin: discord.PermissionOverwrite(read_messages=True),

            mod: discord.PermissionOverwrite(read_messages=True),

            suporte: discord.PermissionOverwrite(read_messages=True),

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

        if discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['staff']) not in interaction.user.roles:

            return

        member = self.membro

        guild = interaction.guild

        admin = discord.utils.get(guild.roles, id = configData['roles']['staff']['admin'])
            
        mod = discord.utils.get(guild.roles, id = configData['roles']['staff']['mod'])

        suporte = discord.utils.get(guild.roles, id = configData['roles']['staff']['suporte'])

        overwrites = {

            member: discord.PermissionOverwrite(read_messages=False),

            guild.default_role: discord.PermissionOverwrite(read_messages=False),

            admin: discord.PermissionOverwrite(read_messages=True),

            mod: discord.PermissionOverwrite(read_messages=True),

            suporte: discord.PermissionOverwrite(read_messages=True),

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

        data_e_hora_atuais = datetime.now()

        fuso_horario = timezone('America/Sao_Paulo')

        data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)

        dt = data_e_hora_sao_paulo.strftime('%d/%m/%Y')

        guild = interaction.guild

        Chat = discord.utils.get(guild.channels, name=f'ticket-{interaction.user.id}')

        if Chat is None:

            guild = interaction.guild

            ticket = f'ticket-{interaction.user.id}'

            member = interaction.user

            admin = discord.utils.get(guild.roles, id = configData['roles']['staff']['admin'])
            
            mod = discord.utils.get(guild.roles, id = configData['roles']['staff']['mod'])

            suporte = discord.utils.get(guild.roles, id = configData['roles']['staff']['suporte'])

            overwrites = {

                guild.default_role: discord.PermissionOverwrite(read_messages=False),

                member: discord.PermissionOverwrite(read_messages=True),

                admin: discord.PermissionOverwrite(read_messages=True),

                mod: discord.PermissionOverwrite(read_messages=True),

                suporte: discord.PermissionOverwrite(read_messages=True),

                }

            for file in os.listdir('./tickets'):

                if file.endswith('.txt'):

                    if file.startswith(f'{ticket}'):

                        os.remove(f"./tickets/{ticket}.txt")

            with open(f'./tickets/{ticket}.txt', 'a') as f:

                f.write(f'Ticket de {interaction.user.name} {dt}')

            channel = await guild.create_text_channel(name=ticket, 
            overwrites = overwrites, 
            category = discord.utils.get(interaction.guild.categories, id = configData['catego']['ticket']))

            await interaction.response.send_message('Ticket criado com sucesso', ephemeral = True)

            await channel.send(view=adonticket(member))

            await channel.send(f'{interaction.user.mention} {suporte.mention}')
        
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

        if discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['admin']) or discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['mod']) in interaction.user.roles:
        
            l1 = self.bot.get_channel(configData['logs']['mod'])

            guild = interaction.guild

            E = discord.Embed(title = 'kick', description = f'Pessoa expulsa: {self.membro.name} \n Quem expulsou: {self.ctx.mention} \nAprovado por: {interaction.user.mention} \n motivo: {self.motivo} \n{self.membro.id}')

            await l1.send(embed = E)

            await interaction.message.delete()

            await interaction.response.send_message(f'{self.membro.name} expulso com sucesso', ephemeral = True)

            await guild.kick(user = self.membro ,reason = self.motivo)

            self.stop()

        else:

            await interaction.response.send_message('Você não tem permissão para usar isso', ephemeral = True)

    @discord.ui.button(label = '❎', style = discord.ButtonStyle.blurple)
    async def denykick(self, button: discord.ui.Button, interaction: discord.Interaction):

        if discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['admin']) or discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['mod']) in interaction.user.roles:
        
            await interaction.message.delete()

            await interaction.response.send_message(f'Ufa, ainda bem que não tive que expulsar o {self.membro.mention}', ephemeral = True)

            self.stop()

        else:

            await interaction.response.send_message('Você não tem permissão para usar isso', ephemeral = True)

class ban(discord.ui.View):
    
    def __init__(self, bot, membro, motivo, ctx):

        self.membro = membro

        self.bot = bot

        self.motivo = motivo

        self.ctx = ctx

        super().__init__(timeout = None)

    @discord.ui.button(label = '✅', style = discord.ButtonStyle.blurple)
    async def confirmban(self, button: discord.ui.Button, interaction: discord.Interaction):

        if discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['admin']) or discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['mod']) in interaction.user.roles:

            l1 = self.bot.get_channel(configData['logs']['mod'])

            guild = interaction.guild

            E = discord.Embed(title = 'Ban', description = f'Pessoa banida: {self.membro.name} \nQuem baniu: {self.ctx.mention}\nAprovado por: {interaction.user.mention} \nmotivo: {self.motivo} \nid: {self.membro.id}')

            await l1.send(embed = E)

            await interaction.message.delete()

            await interaction.response.send_message(f'{self.membro.name} banido com sucesso', ephemeral = True)

            await guild.ban(user = self.membro ,reason = self.motivo)

            self.stop()

        else:

            await interaction.response.send_message('Você não tem permissão para usar isso', ephemeral = True)


    @discord.ui.button(label = '❎', style = discord.ButtonStyle.blurple)
    async def denyban(self, button: discord.ui.Button, interaction: discord.Interaction):

        if discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['admin']) or discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['mod']) in interaction.user.roles:

            await interaction.message.delete()

            self.stop()

        else:

            await interaction.response.send_message('Você não tem permissão para usar isso', ephemeral = True)

class cmdstf(discord.ui.View):
    
    def __init__(self, bot):

        self.bot = bot

        super().__init__(timeout = None)

    @discord.ui.button(label = 'Ausencia', style = discord.ButtonStyle.blurple)
    async def ausente(self, button: discord.ui.Button, interaction: discord.Interaction):

        data_e_hora_atuais = datetime.now()

        fuso_horario = timezone('America/Sao_Paulo')

        data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)

        dt = data_e_hora_sao_paulo.strftime('%d/%m/%Y')

        def check(m):
            return m.content and m.author.id == interaction.user.id

        try:

            role = discord.utils.get(interaction.guild.roles, id = configData['roles']['outras']['standby'])

            ausente = self.bot.get_channel(configData['chats']['ausencia'])

            channel = self.bot.get_channel(configData['chats']['cmdstf'])

            if role not in interaction.user.roles:

                await interaction.response.send_message('Escreva o motivo de estar ausente', ephemeral = True)

                msg = await self.bot.wait_for('message', check = check, timeout = 130)

                await interaction.user.add_roles(role)

                await ausente.send(f'{interaction.user.name} entrou em ausencia às {dt}\nMotivo: {msg.content}')

                await channel.send(f'Agora você está ausente {interaction.user.mention}', delete_after = 2)

                await msg.delete()

                await ausendb(interaction.user,msg.content,dt)

                return

            if role in interaction.user.roles:

                await interaction.user.remove_roles(role)

                await ausente.send(f'{interaction.user.name} Saiu da ausencia às {dt}')

                await interaction.response.send_message('Você não está mais ausente', delete_after = 2, ephemeral = True)

                await desausendb(interaction.user)

                return
        
        except Exception:

            await ausente.send(f'{interaction.user.name} clicou no ausente mas não fez nada')

    @discord.ui.button(label = 'Ban', style = discord.ButtonStyle.blurple)
    async def ban(self, button: discord.ui.Button, interaction: discord.Interaction):

        if discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['staff']) not in interaction.user.roles:

            await interaction.response.send_message('Você não tem permissão para usar isso', ephemeral = True)

            return

        channel = self.bot.get_channel(configData['chats']['cmdstf'])

        def check(m):
            return m.content and m.author.id == interaction.user.id

        try:

            id = await channel.send('Mande o id da pessoa a banir')

            msg = await self.bot.wait_for('message', check = check, timeout = 130)

            membro = interaction.guild.get_member(int(msg.content))

            await id.delete()

            await msg.delete()

            def check2(m):
                return m.content and m.author.id == interaction.user.id

            try:

                id = await channel.send('Mande o motivo de banir o membro')

                msg2 = await self.bot.wait_for('message', check = check2, timeout = 130)

                await id.delete()

                await msg2.delete()

                e = discord.Embed(title = 'Ban')

                e.add_field(name = 'Pessoa a banir', value = f'{membro.mention}')

                e.add_field(name = 'Quem baniu', value = interaction.user.mention, inline = False)
                
                e.add_field(name = 'Motivo', value = msg2.content)

                await channel.send(embed = e, view = ban(self.bot,membro,msg2.content, interaction.user))

            except:
                print('error')

        except:
            print('error')
    
    @discord.ui.button(label = 'advertência', style = discord.ButtonStyle.blurple)
    async def advertência(self, button: discord.ui.Button, interaction: discord.Interaction):

        if discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['staff']) not in interaction.user.roles:

            await interaction.response.send_message('Você não tem permissão para usar isso', ephemeral = True)

            return

        await interaction.response.send_message('O que ira fazer?', ephemeral = True, view = adv1(self.bot))

    @discord.ui.button(label = 'cargos', style = discord.ButtonStyle.blurple)
    async def cargos(self, button: discord.ui.Button, interaction: discord.Interaction):

        if discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['admin']) in interaction.user.roles \
        or discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['mod']) in interaction.user.roles \
        or discord.utils.get(interaction.guild.roles, id = configData['roles']['equipes']['equipeeventos']['chefeeventos']) in interaction.user.roles \
        or discord.utils.get(interaction.guild.roles, id = configData['roles']['equipes']['equipecall']['submod']) in interaction.user.roles \
        or discord.utils.get(interaction.guild.roles, id = configData['roles']['equipes']['equipechat']['liderchat']) in interaction.user.roles \
        or discord.utils.get(interaction.guild.roles, id = configData['roles']['equipes']['equipediv']['promoters']) in interaction.user.roles \
        or discord.utils.get(interaction.guild.roles, id = configData['roles']['equipes']['equipemidia']['chefemidia']) in interaction.user.roles:

            await interaction.response.send_message('Oque ira fazer?', ephemeral = True, view = adcrmv(self.bot))

        else:
        
            await interaction.response.send_message('Você não tem permissão para usar isto', ephemeral = True)

            return