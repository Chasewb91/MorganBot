import discord
from discord.ext import commands
from tinydb import TinyDB, Query
from tinydb.operations import increment, decrement

db = TinyDB('db.json')

class Scorecard(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def register(self, ctx):
      user = ctx.message.author
      userdb = str(user)
      db.insert({'User': userdb, 'Points': 0,})
      await ctx.channel.send("You have registered for the points system!")


    @commands.command()
    async def query(self, ctx):
      user = ctx.author
      userdb = str(user)
      Points = Query()
      tally  = db.search(Points.User == userdb)
      await ctx.channel.send(tally)

    @commands.command()
    async def point(self,ctx, user: discord.User):
      userdb = str(user)
      User = Query()
      db.update(increment('Points'), User.User == userdb)
      print(userdb + " has gained a point!")
      await ctx.channel.send(f"A point has been awarded to {userdb}!")

    @commands.command()
    async def unpoint(self, ctx, user: discord.User):
      userdb = str(user)
      User = Query()
      db.update(decrement('Points'), User.User == userdb)
      print(userdb + " has lost a point!")
      await ctx.channel.send(f"Point taken from {userdb}!")     



def setup(bot):
    bot.add_cog(Scorecard(bot))

