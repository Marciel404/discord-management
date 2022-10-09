import discord

from discord.ext import commands
from db.economy import update_bank

class economia(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @discord.slash_command(guild_only = True,name = 'adchygcoins', description = 'Adiciona hyg coins a um membro')
    @discord.option(name = 'membro', description = 'Mencione o membro')
    @discord.option(name = 'hygcoins', description = 'Coloque a quantidade de hygcoins')
    async def Set(self,ctx, membro: discord.Member, hygcoins: int):

        await update_bank(membro, + hygcoins)

        await ctx.respond(f'Foram dados {hygcoins} hyg coins para {membro.mention}', ephemeral = True)

    @discord.slash_command(guild_only = True,name = 'rmvhygcoins', description = 'Remove hyg coins a um membro')
    @discord.option(name = 'membro', description = 'Mencione o membro')
    @discord.option(name = 'hygcoins', description = 'Coloque a quantidade de hygcoins')
    async def Rmv(self,ctx, membro: discord.Member, hygcoins:int):

        await update_bank(membro, - hygcoins)

        await ctx.respond(f'Foram removidos {hygcoins} hyg coins de {membro.mention}', ephemeral = True)

def setup(bot:commands.Bot):
    bot.add_cog(economia(bot))