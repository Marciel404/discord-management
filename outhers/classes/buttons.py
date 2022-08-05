import discord, asyncio
from outhers.info.fi import configData
from outhers.db.mod import *
from outhers.classes.selectmenus import *

class adv(discord.ui.View):

    def __init__(self, bot, membro, motivo, ctx):

        self.motivo = motivo

        self.membro = membro

        self.bot = bot

        self.ctx = ctx

        super().__init__(timeout = None)

    @discord.ui.button(label = '✅'  , style = discord.ButtonStyle.blurple)
    async def adv(self, button: discord.ui.Button, interaction: discord.Interaction):

        if discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['admin']) or discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['mod']) in interaction.user.roles:

            role1 = discord.utils.get(interaction.guild.roles, id = configData['roles']['adv']['adv1'])

            role2 = discord.utils.get(interaction.guild.roles, id = configData['roles']['adv']['adv2'])

            role3 = discord.utils.get(interaction.guild.roles, id = configData['roles']['adv']['adv3'])

            mute = discord.utils.get(interaction.guild.roles, id = configData['roles']['outras']['mute'])

            channel = self.bot.get_channel(configData['logs']['mod'])

            if role3 in self.membro.roles:

                E = discord.Embed(title = 'Ban', description = f'Pessoa banida: {self.membro.name} \n Quem baniu: {interaction.user.mention} \n motivo: Acumulo de adv')

                await channel.send(embed = E)

                await self.membro.ban(reason = 'Acumulo de advertencia')

                await interaction.message.delete()

                await interaction.response.send_message(f'{self.membro.name} advertido com sucesso e banido devido o acumulo de adv', ephemeral = True)


            if role2 in self.membro.roles:

                e = discord.Embed(title = 'Advertencia 3', description = f'{self.membro.mention} foi advertido por {self.ctx.mention} e aprovado por {interaction.user.mention}\nMotivo:{self.motivo}')
                
                await advdb(self.membro,3,self.motivo)

                await self.membro.add_roles(role3, reason = self.motivo)
                await self.membro.add_roles(mute, reason = 'Adv3')

                await interaction.message.delete()

                await channel.send(embed = e)

                await asyncio.sleep(86400)

                await self.membro.remove_roles(mute)

                return

            if role1 in self.membro.roles:

                e = discord.Embed(title = 'Advertencia 2', description = f'{self.membro.mention} foi advertido por {self.ctx.mention} e aprovado por {interaction.user.mention}\nMotivo:{self.motivo}')
                
                await advdb(self.membro,2,self.motivo)

                await self.membro.add_roles(role2, reason = self.motivo)
                await self.membro.add_roles(mute, reason = 'Adv2')

                await interaction.message.delete()

                await channel.send(embed = e)

                await interaction.response.send_message(f'{self.membro} advertido com sucesso', ephemeral = True)

                await asyncio.sleep(10800)

                await self.membro.remove_roles(mute)

                return

            if role1 not in self.membro.roles:

                e = discord.Embed(title = 'Advertencia 1', description = f'{self.membro.mention} foi advertido por {self.ctx.mention} e aprovado por {interaction.user.mention}\nMotivo:{self.motivo}')

                await advdb(self.membro,3,'None')

                await advdb(self.membro,2,'None')

                await advdb(self.membro,1,self.motivo)
                
                await self.membro.add_roles(role1, reason = self.motivo)

                await self.membro.add_roles(mute, reason = 'Adv1')

                await interaction.message.delete()

                await channel.send(embed = e)

                await interaction.response.send_message(f'{self.membro} advertido com sucesso', ephemeral = True)

                await asyncio.sleep(3600)

                await self.membro.remove_roles(mute)

                return
        else:

            await interaction.response.send_message('Você não tem permissão para usar isso', ephemeral = True)

    @discord.ui.button(label = '❎', style = discord.ButtonStyle.blurple)
    async def cancel(self, button: discord.ui.Button, interaction: discord.Interaction):

        if discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['admin']) or discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['mod']) in interaction.user.roles:
        
            await interaction.message.delete()


            self.stop()

        else:

            await interaction.response.send_message('Você não tem permissão para usar isso', ephemeral = True)

