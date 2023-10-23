import datetime
from discord.ext import commands
import discord
import socket
import requests

BOT_TOKEN = "MTE2NTc4NDk3NDk1MjI0MzMxMg.Gc1Mw9.0RQmruaf58Rm4WcQD4X05DszbdiZfDZH_YwNKc"
ADMIN_CHANNEL_NAME = "pri"
GENERAL_CHANNEL_NAME = "general"

def get_ip_address(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror as e:
        return str(e)

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Ready!")
    print(f"Bot is connected to {len(bot.guilds)} guild(s)")
    print(f"Bot is connected to the following guilds:")
    for guild in bot.guilds:
        print(guild.name)
    print("---------------------")
    print(f"Admin channel ID: {get_channel_id(ADMIN_CHANNEL_NAME)}")
    print(f"General channel ID: {get_channel_id(GENERAL_CHANNEL_NAME)}")

@bot.event
async def on_message(message):
    
    general_channel = get_channel_by_name(GENERAL_CHANNEL_NAME)
    
    
    if message.channel.name == ADMIN_CHANNEL_NAME and message.author != bot.user:
        if general_channel:
            
            await general_channel.send(f"{message.content}")

    
    if message.channel.name == GENERAL_CHANNEL_NAME and message.author != bot.user:
        
        admin_channel = get_channel_by_name(ADMIN_CHANNEL_NAME)
        if admin_channel:
            
            await admin_channel.send(f"{message.author.display_name}: {message.content}")

    await bot.process_commands(message)

def get_channel_by_name(channel_name):
    for guild in bot.guilds:
        channel = discord.utils.get(guild.channels, name=channel_name)
        if channel:
            return channel
    return None

def get_channel_id(channel_name):
    channel = get_channel_by_name(channel_name)
    if channel:
        return channel.id
    else:
        return None

@bot.command()
async def hello(ctx):
    await ctx.send('Send Test')

bot.run(BOT_TOKEN)
