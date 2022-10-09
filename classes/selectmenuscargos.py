import discord

from utils.configs import configData

class adccap(discord.ui.View):

    def __init__(self,bot, membro, cargo, inter):

        self.cargo = cargo

        self.membro = membro

        self.bot = bot

        self.inter = inter

        super().__init__(timeout = None)

    @discord.ui.button(label = '✅'  , style = discord.ButtonStyle.blurple)
    async def adcc(self, button: discord.ui.Button, interaction: discord.Interaction):

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

        if discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['admin'])in interaction.user.roles:
        
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
    async def adccg(self, button: discord.ui.Button, interaction: discord.Interaction):

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

        if discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['admin']) in interaction.user.roles \
        or discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['mod']) in interaction.user.roles:
        
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

        if discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['admin']) in interaction.user.roles \
        or discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['mod']) in interaction.user.roles:
        
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

        if discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['admin']) in interaction.user.roles \
        or discord.utils.get(interaction.guild.roles, id = configData['roles']['staff']['mod']) in interaction.user.roles:
        
            await interaction.message.delete()

            self.stop()

        else:

            await interaction.response.send_message('Você não tem permissão para usar isso', ephemeral = True)