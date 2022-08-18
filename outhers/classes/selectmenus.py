from ..info.fi import configData, discord
from .selectbutons import *

class cargoevento(discord.ui.View):

    def __init__(self, bot , timeout = 300):

        self.bot = bot

        super().__init__(timeout=timeout)

    @discord.ui.select(
        placeholder = "Cargos",
        options = [
            discord.SelectOption(
                label = 'Chefe eventos',
                description = 'Adiciona o cargo de chefe de eventos',
            ),
            discord.SelectOption(
                label = 'Apresentador',
                description = 'Adiciona o cargo de apresentador'
            )
        ]
    )
    async def select_callback(self,  select, interaction : discord.Interaction):

        channel = self.bot.get_channel(configData['chats']['cmdstf'])

        admin = discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['admin'])
            
        mod = discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['mod'])

        capeventos = discord.utils.get(interaction.guild.roles, id = configData['roles']['equipes']['equipeeventos']['chefeeventos'])

        apresentador = discord.utils.get(interaction.guild.roles, id = configData['roles']['equipes']['equipeeventos']['apresentador'])

        if select.values[0] == 'Chefe eventos':

            if admin in interaction.user.roles \
            or mod in interaction.user.roles:

                await interaction.response.send_message('Mande no chat o id da pessoa a receber o cargo', ephemeral = True)

                def check50(m):
                    return m.content and m.author.id == interaction.user.id

                msg50 = await self.bot.wait_for('message', check = check50, timeout = 130)

                membro = interaction.guild.get_member(int(msg50.content))

                await msg50.delete()

                e = discord.Embed(title = 'Adicionar cargo de Chefe de eventos')

                e.add_field(name = 'Quem vai ser adicionado o cargo', value = f'{membro.mention}')
                
                e.add_field(name = 'Quem adicionou ', value = interaction.user.mention, inline = False)

                await channel.send(embed = e, view = adccap(self.bot, membro, capeventos, interaction.user))

                self.stop()

            else:

                interaction.response.send_message('Você não tem permissão para usar isto', ephemeral = True)

                return

        if select.values[0] == 'Apresentador':


            await interaction.response.send_message('Mande no chat o id da pessoa a receber o cargo', ephemeral = True)
            
            def check50(m):
                return m.content and m.author.id == interaction.user.id

            msg50 = await self.bot.wait_for('message', check = check50, timeout = 130)

            membro = interaction.guild.get_member(int(msg50.content))

            await msg50.delete()

            e = discord.Embed(title = 'Adicionar cargo de Chefe de eventos')

            e.add_field(name = 'Quem vai ser adicionado o cargo', value = f'{membro.mention}')

            e.add_field(name = 'Quem adicionou ', value = interaction.user.mention, inline = False)

            await channel.send(embed = e, view = adccargo(self.bot, membro, apresentador, interaction.user))

            self.stop()

