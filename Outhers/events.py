from Outhers.info.fi import *
from Commands.Mod import *

class events(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):

        await tck(self)

        print(f'EU entrei como {self.bot.user}')

        print(discord.__version__)

    @commands.Cog.listener()
    async def on_message(self, message):

        if message.author == self.bot.user: return

        if message.author.bot: return
        
        elif message.mention_everyone:

            return

    @commands.Cog.listener()
    async def on_message_edit(self, antes:discord.Message, depois: discord.Message):

        if antes.author.bot:

            return

        channel = self.bot.get_channel(configData['logs']['chat'])

        e = discord.Embed(

            description = f'Mensagem enviada por {antes.author.mention} foi editada em {antes.channel.mention}'

        )
        e.add_field(name = 'Antiga:', value = f'{antes.content}', inline=False)

        e.add_field(name = 'Nova:', value =  f'{depois.content}', inline=False)

        e.set_author(name = antes.author.name, icon_url = antes.author.avatar, url = antes.author.avatar)

        e.set_footer(text = f'生 HAYLENG 死 às {dt}')

        await channel.send(embed = e)

    @commands.Cog.listener()
    async def on_message_delete(self, message: discord.Message):

        channel = self.bot.get_channel(configData['logs']['chat'])

        e = discord.Embed(

            description = f'Mensagem enviada por {message.author.mention} foi deletada em {message.channel.mention}'

        )
        e.add_field(name = 'Mensagem:', value = f'{message.content}', inline=False)

        e.set_author(name = message.author.name, icon_url = message.author.avatar, url = message.author.avatar)

        e.set_footer(text = f'生 HAYLENG 死 às {dt}')

        await channel.send(embed = e)

    @commands.Cog.listener()
    async def on_member_update(self, antes:discord.User, depois:discord.User):

        channel = self.bot.get_channel(configData['logs']['membros'])

        if antes.nick != depois.nick:
            e = discord.Embed(

            description = f'{antes.mention} editou o nick'
        )
            e.add_field(name = 'Nome antigo:', value = f'{antes.display_name}', inline=False)

            e.add_field(name = 'Nome novo:', value =  f'{depois.display_name}', inline=False)

            e.set_author(name = antes.name, icon_url = antes.avatar, url = antes.avatar)

            e.set_footer(text = f'生 HAYLENG 死 às {dt}')

            await channel.send(embed = e)

        if antes.avatar != depois.avatar:

            e = discord.Embed(

            description = f'{antes.mention} Trocou de foto\nFoto antiga')

            e.set_author(name = antes.name, icon_url = antes.avatar, url = antes.avatar)

            e.set_footer(text = f'生 HAYLENG 死 às {dt}')
            
            e.set_image(antes.display_avatar)

            e2 = discord.Embed(

            description = f'{antes.mention} Trocou de foto\nFoto Nova')

            e2.set_author(name = antes.name, icon_url = antes.avatar, url = antes.avatar)

            e2.set_footer(text = f'生 HAYLENG 死 às {dt}')

            e2.set_image(depois.display_avatar)

            await channel.send(embeds = [e,e2])

    @commands.Cog.listener()
    async def on_user_update(self, antes:discord.User, depois:discord.User):

        channel = self.bot.get_channel(configData['logs']['membros'])

        if antes.avatar != depois.avatar:

            e = discord.Embed(

            description = f'{antes.mention} Trocou de foto\nFoto antiga')

            e.set_author(name = antes.name, icon_url = antes.avatar, url = antes.avatar)

            e.set_footer(text = f'生 HAYLENG 死 às {dt}')
            
            e.set_image(antes.display_avatar)

            e2 = discord.Embed(

            description = f'{antes.mention} Trocou de foto\nFoto Nova')

            e2.set_author(name = antes.name, icon_url = antes.avatar, url = antes.avatar)

            e2.set_footer(text = f'生 HAYLENG 死 às {dt}')

            e2.set_image(depois.display_avatar)

            await channel.send(embeds = [e,e2])

    @commands.Cog.listener()
    async def on_voice_state_update(self, member:discord.Member, before:discord.VoiceState, after:discord.VoiceState):

        channel = self.bot.get_channel(configData['logs']['call'])

        if before.channel != after.channel:

            if before.channel == None:

                e = discord.Embed(

                description = f'{member.mention} entrou no chat {after.channel}'

                )
                e.set_author(name = member.name, icon_url = member.avatar, url = member.avatar)

                e.set_footer(text = f'生 HAYLENG 死 às {dt}')

                await channel.send(embed = e)

                return
            
            elif after.channel == None:

                e = discord.Embed(

                description = f'{member.mention} saiu do chat {before.channel}'

                )
                e.set_author(name = member.name, icon_url = member.avatar, url = member.avatar)

                e.set_footer(text = f'生 HAYLENG 死 às {dt}')

                await channel.send(embed = e)

                return

            e = discord.Embed(

            description = f'{member.mention} se moveu do {before.channel} para {after.channel}'

            )
            e.set_author(name = member.name, icon_url = member.avatar, url = member.avatar)

            e.set_footer(text = f'生 HAYLENG 死 às {dt}')

            await channel.send(embed = e)

        elif after.self_deaf:

            e = discord.Embed(

            description = f'{member.mention} mutou o fone no {after.channel}')

            e.set_author(name = member.name, icon_url = member.avatar, url = member.avatar)

            e.set_footer(text = f'生 HAYLENG 死 às {dt}')

            await channel.send(embed = e)
        
        elif before.self_deaf:



            e = discord.Embed(

            description = f'{member.mention} desmutou o fone no {after.channel}')

            e.set_author(name = member.name, icon_url = member.avatar, url = member.avatar)

            e.set_footer(text = f'生 HAYLENG 死 às {dt}')

            await channel.send(embed = e)

        elif before.self_mute:

            e = discord.Embed(

            description = f'{member.mention} desmutou o microfone no {after.channel}')

            e.set_author(name = member.name, icon_url = member.avatar, url = member.avatar)

            e.set_footer(text = f'生 HAYLENG 死 às {dt}')

            await channel.send(embed = e)

        elif after.self_mute:

            e = discord.Embed(

            description = f'{member.mention} mutou o microfone no {after.channel}')

            e.set_author(name = member.name, icon_url = member.avatar, url = member.avatar)

            e.set_footer(text = f'生 HAYLENG 死 às {dt}')

            await channel.send(embed = e)

        elif after.self_video:

            e = discord.Embed(

            description = f'{member.mention} ativou o video no {after.channel}')

            e.set_author(name = member.name, icon_url = member.avatar, url = member.avatar)

            e.set_footer(text = f'生 HAYLENG 死 às {dt}')

            await channel.send(embed = e)
        
        elif before.self_video:

            e = discord.Embed(

            description = f'{member.mention} desativou o video no {after.channel}')

            e.set_author(name = member.name, icon_url = member.avatar, url = member.avatar)

            e.set_footer(text = f'生 HAYLENG 死 às {dt}')

            await channel.send(embed = e)

        elif after.self_stream:

            e = discord.Embed(

            description = f'{member.mention} começou a transmitir no {after.channel}')

            e.set_author(name = member.name, icon_url = member.avatar, url = member.avatar)

            e.set_footer(text = f'生 HAYLENG 死 às {dt}')

            await channel.send(embed = e)
        
        elif before.self_stream:

            e = discord.Embed(

            description = f'{member.mention} parou de transmitir no {after.channel}')

            e.set_author(name = member.name, icon_url = member.avatar, url = member.avatar)

            e.set_footer(text = f'生 HAYLENG 死 às {dt}')

            await channel.send(embed = e)

        if after.deaf:

            e = discord.Embed(

            description = f'{member.mention} foi ensurdecido no {after.channel}')

            e.set_author(name = member.name, icon_url = member.avatar, url = member.avatar)

            e.set_footer(text = f'生 HAYLENG 死 às {dt}')

            await channel.send(embed = e)
        
        elif before.deaf:

            e = discord.Embed(

            description = f'{member.mention} foi desensurdecido no {after.channel}')

            e.set_author(name = member.name, icon_url = member.avatar, url = member.avatar)

            e.set_footer(text = f'生 HAYLENG 死 às {dt}')

            await channel.send(embed = e)

        elif before.mute:

            e = discord.Embed(

            description = f'{member.mention} foi desmutado no {after.channel}')

            e.set_author(name = member.name, icon_url = member.avatar, url = member.avatar)

            e.set_footer(text = f'生 HAYLENG 死 às {dt}')

            await channel.send(embed = e)

        elif after.mute:

            e = discord.Embed(

            description = f'{member.mention} mutado no {after.channel}')

            e.set_author(name = member.name, icon_url = member.avatar, url = member.avatar)

            e.set_footer(text = f'生 HAYLENG 死 às {dt}')

            await channel.send(embed = e)

def setup(bot:commands.Bot):
    bot.add_cog(events(bot))