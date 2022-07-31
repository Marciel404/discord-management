from outhers.info.fi import *

class Membros(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @discord.slash_command(name = 'mv', description = 'Move um membro para a sua call privada')
    @discord.option(name = 'membro', description = 'Escolha o membro para puxar para sua call privada')
    async def mv(self, ctx, membro: discord.Member = None):

        call = discord.utils.get(ctx.author.guild.channels, name = f'Call Privada de {ctx.author.display_name}')

        if membro.voice == None:

            await ctx.respond(f'{membro.mention} não está em um canal de voz', ephemeral = True)

            return

        if membro.voice.channel == discord.utils.get(ctx.author.guild.channels, name = f'Call Privada de {membro.display_name}'):

            await membro.move_to(call)

            await ctx.respond(f'{membro.mention} movido para {call}', ephemeral = True)

            return

        if ctx.author.voice.channel != call:

            await ctx.respond('Você não está no seu canal privado', ephemeral = True)

            return

        if membro.voice.channel != discord.utils.get(ctx.guild.channels, id = configData['calls']['espera']):

            await ctx.respond(f'{membro.mention} não está no canal de espera', ephemeral = True)
            
            return

        await membro.move_to(call)

        await ctx.respond(f'{membro.mention} movido para {call}', ephemeral = True)
    
def setup(bot:commands.Bot):
    bot.add_cog(Membros(bot))