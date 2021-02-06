from discord.ext import commands
from discord import Guild
import discord
import keep_alive
import os
from dotenv import load_dotenv



load_dotenv()  # pulls discord bot token from .env file
TOKEN = os.getenv('DISCORD_TOKEN')  # pulls discord bot token from .env file

key = os.getenv('key')

wkey = os.getenv('wkey')

intents = discord.Intents.default()
intents.members = True


client = commands.Bot(command_prefix='$', intents=intents)  #Makes the bot prefix.



@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    print(f'Discord.py version {discord.__version__}')
    await client.change_presence(activity=discord.Game('Poker'))  # discord presence

@client.event
async def on_member_join(member):
  member = member
  print(f"{member} has joined the server")
  chan = client.get_channel(807754507122638848)
  await chan.send(f"Welcome, {member.mention}.")
  await member.send(content="welcome to the server, and stay awhile!")
  

@client.command()
async def ping(ctx):
  await ctx.channel.send("pong")

@client.command()
async def join_test(ctx, member: discord.Member):
    client.dispatch('member_join', member)


#cogs

client.load_extension("cogs.gencog")

client.load_extension("cogs.dicecog")

client.load_extension("cogs.admincog")


keep_alive.keep_alive()  #keep this at the end

client.run(TOKEN)