class cargocall(discord.ui.View):

    def __init__(self, bot , timeout = 300):

        self.bot = bot

        super().__init__(timeout=timeout)

    @discord.ui.select(
        placeholder = "Cargos",
        options = [
            discord.SelectOption(
                label = 'Sub mod',
                description = 'Adiciona o cargo de sub mod',
            ),
            discord.SelectOption(
                label = 'Staff call',
                description = 'Adiciona o cargo de staff call'
            ),
            discord.SelectOption(
                label = 'Movimentação',
                description = 'Adiciona o cargo de movimentação'
            )
        ]
    )
    async def select_callback(self,  select, interaction : discord.Interaction):

        channel = self.bot.get_channel(configData['chats']['cmdstf'])

        admin = discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['admin'])
            
        mod = discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['mod'])

        submod = discord.utils.get(interaction.guild.roles, id = configData['roles']['equipes']['equipecall']['submod'])

        staffcall = discord.utils.get(interaction.guild.roles, id = configData['roles']['equipes']['equipecall']['staffcall'])

        movi =  discord.utils.get(interaction.guild.roles, id = configData['roles']['equipes']['equipecall']['movimenta'])

        if select.values[0] == 'Sub mod':

            if admin in interaction.user.roles \
            or mod in interaction.user.roles:

                await interaction.response.send_message('Mande no chat o id da pessoa a receber o cargo', ephemeral = True)

                def check50(m):
                    return m.content and m.author.id == interaction.user.id

                msg50 = await self.bot.wait_for('message', check = check50, timeout = 130)

                membro = interaction.guild.get_member(int(msg50.content))

                await msg50.delete()

                e = discord.Embed(title = 'Adicionar cargo de Chefe de eventos')

                e.add_field(name = 'Quem vai ser adicionado o cargo', value = f'{membro.mention}')
                e.add_field(name = 'Quem adicionou ', value = interaction.user.mention, inline = False)

                await channel.send(embed = e, view = adccap(self.bot, membro, submod, interaction.user))

                self.stop()

            else:

                interaction.response.send_message('Você não tem permissão para usar isto', ephemeral = True)

                return

        if select.values[0] == 'Staff call':

            await interaction.response.send_message('Mande no chat o id da pessoa a receber o cargo', ephemeral = True)

            def check50(m):
                return m.content and m.author.id == interaction.user.id

            msg50 = await self.bot.wait_for('message', check = check50, timeout = 130)

            membro = interaction.guild.get_member(int(msg50.content))

            await msg50.delete()

            e = discord.Embed(title = 'Adicionar cargo de Chefe de eventos')

            e.add_field(name = 'Quem vai ser adicionado o cargo', value = f'{membro.mention}')
            e.add_field(name = 'Quem adicionou ', value = interaction.user.mention, inline = False)

            await channel.send(embed = e, view = adccargo(self.bot, membro, staffcall, interaction.user))

            self.stop()

        if select.values[0] == 'Movimentação':

            await interaction.response.send_message('Mande no chat o id da pessoa a receber o cargo', ephemeral = True)

            def check50(m):
                return m.content and m.author.id == interaction.user.id

            msg50 = await self.bot.wait_for('message', check = check50, timeout = 130)

            membro = interaction.guild.get_member(int(msg50.content))

            await msg50.delete()

            e = discord.Embed(title = 'Adicionar cargo de Chefe de eventos')

            e.add_field(name = 'Quem vai ser adicionado o cargo', value = f'{membro.mention}')
            e.add_field(name = 'Quem adicionou ', value = interaction.user.mention, inline = False)

            await channel.send(embed = e, view = adccargo(self.bot, membro, movi, interaction.user))

            self.stop()

class cargochat(discord.ui.View):

    def __init__(self, bot , timeout = 300):

        self.bot = bot

        super().__init__(timeout=timeout)

    @discord.ui.select(
        placeholder = "Cargos",
        options = [
            discord.SelectOption(
                label = 'Lider chat',
                description = 'Adiciona o cargo de Lider chat',
            ),
            discord.SelectOption(
                label = 'Staff chat',
                description = 'Adiciona o cargo de Staff chat'
            ),
            discord.SelectOption(
                label = 'Movimentação',
                description = 'Adiciona o cargo de movimentação'
            )
        ]
    )
    async def select_callback(self,  select, interaction : discord.Interaction):

        channel = self.bot.get_channel(configData['chats']['cmdstf'])

        admin = discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['admin'])
            
        mod = discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['mod'])

        liderchat = discord.utils.get(interaction.guild.roles, id = configData['roles']['equipes']['equipechat']['liderchat'])

        staffchat = discord.utils.get(interaction.guild.roles, id = configData['roles']['equipes']['equipechat']['staffchat'])

        movi =  discord.utils.get(interaction.guild.roles, id = configData['roles']['equipes']['equipechat']['movimenta'])

        if select.values[0] == 'Lider chat':

            if admin in interaction.user.roles \
            or mod in interaction.user.roles:

                await interaction.response.send_message('Mande no chat o id da pessoa a receber o cargo', ephemeral = True)

                def check50(m):
                    return m.content and m.author.id == interaction.user.id

                msg50 = await self.bot.wait_for('message', check = check50, timeout = 130)

                membro = interaction.guild.get_member(int(msg50.content))

                await msg50.delete()

                e = discord.Embed(title = 'Adicionar cargo de Chefe de eventos')

                e.add_field(name = 'Quem vai ser adicionado o cargo', value = f'{membro.mention}')
                e.add_field(name = 'Quem adicionou ', value = interaction.user.mention, inline = False)

                await channel.send(embed = e, view = adccap(self.bot, membro, liderchat, interaction.user))

                self.stop()

            else:

                interaction.response.send_message('Você não tem permissão para usar isto', ephemeral = True)

                return

        if select.values[0] == 'Staff chat':

            await interaction.response.send_message('Mande no chat o id da pessoa a receber o cargo', ephemeral = True)

            def check50(m):
                return m.content and m.author.id == interaction.user.id

            msg50 = await self.bot.wait_for('message', check = check50, timeout = 130)

            membro = interaction.guild.get_member(int(msg50.content))

            await msg50.delete()

            e = discord.Embed(title = 'Adicionar cargo de Chefe de eventos')

            e.add_field(name = 'Quem vai ser adicionado o cargo', value = f'{membro.mention}')
            e.add_field(name = 'Quem adicionou ', value = interaction.user.mention, inline = False)

            await channel.send(embed = e, view = adccargo(self.bot, membro, staffchat, interaction.user))

            self.stop()

        if select.values[0] == 'Movimentação':

            await interaction.response.send_message('Mande no chat o id da pessoa a receber o cargo', ephemeral = True)

            def check50(m):
                return m.content and m.author.id == interaction.user.id

            msg50 = await self.bot.wait_for('message', check = check50, timeout = 130)

            membro = interaction.guild.get_member(int(msg50.content))

            await msg50.delete()

            e = discord.Embed(title = 'Adicionar cargo de Chefe de eventos')

            e.add_field(name = 'Quem vai ser adicionado o cargo', value = f'{membro.mention}')
            e.add_field(name = 'Quem adicionou ', value = interaction.user.mention, inline = False)

            await channel.send(embed = e, view = adccargo(self.bot, membro, movi, interaction.user))

            self.stop()

