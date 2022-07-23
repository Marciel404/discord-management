from Outhers.info.fi import *

intents = discord.Intents.all()

client = commands.Bot(

command_prefix = configData['prefix'],

help_command = None,

case_insensitive = True,

intents = intents

)

for filename in os.listdir('./Commands'):
        
    if filename.endswith('.py'):

        client.load_extension('Commands.{0}'.format(filename[:-3]))

for filename in os.listdir('./Outhers'):

    if filename.endswith('.py'):

        client.load_extension(f'Outhers.{filename[:-3]}')

client.run(configData['token'])