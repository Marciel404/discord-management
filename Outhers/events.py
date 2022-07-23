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
    async def on_message_delete(self, message:discord.Message):

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

        channel = self.bot.get_channel(configData['logs']['mod'])

        if antes.nick != depois.nick:
            e = discord.Embed(

            description = f'{antes.mention} editou o nick'
        )
            e.add_field(name = 'Nome antigo:', value = f'{antes.display_name}', inline=False)

            e.add_field(name = 'Nome novo:', value =  f'{depois.display_name}', inline=False)

            e.set_author(name = antes.name, icon_url = antes.avatar, url = antes.avatar)

            e.set_footer(text = f'生 HAYLENG 死 às {dt}')

            await channel.send(embed = e)

def setup(bot:commands.Bot):
    bot.add_cog(events(bot))