class cargodiv(discord.ui.View):

    def __init__(self, bot , timeout = 300):

        self.bot = bot

        super().__init__(timeout=timeout)

    @discord.ui.select(
        placeholder = "Cargos",
        options = [
            discord.SelectOption(
                label = 'Promoters',
                description = 'Adiciona o cargo de promoters',
            ),
            discord.SelectOption(
                label = 'Divulgação',
                description = 'Adiciona o cargo de divulgação'
            )
        ]
    )
    async def select_callback(self,  select, interaction : discord.Interaction):

        channel = self.bot.get_channel(configData['chats']['cmdstf'])

        admin = discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['admin'])
            
        mod = discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['mod'])

        promoters = discord.utils.get(interaction.guild.roles, id = configData['roles']['equipes']['equipediv']['promoters'])

        divulgação = discord.utils.get(interaction.guild.roles, id = configData['roles']['equipes']['equipediv']['div'])

        if select.values[0] == 'Promoters':

            if admin in interaction.user.roles \
            or mod in interaction.user.roles:

                await interaction.response.send_message('Mande no chat o id da pessoa a receber o cargo', ephemeral = True)

                def check50(m):
                    return m.content and m.author.id == interaction.user.id

                msg50 = await self.bot.wait_for('message', check = check50, timeout = 130)

                membro = interaction.guild.get_member(int(msg50.content))

                await msg50.delete()

                e = discord.Embed(title = 'Adicionar cargo de Chefe de eventos')

                e.add_field(name = 'Quem vai ser adicionado o cargo', value = f'{membro.mention}')
                e.add_field(name = 'Quem adicionou ', value = interaction.user.mention, inline = False)

                await channel.send(embed = e, view = adccap(self.bot, membro, promoters, interaction.user))

                self.stop()

            else:

                interaction.response.send_message('Você não tem permissão para usar isto', ephemeral = True)

                return

        if select.values[0] == 'Divulgação':

            await interaction.response.send_message('Mande no chat o id da pessoa a receber o cargo', ephemeral = True)

            def check50(m):
                return m.content and m.author.id == interaction.user.id

            msg50 = await self.bot.wait_for('message', check = check50, timeout = 130)

            membro = interaction.guild.get_member(int(msg50.content))

            await msg50.delete()

            e = discord.Embed(title = 'Adicionar cargo de Chefe de eventos')

            e.add_field(name = 'Quem vai ser adicionado o cargo', value = f'{membro.mention}')
            e.add_field(name = 'Quem adicionou ', value = interaction.user.mention, inline = False)

            await channel.send(embed = e, view = adccargo(self.bot, membro, divulgação, interaction.user))

            self.stop()

