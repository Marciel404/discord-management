from ..db.mod import *

class adcadv(discord.ui.View):

    def __init__(self, bot, membro, motivo, ctx):

        self.motivo = motivo

        self.membro = membro

        self.bot = bot

        self.ctx = ctx

        super().__init__(timeout = None)

    @discord.ui.button(label = '✅'  , style = discord.ButtonStyle.blurple)
    async def adv(self, button: discord.ui.Button, interaction: discord.Interaction):

        data_e_hora_atuais = datetime.now()

        fuso_horario = timezone('America/Sao_Paulo')

        data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
        
        dt = data_e_hora_sao_paulo.strftime('%H:%M %d/%m/%Y')

        if discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['admin']) or discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['mod']) in interaction.user.roles:

            role1 = discord.utils.get(interaction.guild.roles, id = configData['roles']['adv']['adv1'])

            role2 = discord.utils.get(interaction.guild.roles, id = configData['roles']['adv']['adv2'])

            role3 = discord.utils.get(interaction.guild.roles, id = configData['roles']['adv']['adv3'])

            mute2 = discord.utils.get(interaction.guild.roles, id = configData['roles']['outras']['mute'])

            channel = self.bot.get_channel(configData['logs']['mod'])

            if role3 in self.membro.roles:

                E = discord.Embed(title = 'Ban', description = f'Pessoa banida: {self.membro.name} \n Quem baniu: {interaction.user.mention} \n motivo: Acumulo de adv')

                await channel.send(embed = E)

                await self.membro.ban(reason = 'Acumulo de advertencia')

                await interaction.message.delete()

                await interaction.response.send_message(f'{self.membro.name} advertido com sucesso e banido devido o acumulo de adv', ephemeral = True)

            if role2 in self.membro.roles:

                e = discord.Embed(title = 'Advertencia 3', description = f'{self.membro.mention} foi advertido por {self.ctx.mention} e aprovado por {interaction.user.mention}\nMotivo:{self.motivo}')
                
                await advdb(self.membro,3,f'{self.motivo} {dt}')

                await self.membro.add_roles(role3, reason = self.motivo)
                await self.membro.add_roles(mute2, reason = 'Adv3')

                await interaction.message.delete()

                await channel.send(embed = e)

                await asyncio.sleep(86400)

                await self.membro.remove_roles(mute2)

                return

            if role1 in self.membro.roles:

                e = discord.Embed(title = 'Advertencia 2', description = f'{self.membro.mention} foi advertido por {self.ctx.mention} e aprovado por {interaction.user.mention}\nMotivo:{self.motivo}')
                
                await advdb(self.membro,2,f'{self.motivo} {dt}')

                await self.membro.add_roles(role2, reason = self.motivo)
                await self.membro.add_roles(mute2, reason = 'Adv2')

                await interaction.message.delete()

                await channel.send(embed = e)

                await interaction.response.send_message(f'{self.membro} advertido com sucesso', ephemeral = True)

                await asyncio.sleep(10800)

                await self.membro.remove_roles(mute2)

                return

            if role1 not in self.membro.roles:

                e = discord.Embed(title = 'Advertencia 1', description = f'{self.membro.mention} foi advertido por {self.ctx.mention} e aprovado por {interaction.user.mention}\nMotivo:{self.motivo}')

                await advdb(self.membro,3,'None')

                await advdb(self.membro,2,'None')

                await advdb(self.membro,1,f'{self.motivo} {dt}')
                
                await self.membro.add_roles(role1, reason = self.motivo)

                await self.membro.add_roles(mute2, reason = 'Adv1')

                await interaction.message.delete()

                await channel.send(embed = e)

                await interaction.response.send_message(f'{self.membro} advertido com sucesso', ephemeral = True)

                await asyncio.sleep(3600)

                await self.membro.remove_roles(mute2)

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

class adccap(discord.ui.View):

    def __init__(self,bot, membro, cargo, inter):

        self.cargo = cargo

        self.membro = membro

        self.bot = bot

        self.inter = inter

        super().__init__(timeout = None)

    @discord.ui.button(label = '✅'  , style = discord.ButtonStyle.blurple)
    async def adc(self, button: discord.ui.Button, interaction: discord.Interaction):

        channel = self.bot.get_channel(configData['logs']['cargos'])

        admin = discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['admin'])

        e = discord.Embed(title = 'Adição cargo')

        e.add_field(name = 'Qual cargo adicionado', value = self.cargo.mention)

        e.add_field(name = 'Quem adicionou', value = self.inter.mention, inline = False)

        e.add_field(name = 'Foi adicionado a', value = self.membro.mention)

        e.add_field(name = 'Aprovado por', value = interaction.user.mention, inline = False)

        if admin in interaction.user.roles:

            await self.membro.add_roles(self.cargo)

            await interaction.message.delete()

            await channel.send(embed = e)

        else:

            await interaction.response.send_message('Você não tem permissão para usar isso', ephemeral = True)

    @discord.ui.button(label = '❎', style = discord.ButtonStyle.blurple)
    async def cancel(self, button: discord.ui.Button, interaction: discord.Interaction):

        if discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['admin']) or discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['mod']) in interaction.user.roles:
        
            await interaction.message.delete()

            self.stop()

        else:

            await interaction.response.send_message('Você não tem permissão para usar isso', ephemeral = True)

