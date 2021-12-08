from discord.ext import commands
import discord
import os
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('privatekey')

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
  chan = client.get_channel(807754507122638848) 
  print(f"{member} has joined the server")
  await chan.send(f"Welcome to the Test Bunker, {member.mention}.")
  await member.send(content="welcome to the server, and stay awhile!")
  

@client.command()
async def ping(ctx):
  await ctx.channel.send("pong")

@client.command(help = "Used to test member greetings - Admin only") 
@commands.has_role('Admin')
async def join_test(ctx, member: discord.Member):
  client.dispatch('member_join', member)


#cogs

client.load_extension("cogs.gencog")

client.load_extension("cogs.gamescog")

client.load_extension("cogs.admincog")

client.load_extension("cogs.dbcog")

client.load_extension("cogs.cryptocog")


client.run(TOKEN)



