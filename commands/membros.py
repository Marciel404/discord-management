from outhers.info.fi import *

class Membros(commands.Cog):

    def __init__(self, bot:commands.Bot):

        self.bot = bot

    @discord.slash_command(name = 'mv', description = 'Move um membro para a sua call privada')
    @discord.option(name = 'membro', description = 'Escolha o membro para puxar para sua call privada')
    async def mv(self, ctx, membro: discord.Member = None):

        call = discord.utils.get(ctx.author.guild.channels, name = f'Call Privada de {ctx.author.name}')

        if membro.voice == None:

            await ctx.respond(f'{membro.mention} não está em um canal de voz', ephemeral = True)

            return

        if membro.voice.channel == discord.utils.get(ctx.author.guild.channels, name = f'Call Privada de {membro.name}'):

            await membro.move_to(call)

            await ctx.respond(f'{membro.mention} movido para {call}', ephemeral = True)

            return

        if ctx.author.voice.channel != call:

            await ctx.respond('Você não está no seu canal privado', ephemeral = True)

            return

        if membro.voice.channel != discord.utils.get(ctx.guild.channels, id = configData['calls']['espera']):

            await ctx.respond(f'{membro.mention} não está no canal de espera', ephemeral = True)
            
            return

        if membro == ctx.author:

            await ctx.respond(f'Você não pode mover a si mesmo para sua call', ephemeral = True)

            return

        await membro.move_to(call)

        await ctx.respond(f'{membro.mention} movido para {call}', ephemeral = True)

    
    @discord.slash_command(name = 'dsc', description = 'Desconecta um membro da sua call privada')
    @discord.option(name = 'membro', description = 'Escolha o membro para desconectar')
    async def dsc(self, ctx, membro: discord.Member = None):

        call = discord.utils.get(ctx.author.guild.channels, name = f'Call Privada de {ctx.author.name}')

        if membro.voice == None:

            await ctx.respond(f'{membro.mention} não está em um canal de voz', ephemeral = True)

            return

        if ctx.author.voice.channel != call:

            await ctx.respond('Você não está no seu canal privado', ephemeral = True)

            return

        if membro.voice.channel != call:

            await ctx.respond(f'{membro.mention} não está no seu canal privado', ephemeral = True)

            return

        if membro == ctx.author:

            await ctx.respond(f'Você não pode desconectar a si mesmo', ephemeral = True)

            return

        await membro.move_to(None)

        await ctx.respond(f'{membro.mention} desconectado com sucesso', ephemeral = True)
    
def setup(bot:commands.Bot):
    bot.add_cog(Membros(bot))