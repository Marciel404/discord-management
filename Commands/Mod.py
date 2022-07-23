from Outhers.info.fi import *
from Outhers.Class.Buttons import *

class Mod(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @discord.slash_command(name = 'kick', description = 'Expulsa um membro')
    @discord.option(name = 'Membro', description = 'Escolha o membro para expulsar')
    @discord.option(name = 'Motivo', description = 'Escreva o motivo de expulsar')
    @commands.bot_has_permissions(kick_members = True)
    @commands.has_permissions(kick_members = True)
    async def kick(self, 
    ctx, 
    membro: discord.Member = None, 
    *,motivo=None):


        if motivo == None:

            motivo = 'Motivo não informado'

        e1 = discord.Embed(title = 'kick', description = f'Voce esta prestes a expulsar {membro.mention}')

        if membro == self.bot.user:

            await ctx.response.send_message('Não posso expulsar a mim mesmo')

            return

        elif  membro == ctx.author:

            await ctx.response.send_message('Você não pode expulsar a si mesmo')

            return
        
        elif membro == None:

            await ctx.response.send_message('Você precisa mensionar o membro a banir')

            return

        await ctx.response.send_message(embed = e1, view = kick(self.bot,membro, motivo, ctx))

    @discord.slash_command(name = 'ban', description = 'Bane um membro')
    @discord.option(name = 'Membro', description = 'Escolha o membro para Banir')
    @discord.option(name = 'Motivo', description = 'Escreva o motivo de Banir')
    @commands.bot_has_permissions(ban_members = True)
    @commands.has_permissions(ban_members = True)
    async def Ban(self, ctx, membro: discord.Member = None, *,motivo=None):

        if motivo == None:

            motivo = 'Motivo não informado'

        e1 = discord.Embed(title = 'kick', description = f'Voce esta prestes a expulsar {membro.mention}')

        if membro == self.bot.user:

            await ctx.response.send_message('Não posso expulsar a mim mesmo')

            return

        elif  membro == ctx.author:

            await ctx.response.send_message('Você não pode expulsar a si mesmo')

            return

        elif membro == None:

            await ctx.response.send_message('Você precisa mensionar o membro a banir')

            return

        await ctx.response.send_message(embed = e1, view = ban(self.bot, membro,motivo,ctx))

    @discord.slash_command(name = 'embed', description = 'Envia uma embed em um chat desejado')
    @discord.option(name = 'Canal', description = 'Escolha o chat para enviar a embed')
    @discord.option(name = 'title', description = 'Escreva o titulo da embed')
    @discord.option(name = 'img', description = 'Escolha a imagem da embed')
    @discord.option(name = 'Motivo', description = 'Escreva o conteudo da embed')
    @commands.has_permissions(manage_channels = True)
    async def say(self, ctx, channel: discord.TextChannel = None, title = None, img = None, *, msg = None):

        if channel == None:
            await ctx.response.send_message('Você precisa escolher o chat para enviar a embed')

        if title == None:
            title = ''

        if img == None:
            img = ''
        
        if title == 'None':
            title = ''

        if img == 'None':
            img = ''

        if msg == 'None':
            msg = ''

        e = discord.Embed(title = title, description = msg, colour = 0x4B0082)
        e.set_image(url = img)
        e.set_footer(text = f'Ass. {ctx.guild.name}', icon_url = ctx.guild.icon)

        channel2 = self.bot.get_channel(channel.id)


        await channel2.send(embed = e)

    @discord.slash_command(name = 'clear', description = 'Limpa o chat')
    @discord.option(name = 'quantidade',type = int, description = 'Escolha a quantidade de mensagens a limpar')
    @commands.has_permissions(manage_channels = True)
    async def clear(self, ctx, quantidade: int = 0):

        if quantidade > 100:

            await ctx.response.send_message('O limite maximo é de 100 mensagens')

            return
            
        elif quantidade == 0:

            await ctx.response.send_message('Você precisa escolher uma quantidade de mensagens, a quantidade maxima é 1000 mensagens')

        else:

            purge = await ctx.channel.purge(limit=quantidade)

            await ctx.response.send_message(f"O chat teve {len(purge)} mensagens apagadas por {ctx.author.mention}")

    @discord.slash_command(name = 'banid', description ='bane um membro que não está no server')
    @discord.option(name = 'Membro', description = 'Coloque o id da pesoa a banir')
    @discord.option(name = 'Motivo', description = 'Escreva o motivo de Banir')
    @commands.bot_has_permissions(ban_members = True)
    @commands.has_permissions(ban_members = True)
    async def banid(self, ctx, membro: int, *,motivo=None):

        if motivo == None:

            motivo = 'Motivo não informado'

        else:

            motivo = motivo

        e1 = discord.Embed(title = 'BanId', description = f'Voce esta prestes a banir {membro}')

        if membro == self.bot.user.id:

            await ctx.response.send_message('Não posso banir a mim mesmo')

        elif  membro == ctx.author.id:

            await ctx.response.send_message('Você não pode banir a si mesmo')

        await ctx.response.send_message(embed = e1, view = banid(self.bot, id,motivo,ctx))

    @discord.slash_command(name = 'unban', description = 'Desbane um membro')
    @commands.bot_has_permissions(ban_members = True)
    @commands.has_permissions(ban_members = True)
    async def unban(self, ctx, id: int, *, razão = None):

        l1 = self.bot.get_channel(950170587681128468)

        if razão == None:

            razão = 'Não informado'

        else:

            razão = razão

        e = discord.Embed(title = 'UnBan',

        description = f'Quem desbaniu: {ctx.author}\n quem foi desbanido: <@{id}> \nrazão: {razão}')

        user = await self.bot.fetch_user(id)

        await ctx.guild.unban(user)

        await l1.response.send_message(embed = e)

        await ctx.response.send_message(f'{id} desbanido com sucesso')

    @discord.slash_command(name = 'say', description = 'Envia uma mensagem em um chat')
    async def say(self, ctx, channel: discord.TextChannel = None, *, msg = None):

        if channel == None:
            await ctx.response.send_message('Você precisa escolher o chat para enviar a embed')

        if msg == None:
            await ctx.response.send_message('Você precisa escrever algo para enviar')


        channel2 = self.bot.get_channel(channel.id)


        await channel2.send(msg)

    @discord.slash_command(name = 'standby', description = 'Te coloca em estado de stand-by')
    async def sandby(self, ctx, *, motivo):

        role = discord.utils.get(ctx.guild.roles, id = configData['roles']['standby'])

        if role in ctx.author.roles:
            
            await ctx.author.remove_roles(role, reason = motivo)

        else:

            await ctx.author.add_roles(role, reason = motivo)


async def tck(self):

    guild = self.bot.get_guild(configData["guild"])

    e = discord.Embed(
    title = 'Precisa de ajuda? Reaja a 🛎 para abrir um ticket',  
    description = 'Com os tickets você pode reportar algo ou tirar alguma dúvida.',
    color = 0x4B0082)
    e.set_footer(text = 'Staff Hayleng', icon_url = guild.icon)
    e.set_image(url = 'https://media.discordapp.net/attachments/793256675229564948/1000150688900325569/standard_gif_suporte.gif')

    channel = self.bot.get_channel(configData['chats']['ticket'])

    await channel.purge(limit=1)

    await channel.send(embed = e, view = ticket())

def setup(bot:commands.Bot):
    bot.add_cog(Mod(bot))