class rmvadv(discord.ui.View):

    def __init__(self, bot, membro):

        self.membro = membro

        self.bot = bot

        super().__init__(timeout = None)

    @discord.ui.button(label = '✅'  , style = discord.ButtonStyle.blurple)
    async def rmvadv(self, button: discord.ui.Button, interaction: discord.Interaction):

        if discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['admin']) or discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['mod']) in interaction.user.roles:

            await interaction.message.delete()

            membro = self.membro

            role1 = discord.utils.get(interaction.guild.roles, id = configData['roles']['adv']['adv1'])

            role2 = discord.utils.get(interaction.guild.roles, id = configData['roles']['adv']['adv2'])

            role3 = discord.utils.get(interaction.guild.roles, id = configData['roles']['adv']['adv3'])

            channel = self.bot.get_channel(configData['logs']['mod'])

            mute = discord.utils.get(interaction.guild.roles, id = configData['roles']['outras']['mute'])

            e = discord.Embed(title = 'Remoção adv', description = f'{interaction.user.mention} removeu uma advertencia de {membro.mention}')

            if role3 in membro.roles:
                
                await rmvadvdb(membro,3, 'None')

                await membro.remove_roles(role3)

                await channel.send(embed = e)

                await interaction.response.send_message('Advertência removida com sucesso', ephemeral = True)

                await self.membro.remove_roles(mute)

                return

            elif role2 in membro.roles:
                
                await rmvadvdb(membro,2,'None')

                await membro.remove_roles(role2)

                await channel.send(embed = e)

                await interaction.response.send_message('Advertência removida com sucesso', ephemeral = True)

                await self.membro.remove_roles(mute)

                return

            elif role1 in membro.roles:

                await rmvadvdb(membro,1,'None')
                
                await membro.remove_roles(role1)

                await channel.send(embed = e)

                await interaction.response.send_message('Advertência removida com sucesso', ephemeral = True)

                await self.membro.remove_roles(mute)

                return

            elif discord.utils.get(interaction.guild.roles, id = configData['roles']['adv']['adv1']) not in membro.roles:

                await interaction.response.send_message('Esse membro não possue advertencias', delete_after = 3)

                return
        else:

            await interaction.response.send_message('Você não tem permissão para usar isso', ephemeral = True)

    @discord.ui.button(label = '❎', style = discord.ButtonStyle.blurple)
    async def cancel(self, button: discord.ui.Button, interaction: discord.Interaction):

        if discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['admin']) or discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['mod']) in interaction.user.roles:
        
            await interaction.message.delete()

            self.stop()

        else:

            await interaction.response.send_message('Você não tem permissão para usar isso', ephemeral = True)

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

            channel = await guild.create_text_channel(name=ticket, 
            overwrites = overwrites, 
            category = discord.utils.get(interaction.guild.categories, id = configData['catego']['ticket']))

            await interaction.response.send_message('Ticket criado com sucesso', ephemeral = True)

            await channel.send(view=adonticket(member))

            await channel.send(f'{interaction.user.mention} {suporte.mention}')
        
        else:

            await interaction.send_message('Ticket já existente, encerre o ultimo para criar outro', ephemeral = True)

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
        dt = data_e_hora_sao_paulo.strftime('%H:%M %d/%m/%Y')

        def check(m):
            return m.content and m.author.id == interaction.user.id

        try:

            role = discord.utils.get(interaction.guild.roles, id = configData['roles']['outras']['standby'])

            ausente = self.bot.get_channel(configData['chats']['ausencia'])

            channel = self.bot.get_channel(configData['chats']['cmdstf'])


            if role not in interaction.user.roles:

                ausente2 = await channel.send('Escreva o motivo de estar ausente')

                msg = await self.bot.wait_for('message', check = check, timeout = 130)

                await ausente2.delete()

                await interaction.user.add_roles(role)

                await ausente.send(f'{interaction.user.name} entrou em ausencia às {dt}\nMotivo: {msg.content}')

                await channel.send(f'Agora você está ausente {interaction.user.mention}', delete_after = 2)

                await msg.delete()

                return

            if role in interaction.user.roles:

                await interaction.user.remove_roles(role)

                await ausente.send(f'{interaction.user.name} Saiu da ausencia às {dt}')

                await channel.send('Você não está mais ausente', delete_after = 2)

                return
        
        except Exception:

            await ausente2.delete()

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

                print(msg2.content)

                e = discord.Embed(title = 'Ban')

                e.add_field(name = 'Pessoa a banir', value = f'{membro.mention}')
                e.add_field(name = 'Quem baniu', value = interaction.user.mention, inline = False)
                e.add_field(name = 'Motivo', value = msg2.content)

                await channel.send(embed = e, view = ban(self.bot,membro,msg2.content, interaction.user))

                print(msg.content, msg2.content)

            except:
                print('error')

        except:
            print('error')
    
    @discord.ui.button(label = 'advertência', style = discord.ButtonStyle.blurple)
    async def advertência(self, button: discord.ui.Button, interaction: discord.Interaction):

        if discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['staff']) not in interaction.user.roles:

            await interaction.response.send_message('Você não tem permissão para usar isso', ephemeral = True)

            return

        channel = self.bot.get_channel(configData['chats']['cmdstf'])

        def check(m):
            return m.content and m.author.id == interaction.user.id

        try:

            id50 = await channel.send('Escreva "adc" para adicionar ou "rmv" para remover uma advertência')

            ms = await self.bot.wait_for('message', check = check, timeout = 130)

            await id50.delete()

            await ms.delete()

            if ms.content.lower() == 'adc':

                def check(m):
                    return m.content and m.author.id == interaction.user.id

                try:

                    id = await channel.send('Mande o id da pessoa a adverter')

                    msg = await self.bot.wait_for('message', check = check, timeout = 130)

                    membro = interaction.guild.get_member(int(msg.content))

                    await id.delete()

                    await msg.delete()

                    def check2(m):
                        return m.content and m.author.id == interaction.user.id

                    try:

                        id = await channel.send('Mande o motivo de adverter o membro')

                        msg2 = await self.bot.wait_for('message', check = check2, timeout = 130)

                        await id.delete()

                        await msg2.delete()

                        print(msg2.content)

                        e = discord.Embed(title = 'Advertencia')

                        e.add_field(name = 'Pessoa a adverter', value = f'{membro.mention}')
                        e.add_field(name = 'Quem adverteu', value = interaction.user.mention, inline = False)
                        e.add_field(name = 'Motivo', value = msg2.content)

                        await channel.send(embed = e, view = adv(self.bot,membro,msg2.content, interaction.user))

                    except:
                        print('error')

                except:
                    print('error')
            
            elif ms.content.lower() == 'rmv':

                def check50(m):
                    return m.content and m.author.id == interaction.user.id

                try:

                    id70 = await channel.send('Mande o id da pessoa a remover a advertencia')

                    msg50 = await self.bot.wait_for('message', check = check50, timeout = 130)

                    membro = interaction.guild.get_member(int(msg50.content))

                    await id70.delete()

                    await msg50.delete()

                    e = discord.Embed(title = 'Advertencia')

                    e.add_field(name = 'Remover advertencia de ', value = f'{membro.mention}')
                    e.add_field(name = 'Quem removeu ', value = interaction.user.mention, inline = False)

                    await channel.send(embed = e, view = rmvadv(self.bot,membro))

                except:

                    print('error')
        except:

            print('error')

    @discord.ui.button(label = 'cargos', style = discord.ButtonStyle.blurple)
    async def cargos(self, button: discord.ui.Button, interaction: discord.Interaction):

        capeventos = discord.utils.get(interaction.guild.roles, id = configData['roles']['equipes']['equipeeventos']['chefeeventos'])

        capcall = discord.utils.get(interaction.guild.roles, id = configData['roles']['equipes']['equipecall']['submod'])

        capchat = discord.utils.get(interaction.guild.roles, id = configData['roles']['equipes']['equipechat']['liderchat'])

        capdiv = discord.utils.get(interaction.guild.roles, id = configData['roles']['equipes']['equipediv']['promoters'])

        admin = discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['admin'])
            
        mod = discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['mod'])

        if admin in interaction.user.roles \
        or mod in interaction.user.roles \
        or capeventos in interaction.user.roles \
        or capcall in interaction.user.roles \
        or capchat in interaction.user.roles \
        or capdiv in interaction.user.roles:

            await interaction.response.send_message('Em qual equipe vai adicionar o cargo?', ephemeral = True, view = cargos1(self.bot))

        else:
        
            await interaction.response.send_message('Você não tem permissão para usar isto', ephemeral = True)

            return
