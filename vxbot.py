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
    new_content = new_content.replace('https://twitter.com/', 'https://vxtwitter.com/')
    new_content = new_content.replace('https://x.com/', 'https://vxtwitter.com/')
    new_content = new_content.replace('https://www.tiktok.com/', 'https://www.vxtiktok.com/')
    
    if new_content != message.content:
        await message.delete()
        await message.channel.send(f'{message.author.mention} posted: {new_content}')

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