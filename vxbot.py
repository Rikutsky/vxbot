import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True

# Bot token (replace 'YOUR_TOKEN' with your actual bot token)
TOKEN = 'YOUR_TOKEN'


bot = commands.Bot(command_prefix='!', intents=intents)

async def modify_twitter_message(message):
    new_content = message.content
    if 'https://twitter.com/' in message.content.lower():
        new_content = new_content.replace('https://twitter.com/', 'https://vxtwitter.com/')
    if 'https://x.com/' in message.content.lower():
        new_content = new_content.replace('https://x.com/', 'https://vxtwitter.com/')
    
    if new_content != message.content:
        new_message = f'{message.author.mention} posted:\nOriginal: {message.content}\nModified: {new_content}'
        await message.delete()
        await message.channel.send(new_message)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    await modify_twitter_message(message)

    await bot.process_commands(message)

bot.run(TOKEN)
