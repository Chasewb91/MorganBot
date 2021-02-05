from discord.ext import commands
import discord
import quandl
import keep_alive
import os
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')  # pulls discord bot token from .env file

key = os.getenv('key')

wkey = os.getenv('wkey')


client = discord.Client()

client = commands.Bot(command_prefix='$')  #Makes the bot prefix.

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    await client.change_presence(activity=discord.Game('Poker'))  # discord presence

@client.command()
async def ping(ctx):
  await ctx.channel.send("pong")

#cogs

client.load_extension("cogs.gencog")

client.run(TOKEN)

keep_alive.keep_alive()  #keep this at the end
