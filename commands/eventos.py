import discord

from discord.ext import commands
from db.evento import *

class eventos(commands.Cog):

    def __init__(self, bot:commands.Bot):

        self.bot = bot

    @discord.slash_command(guild_only = True,name = 'adcponto', description = 'Adiciona um ponto de evento para um membro')
    @discord.option(name = 'membro', description = 'mencione o membro')
    async def addpoints(self, ctx, membro: discord.Member = None):

        await addp(membro, + 1)

        pt = points.find_one({"_id": membro.id})

        pt2 = pt['pontos']

        await addp2(membro, ctx.author, pt2)

        role = discord.utils.get(ctx.guild.roles, name = f'{pt2}🏆')

        if role not in ctx.guild.roles:

            role2 = await ctx.guild.create_role(name = f'{pt2}🏆', color = 0xff8600)

            await membro.add_roles(role2)

            if discord.utils.get(ctx.guild.roles, name = f'{pt2-1}🏆') in ctx.guild.roles:

                await discord.utils.get(ctx.guild.roles, name = f'{pt2-1}🏆').edit(color = discord.Colour.default())

            if discord.utils.get(ctx.guild.roles, name = f'{pt2-1}🏆') in membro.roles:

                await membro.remove_roles(discord.utils.get(ctx.guild.roles, name = f'{pt2-1}🏆'))

            await ctx.respond(f'Ponto adicionado com sucesso e {role2.mention} adicionado com sucesso', ephemeral = True)

        else:

            await membro.add_roles(role)

            if discord.utils.get(ctx.guild.roles, name = f'{pt2-1}🏆') in membro.roles:

                await membro.remove_roles(discord.utils.get(ctx.guild.roles, name = f'{pt2-1}🏆'))

            await ctx.respond(f'Ponto adicionado com sucesso e {role.mention} adicionado com sucesso', ephemeral = True)
    
    @discord.slash_command(guild_only = True,name = 'rmvponto', description = 'remove um ponto de evento para um membro')
    @discord.option(name = 'membro', description = 'mencione o membro')
    async def rmvpoints(self, ctx, membro: discord.Member = None):

        await rmvp(membro, - 1)

        pt = points.find_one({"_id": membro.id})

        pt2 = pt['pontos']

        if pt2 == -1:

            await addp(membro, + 1)

            await ctx.respond('Esse membro não posue pontos', ephemeral = True)

            if discord.utils.get(ctx.guild.roles, name = f'{pt2+1}🏆') in membro.roles:

                await membro.remove_roles(discord.utils.get(ctx.guild.roles, name = f'{pt2+1}🏆'))

            return

        pt3 = pt[f'ponto{pt2+1}']

        if pt == 0:

            pt3 = pt[f'ponto{1}']

        if pt2 > 0:

            await rmvp2(membro,pt2+1,pt3)

        if pt2 == 0:

            await rmvp2(membro,1,pt3)

        role = discord.utils.get(ctx.guild.roles, name = f'{pt2}🏆')

        if role in ctx.guild.roles:

            await membro.add_roles(role)

            if discord.utils.get(ctx.guild.roles, name = f'{pt2+1}🏆') in membro.roles:

                await membro.remove_roles(discord.utils.get(ctx.guild.roles, name = f'{pt2+1}🏆'))

            await ctx.respond(f'Ponto removido com sucesso e {role.mention} adicionado com sucesso', ephemeral = True)

            return
        
        if discord.utils.get(ctx.guild.roles, name = f'{pt2+1}🏆') in membro.roles:

            await membro.remove_roles(discord.utils.get(ctx.guild.roles, name = f'{pt2+1}🏆'))

        await ctx.respond(f'Ponto removido com sucesso e agora este membro não posue pontos', ephemeral = True)

    @discord.slash_command(guild_only = True,name = 'verpontos', description = 'mostra os pontos de evento de um membro')
    @discord.option(name = 'membro', description = 'mencione o membro')
    async def verpontos(self, ctx, membro: discord.Member = None):

        if (points.count_documents({"_id": membro.id}) == 1):

            pt = points.find_one({"_id": membro.id})

            await ctx.respond(pt, ephemeral = True)

            return

        await ctx.respond('Esse membro não está nos meus registros', ephemeral = True)

def setup(bot:commands.Bot):
    bot.add_cog(eventos(bot))