from discord.ext import commands
import random

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def who(self, ctx):
      await ctx.channel.send("I am MorganBot, a premium Discord concierge bot. \n \nBuilt by Chase Boyd in Python. \n \nType $help for more commands")




def setup(bot):
  bot.add_cog(General(bot))