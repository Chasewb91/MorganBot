import discord
from discord.ext import commands
from tinydb import TinyDB, Query
from tinydb.operations import increment, decrement

db = TinyDB('db.json')

class Database(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def register(self, ctx):
      user = ctx.message.author
      userdb = str(user)
      db.insert({'User': userdb, 'inspiration': 0,})
      await ctx.channel.send("You have registered for the inspiration counter!")


    @commands.command()
    async def query(self, ctx):
      user = ctx.author
      userdb = str(user)
      Inspo = Query()
      tally  = db.search(Inspo.User == userdb)
      await ctx.channel.send(tally)

    @commands.command()
    async def inspo(self,ctx, user: discord.User):
      userdb = str(user)
      User = Query()
      db.update(increment('inspiration'), User.User == userdb)
      print(userdb + " has gained inspiration!")
      await ctx.channel.send("Inspiration has been awarded!")

    @commands.command()
    async def dinspo(self, ctx, user: discord.User):
      userdb = str(user)
      User = Query()
      db.update(decrement('inspiration'), User.User == userdb)
      print(userdb + " has lost inspiration!")
      await ctx.channel.send("Inspiration has been used!")     



def setup(bot):
    bot.add_cog(Database(bot))