class cargomidia(discord.ui.View):

    def __init__(self, bot , timeout = 300):

        self.bot = bot

        super().__init__(timeout=timeout)

    @discord.ui.select(
        placeholder = "Cargos",
        options = [
            discord.SelectOption(
                label = 'Lider de midia',
                description = 'Adiciona o cargo de lider de midia',
            ),
            discord.SelectOption(
                label = 'Equipe de midia',
                description = 'Adiciona o cargo de equipe de midia'
            )
        ]
    )
    async def select_callback(self, select, interaction: discord.Interaction):

        channel = self.bot.get_channel(configData['chats']['cmdstf'])

        admin = discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['admin'])
            
        mod = discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['mod'])

        chefemidia = discord.utils.get(interaction.guild.roles, id = configData['roles']['equipes']['equipemidia']['chefemidia'])

        equipemidia = discord.utils.get(interaction.guild.roles, id = configData['roles']['equipes']['equipemidia']['equipemidia'])

        if select.values[0] == 'Lider de midia':

            if admin in interaction.user.roles \
            or mod in interaction.user.roles:

                await interaction.response.send_message('Mande no chat o id da pessoa a receber o cargo', ephemeral = True)

                def check50(m):
                    return m.content and m.author.id == interaction.user.id

                msg50 = await self.bot.wait_for('message', check = check50, timeout = 130)

                membro = interaction.guild.get_member(int(msg50.content))

                await msg50.delete()

                e = discord.Embed(title = 'Adicionar cargo de Chefe de eventos')

                e.add_field(name = 'Quem vai ser adicionado o cargo', value = f'{membro.mention}')
                e.add_field(name = 'Quem adicionou ', value = interaction.user.mention, inline = False)

                await channel.send(embed = e, view = adccap(self.bot, membro, chefemidia, interaction.user))

                self.stop()

            else:

                interaction.response.send_message('Você não tem permissão para usar isto', ephemeral = True)

                return

        if select.values[0] == 'Equipe de midia':

            await interaction.response.send_message('Mande no chat o id da pessoa a receber o cargo', ephemeral = True)

            def check50(m):
                return m.content and m.author.id == interaction.user.id

            msg50 = await self.bot.wait_for('message', check = check50, timeout = 130)

            membro = interaction.guild.get_member(int(msg50.content))

            await msg50.delete()

            e = discord.Embed(title = 'Adicionar cargo de Chefe de eventos')

            e.add_field(name = 'Quem vai ser adicionado o cargo', value = f'{membro.mention}')
            e.add_field(name = 'Quem adicionou ', value = interaction.user.mention, inline = False)

            await channel.send(embed = e, view = adccargo(self.bot, membro, equipemidia, interaction.user))

            self.stop()

