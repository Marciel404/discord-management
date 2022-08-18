from outhers.info.fi import *
from outhers.classes.buttons import *

class Mod(commands.Cog):

    def __init__(self, bot:commands.Bot):

        self.bot = bot

    @discord.slash_command(name = 'kick', description = 'Expulsa um membro')
    @discord.option(name = 'Membro', description = 'Escolha o membro para expulsar')
    @discord.option(name = 'Motivo', description = 'Escreva o motivo de expulsar')
    @commands.bot_has_permissions(kick_members = True)
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx,membro: discord.Member = None,*,motivo=None):

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

        await ctx.response.send_message(embed = e1, view = kick(self.bot,membro, motivo, ctx.author))

        cmdl = f'''{ctx.author} usou o comando {ctx.command.name} e expulsou o {membro.name}'''

        cmdlc = self.bot.get_channel(configData['logs']['usocomandos'])

        await cmdlc.send(cmdl)

    @discord.slash_command(name = 'embed', description = 'Envia uma embed em um chat desejado')
    @discord.option(name = 'canal', description = 'Escolha o chat para enviar a embed')
    @discord.option(name = 'title', description = 'Escreva o titulo da embed')
    @discord.option(name = 'img', description = 'Escolha a imagem da embed')
    @discord.option(name = 'Motivo', description = 'Escreva o conteudo da embed')
    @commands.has_permissions(manage_channels = True)
    async def embed(self, ctx, canal: discord.TextChannel = None, title = None, img = None, *, msg = None):

        if title == None:

            title = ''

        if img == None:

            img = ''

        if msg == None:

            msg = ''

        e = discord.Embed(title = title, description = msg, colour = 0x4B0082)

        e.set_image(url = img)

        e.set_footer(text = f'Ass. {ctx.guild.name}', icon_url = ctx.guild.icon)

        if canal == None:

            canal = ctx.channel

        channel2 = self.bot.get_channel(canal.id)

        await channel2.send(embed = e)

        cmdl = f'''{ctx.author} usou o comando {ctx.command.name} e enviou uma embed no {canal.mention}'''

        cmdlc = self.bot.get_channel(configData['logs']['usocomandos'])

        await cmdlc.send(cmdl)

    @discord.slash_command(name = 'clear', description = 'Limpa o chat')
    @discord.option(name = 'quantidade',type = int, description = 'Escolha a quantidade de mensagens a limpar')
    @commands.has_permissions(manage_channels = True)
    async def clear(self, ctx, quantidade: int = 0):

        if quantidade > 100:

            await ctx.response.send_message('O limite maximo é de 100 mensagens')

            return

        elif quantidade == 0:

            await ctx.response.send_message('Você precisa escolher uma quantidade de mensagens, a quantidade maxima é 1000 mensagens')

            return

        purge = await ctx.channel.purge(limit=quantidade)

        await ctx.response.send_message(f"O chat teve {len(purge)} mensagens apagadas por {ctx.author.mention}")

        cmdl = f'''{ctx.author} usou o comando {ctx.command.name} e apagou {len(purge)} mensagens no {ctx.channel}'''

        cmdlc = self.bot.get_channel(configData['logs']['usocomandos'])

        await cmdlc.send(cmdl)

    @discord.slash_command(name = 'unban', description = 'Desbane um membro')
    @discord.option(name = 'id', description = 'Coloque o id do membro a desbanir')
    @discord.option(name = 'motivo', description = 'Escreva o motivo de Banir')
    @commands.bot_has_permissions(ban_members = True)
    @commands.has_permissions(ban_members = True)
    async def unban(self, ctx, id, *, motivo = None):

        l1 = self.bot.get_channel(configData['logs']['mod'])

        if motivo == None:

            motivo = 'Não informado'

        e = discord.Embed(title = 'UnBan',

        description = f'Quem desbaniu: {ctx.author}\n quem foi desbanido: <@{id}> \nrazão: {motivo}')

        await l1.send(embed = e)

        user = await self.bot.fetch_user(id)

        await ctx.guild.unban(user)

        await ctx.respond(f'{id} desbanido com sucesso')

        cmdl = f'''{ctx.author} usou o comando {ctx.command.name} e desbaniu o <@{id}>'''

        cmdlc = self.bot.get_channel(configData['logs']['usocomandos'])

        await cmdlc.send(cmdl)

    @discord.slash_command(name = 'say', description = 'Envia uma mensagem em um chat')
    @discord.option(name = 'canal', description = 'Escolha o canal que falar')
    @discord.option(name = 'mensagem', description = 'Escreva oq deseja que eu fale')
    async def say(self, ctx, canal: discord.TextChannel = None, *, mensagem = None):

        if mensagem == None:

            await ctx.respond('Você precisa escrever algo para enviar')

            return

        if canal == None:

            canal = ctx.channel

        cmdl = f'''{ctx.author} usou o comando {ctx.command.name} e falou {mensagem}'''

        cmdlc = self.bot.get_channel(configData['logs']['usocomandos'])

        await cmdlc.send(cmdl)

        channel2 = self.bot.get_channel(canal.id)

        await channel2.send(mensagem)

    @discord.slash_command(name = 'veradv', description = 'Envia as advs de um membro')
    @discord.option(name = 'membro', description = 'Escolha o membro a remover a advertencia')
    async def veradv(self, ctx, membro: discord.Member):

        myquery = { "_id": membro.id}

        if (mute.count_documents(myquery) == 1):

            cmdl = f'''{ctx.author} usou o comando {ctx.command.name} e viu as advertencias de {membro.display_name}'''

            cmdlc = self.bot.get_channel(configData['logs']['usocomandos'])

            await cmdlc.send(cmdl)

            adv = mute.find_one({"_id": membro.id})

            adv1 = adv['Adv1']

            adv2 = adv['Adv2']

            adv3 = adv['Adv3']

            if adv1 == 'None':

                await ctx.respond('Esse membro não Possui advertencia', ephemeral = True)

                return

            if adv3 != 'None':

                e = discord.Embed(title = f'Advertencias de {membro.name}#{membro.discriminator}', description = f'Adv1: {adv1}\nAdv2: {adv2}\nAdv3: {adv3}')

                await ctx.respond(embed = e, ephemeral = True)

                return

            if adv2 != 'None':

                e = discord.Embed(title = f'Advertencias de {membro.name}#{membro.discriminator}', description = f'Adv1: {adv1}\nAdv2: {adv2}')

                await ctx.respond(embed = e, ephemeral = True)

                return

            if adv1 != 'None':

                e = discord.Embed(title = f'Advertencias de {membro.name}#{membro.discriminator}', description = f'Adv1: {adv1}')

                await ctx.respond(embed = e, ephemeral = True)

                return

        await ctx.respond('Esse membro não Possui advertencia', ephemeral = True)

        cmdl = f'''{ctx.author} usou o comando {ctx.command.name} e viu as advertencias de {membro.display_name}'''

        cmdlc = self.bot.get_channel(configData['logs']['usocomandos'])

        await cmdlc.send(cmdl)

    @discord.slash_command(name = 'editembed', description = 'edita uma embed já enviada')
    @discord.option(name = 'channel', description = 'envie o id do canal')
    @discord.option(name = 'messageid', description = 'envie o id da mensagem')
    @discord.option(name = 'title', description = 'Escreva o titulo da embed')
    @discord.option(name = 'img', description = 'Escolha a imagem da embed')
    @discord.option(name = 'Motivo', description = 'Escreva o conteudo da embed')
    @commands.has_permissions(manage_channels = True)
    async def editembed(self, ctx, channel: discord.TextChannel = None, messageid = None, title = None, img = None, *, msg = None):

        if channel == None:

            channel = ctx.channel

        if title == None:

            title = ''

        if img == None:

            img = ''

        mensagem = await channel.fetch_message(int(messageid))

        e = discord.Embed(title = title, description = msg, colour = 0x4B0082)

        e.set_image(url = img)

        e.set_footer(text = f'Ass. {ctx.guild.name}', icon_url = ctx.guild.icon)

        await mensagem.edit(embed = e)

        cmdl = f'{ctx.author} usou o comando {ctx.command.name} e edtou a embed {messageid} no canal {channel.mention}'

        cmdlc = self.bot.get_channel(configData['logs']['usocomandos'])

        await cmdlc.send(cmdl)

    @discord.slash_command(name = 'editmsg', description = 'edita uma mensagem já enviada')
    @discord.option(name = 'channel', description = 'envie o id do canal')
    @discord.option(name = 'messageid', description = 'envie o id da mensagem')
    @discord.option(name = 'msg', description = 'Escreva a mensagem á editar')
    @commands.has_permissions(manage_channels = True)
    async def editmsg(self, ctx, channel: discord.TextChannel = None, messageid = None, *, msg = None):

        if channel == None:

            channel = ctx.channel

        mensagem = await channel.fetch_message(int(messageid))

        await mensagem.edit(msg)

        cmdl = f'''{ctx.author} usou o comando {ctx.command.name} e editou a mensagem {messageid} no chat {channel.mention}'''

        cmdlc = self.bot.get_channel(configData['logs']['usocomandos'])

        await cmdlc.send(cmdl)

    @discord.slash_command(name = 'fmv', description = 'Move um membro para a sua call privada')
    @discord.option(name = 'membro', description = 'Escolha o membro para mover para uma call')
    @discord.option(name = 'canal', description = 'Escolha o canal para mover o membro')
    async def fmv(self, ctx, membro: discord.Member = None, canal: discord.VoiceChannel = None):

        call = self.bot.get_channel(canal.id)

        if membro.voice == None:

            await ctx.respond(f'{membro.mention} não está em um canal de voz', ephemeral = True)

            return

        await membro.move_to(call)

        await ctx.respond(f'{membro.mention} movido para {call}', ephemeral = True)

        cmdl = f'{ctx.author} usou o comando {ctx.command.name} e moveu o {membro.display_name} para o {canal.name}'

        cmdlc = self.bot.get_channel(configData['logs']['usocomandos'])

        await cmdlc.send(cmdl)

    @discord.slash_command(name = 'fdsc', description = 'Desconecta uma pessoa da call')
    @discord.option(name = 'membro', description = 'Escolha o membro para desconectar da call')
    async def fdsc(self, ctx, membro: discord.Member = None):

        if membro.voice == None:

            await ctx.respond(f'{membro.mention} não está em um canal de voz', ephemeral = True)

            return

        await membro.move_to(None)

        await ctx.respond(f'{membro.mention} desconectado com sucesso', ephemeral = True)

        cmdl = f'{ctx.author} usou o comando {ctx.command.name} e desconectou o {membro.display_name}'

        cmdlc = self.bot.get_channel(configData['logs']['usocomandos'])

        await cmdlc.send(cmdl)

    @discord.slash_command(name = 'verausentes', description = 'Mostra todos os membros em estado de ausente')
    async def verausente(self, ctx):

        if ausen.find_one({"_id": 'validador'})['valor'] == 1:

            await ctx.respond('Aqui está os ausentes', ephemeral = True)

            for x in ausen.find({'Ausente?': True}):

                await ctx.respond(f"Nome: {x['Nome']}\nData: {x['Data']}\nMotivo: {x['Motivo']}", ephemeral = True)
        
        else:

            await ctx.respond('Ninguem está ausente no momento', ephemeral = True)

    @discord.slash_command(name = 'verticket', description = 'Mostra as mensagens do ultimo ticket de um membro')
    @discord.option(name = 'membro', description = 'Mostra as mensagens o ultimo ticket da pessoa')
    async def verticket(self, ctx, membro: discord.Member):

        try:

            await ctx.respond(file = discord.File('./tickets/ticket-{}.txt'.format(membro.id),f'Ticket de {membro.name}.txt'), ephemeral = True)

        except:

            await ctx.respond('Esse membro ainda não abriu um ticket', ephemeral = True)

async def stf(self):

    channel = self.bot.get_channel(configData['chats']['cmdstf'])

    await channel.purge(limit = 1)

    await channel.send(view = cmdstf(self.bot))

async def tck(self):

    guild = self.bot.get_guild(configData["guild"])

    e = discord.Embed(

    title = 'Precisa de ajuda? Reaja a 🛎 para abrir um ticket',

    description = 'Com os tickets você pode reportar algo ou tirar alguma dúvida.',

    color = 0x4B0082)

    e.set_footer(text = 'Staff Hayleng', icon_url = guild.icon)

    e.set_image(url = 'https://media.giphy.com/media/sKezAGnlMZmLnwXwP8/giphy.gif')

    channel = self.bot.get_channel(configData['chats']['ticket'])

    await channel.purge(limit=1)

    await channel.send(embed = e, view = ticket())

def setup(bot:commands.Bot):
    bot.add_cog(Mod(bot))
