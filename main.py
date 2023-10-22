import discord
from discord.ext import commands

# Replace 'YOUR_TOKEN' with your bot's token
TOKEN = 'MTE2NTc2MzA0OTU5Mjk5MTgxNQ.GI8ZgD.6Ql8KtTe_u-tTDaP8gZesraespq_qVfChKevOE'

# Create an instance of the bot
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

@bot.command()
async def hello(ctx):
    await ctx.send('Hello, I am your Discord bot!')

# Run the bot with your token
bot.run(TOKEN)