class adccargo(discord.ui.View):

    def __init__(self,bot, membro, cargo, inter):

        self.cargo = cargo

        self.membro = membro

        self.bot = bot

        self.inter = inter

        super().__init__(timeout = None)

    @discord.ui.button(label = '✅'  , style = discord.ButtonStyle.blurple)
    async def adc(self, button: discord.ui.Button, interaction: discord.Interaction):

        channel = self.bot.get_channel(configData['logs']['cargos'])

        admin = discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['admin'])

        mod = discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['mod'])

        e = discord.Embed(title = 'Adição cargo')

        e.add_field(name = 'Qual cargo adicionado', value = self.cargo.mention)

        e.add_field(name = 'Quem adicionou', value = self.inter.mention, inline = False)

        e.add_field(name = 'Foi adicionado a', value = self.membro.mention)

        e.add_field(name = 'Aprovado por', value = interaction.user.mention, inline = False)

        if admin in interaction.user.roles \
        or mod in interaction.user.roles:

            await self.membro.add_roles(self.cargo)

            await interaction.message.delete()

            await channel.send(embed = e)

        else:

            await interaction.response.send_message('Você não tem permissão para usar isso', ephemeral = True)

    @discord.ui.button(label = '❎', style = discord.ButtonStyle.blurple)
    async def cancel(self, button: discord.ui.Button, interaction: discord.Interaction):

        if discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['admin']) or discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['mod']) in interaction.user.roles:
        
            await interaction.message.delete()

            self.stop()

        else:

            await interaction.response.send_message('Você não tem permissão para usar isso', ephemeral = True)

class rmvcap(discord.ui.View):

    def __init__(self,bot, membro, cargo, inter):

        self.cargo = cargo

        self.membro = membro

        self.bot = bot

        self.inter = inter

        super().__init__(timeout = None)

    @discord.ui.button(label = '✅'  , style = discord.ButtonStyle.blurple)
    async def rmv(self, button: discord.ui.Button, interaction: discord.Interaction):

        channel = self.bot.get_channel(configData['logs']['cargos'])

        admin = discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['admin'])

        e = discord.Embed(title = 'Adição cargo')

        e.add_field(name = 'Qual cargo removido', value = self.cargo.mention)

        e.add_field(name = 'Quem removeu', value = self.inter.mention, inline = False)

        e.add_field(name = 'Foi removido de', value = self.membro.mention)

        e.add_field(name = 'Aprovado por', value = interaction.user.mention, inline = False)

        if admin in interaction.user.roles:

            await self.membro.remove_roles(self.cargo)

            await interaction.message.delete()

            await channel.send(embed = e)

        else:

            await interaction.response.send_message('Você não tem permissão para usar isso', ephemeral = True)

    @discord.ui.button(label = '❎', style = discord.ButtonStyle.blurple)
    async def cancel(self, button: discord.ui.Button, interaction: discord.Interaction):

        if discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['admin']) or discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['mod']) in interaction.user.roles:
        
            await interaction.message.delete()

            self.stop()

        else:

            await interaction.response.send_message('Você não tem permissão para usar isso', ephemeral = True)

class rmvcargo(discord.ui.View):

    def __init__(self,bot, membro, cargo, inter):

        self.cargo = cargo

        self.membro = membro

        self.bot = bot

        self.inter = inter

        super().__init__(timeout = None)

    @discord.ui.button(label = '✅'  , style = discord.ButtonStyle.blurple)
    async def rmv(self, button: discord.ui.Button, interaction: discord.Interaction):

        channel = self.bot.get_channel(configData['logs']['cargos'])

        admin = discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['admin'])

        mod = discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['mod'])

        e = discord.Embed(title = 'Remoção cargo')

        e.add_field(name = 'Qual cargo removido', value = self.cargo.mention)

        e.add_field(name = 'Quem removeu', value = self.inter.mention, inline = False)

        e.add_field(name = 'Foi removido de', value = self.membro.mention)

        e.add_field(name = 'Aprovado por', value = interaction.user.mention, inline = False)

        if admin in interaction.user.roles \
        or mod in interaction.user.roles:

            await self.membro.remove_roles(self.cargo)

            await interaction.message.delete()

            await channel.send(embed = e)

        else:

            await interaction.response.send_message('Você não tem permissão para usar isso', ephemeral = True)

    @discord.ui.button(label = '❎', style = discord.ButtonStyle.blurple)
    async def cancel(self, button: discord.ui.Button, interaction: discord.Interaction):

        if discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['admin']) or discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['mod']) in interaction.user.roles:
        
            await interaction.message.delete()

            self.stop()

        else:

            await interaction.response.send_message('Você não tem permissão para usar isso', ephemeral = True)