class cargos1(discord.ui.View):

    def __init__(self, bot, timeout = 300):

        self.bot = bot

        super().__init__(timeout=timeout)

    @discord.ui.select(
        placeholder = "Cargos",
        options = [
            discord.SelectOption(
                label = 'Eventos',
                description = 'Cargos da equipe de eventos',
            ),
            discord.SelectOption(
                label = 'Call',
                description = 'Cargos da equipe de call'
            ),
            discord.SelectOption(
                label = 'Chat',
                description = 'Cargos da equipe de chat'
            ),
            discord.SelectOption(
                label = 'Divulgação',
                description = 'Cargos da equipe de call'
            ),
            discord.SelectOption(
                label = 'Midia',
                description = 'Cargos da equipe de Midia'
            )
        ]
    )
    async def select_callback(self, select, interaction: discord.Interaction):

        capeventos = discord.utils.get(interaction.guild.roles, id = configData['roles']['equipes']['equipeeventos']['chefeeventos'])

        capcall = discord.utils.get(interaction.guild.roles, id = configData['roles']['equipes']['equipecall']['submod'])

        capchat = discord.utils.get(interaction.guild.roles, id = configData['roles']['equipes']['equipechat']['liderchat'])

        capdiv = discord.utils.get(interaction.guild.roles, id = configData['roles']['equipes']['equipediv']['promoters'])

        capmidia = discord.utils.get(interaction.guild.roles, id = configData['roles']['equipes']['equipemidia']['chefemidia'])

        admin = discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['admin'])
            
        mod = discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['mod'])

        if select.values[0] == 'Eventos':

            if capeventos in interaction.user.roles \
            or admin in interaction.user.roles \
            or mod in interaction.user.roles:

                await interaction.response.send_message('Qual cargo vai adicionar?', ephemeral = True, view = cargoevento(self.bot))

                self.stop()

            else:

                await interaction.response.send_message('Você não tem permissão para usar isto', ephemeral = True)

                return

        elif select.values[0] == 'Call':

            if capcall in interaction.user.roles \
            or admin in interaction.user.roles \
            or mod in interaction.user.roles:

                await interaction.response.send_message('Qual cargo vai adicionar?', ephemeral = True, view = cargocall(self.bot))

                self.stop()

            else:

                await interaction.response.send_message('Você não tem permissão para usar isto', ephemeral = True)

                return

        elif select.values[0] == 'Chat':

            if capchat in interaction.user.roles \
            or admin in interaction.user.roles \
            or mod in interaction.user.roles:

                await interaction.response.send_message('Qual cargo vai adicionar?', ephemeral = True, view = cargochat(self.bot))

                self.stop()

            else:

                await interaction.response.send_message('Você não tem permissão para usar isto', ephemeral = True)

                return

        elif select.values[0] == 'Divulgação':

            if capdiv in interaction.user.roles \
            or admin in interaction.user.roles \
            or mod in interaction.user.roles:

                await interaction.response.send_message('Qual cargo vai adicionar?', ephemeral = True, view = cargodiv(self.bot))

                self.stop()

            else:

                await interaction.response.send_message('Você não tem permissão para usar isto', ephemeral = True)

                return

        elif select.values[0] == 'Midia':

            if capmidia in interaction.user.roles \
            or admin in interaction.user.roles \
            or mod in interaction.user.roles:

                await interaction.response.send_message('Qual cargo vai adicionar?', ephemeral = True, view = cargomidia(self.bot))

                self.stop()

            else:

                await interaction.response.send_message('Você não tem permissão para usar isto', ephemeral = True)

                return

class adv1(discord.ui.View):

    def __init__(self, bot, timeout = 300):

        self.bot = bot

        super().__init__(timeout=timeout)

    @discord.ui.select(
    placeholder = "Advivertencia",
    options = [
        discord.SelectOption(
            label = 'Adicionar',
            description = 'Adiciona uma advertencia'
        ),
        discord.SelectOption(
            label = 'Remover',
            description = 'Remove uma advertencia'
        )
        ]
    )
    async def select_callback(self, select, interaction: discord.Interaction):

        channel = self.bot.get_channel(configData['chats']['cmdstf'])

        if select.values[0] == 'Adicionar':

            def check(m):
                return m.content and m.author.id == interaction.user.id

            try:

                await interaction.response.send_message('Mande o id da pessoa a adverter', ephemeral = True)

                msg = await self.bot.wait_for('message', check = check, timeout = 130)

                membro = interaction.guild.get_member(int(msg.content))

                await msg.delete()

                def check2(m):
                    return m.content and m.author.id == interaction.user.id

                try:

                    id = await channel.send('Mande o motivo de adverter o membro')

                    msg2 = await self.bot.wait_for('message', check = check2, timeout = 130)

                    await id.delete()

                    await msg2.delete()

                    e = discord.Embed(title = 'Advertencia')

                    e.add_field(name = 'Pessoa a adverter', value = f'{membro.mention}')
                    e.add_field(name = 'Quem adverteu', value = interaction.user.mention, inline = False)
                    e.add_field(name = 'Motivo', value = msg2.content)

                    await channel.send(embed = e, view = adcadv(self.bot,membro,msg2.content, interaction.user))

                    self.stop()

                except:
                    print('error')

            except:
                print('error')

        elif select.values[0] == 'Remover':

            def check50(m):
                return m.content and m.author.id == interaction.user.id

            try:

                await interaction.response.send_message('Mande o id da pessoa a remover a advertencia', ephemeral = True)

                msg50 = await self.bot.wait_for('message', check = check50, timeout = 130)

                membro = interaction.guild.get_member(int(msg50.content))

                await msg50.delete()

                e = discord.Embed(title = 'Advertencia')

                e.add_field(name = 'Remover advertencia de ', value = f'{membro.mention}')
                e.add_field(name = 'Quem removeu ', value = interaction.user.mention, inline = False)

                await channel.send(embed = e, view = rmvadv(self.bot,membro))

                self.stop()

            except:

                print('error')