from outhers.info.fi import *

intents = discord.Intents.all()

client = commands.Bot(

command_prefix = configData['prefix'],

help_command = None,

case_insensitive = True,

intents = intents

)

for filename in os.listdir('./commands'):
        
    if filename.endswith('.py'):

        client.load_extension('commands.{0}'.format(filename[:-3]))

for filename in os.listdir('./outhers'):

    if filename.endswith('.py'):

        client.load_extension(f'outhers.{filename[:-3]}')

client.run(configData['token'])
