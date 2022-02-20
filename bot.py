from distutils import command
from urllib import response
import discord
import random
import math 
from discord.ext import commands

client = discord.Client()

TOKEN = 'OTQ0ODU4OTAyOTc2MTU5Nzg1.YhHubQ.Sj_rJ5xJ7hbgxGIvpocE5B4sdJA'



client = commands.Bot(command_prefix='1', help_command=None)

def sub(x: float,y: float):
    return x-y

def add(x: float,y: float):
    return x+y
def div(x: float,y: float):
    return x/y
def rando(x: int,y: int):
    return random.randint(x, y)
def sqrt(x: float):
    return math.sqrt(x)




@client.command()






@client.event 
async def on_readly():
    print('We have logged in as {0.user}'.format(client))

@client.event 
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return

    if message.channel.name == 'general':
        if user_message.lower() == 'hello':
            await message.channel.send(f'hello {username}!')
            return
        elif user_message.lower() == 'bye':
            await message.channel.send(f'See you later {username}!')
            return
        elif user_message.lower() == '@random':
            response = f'This is your random number: {random.randrange(10000000)}'
            await message.channel.send(response)
            return
        if user_message.lower() == '!anywhere':
            await message.channel.send ('This can be used anywhere!')
            return
        if user_message.lower() == '!gif':
            await message.channel.send ('https://giphy.com/gifs/genshin-impact-zhongli-GOaMRxfIqqnvbfF84h')
            return
        if user_message.lower() == 'địt mẹ mày':
            await message.channel.send ('Chửi thể con cằc đồ zô zăn hóa')
            return 
        
client.run(TOKEN)
