from discord.ext import commands


class Gencog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def who(self, ctx):
      await ctx.channel.send("I am MorganBot, a premium Discord concierge bot. \n \nBuilt by Chase Boyd in Python.")

    @commands.command()
    async def slv(self, ctx):
      await ctx.channel.send("https://www.kitco.com/charts/livesilver.html")


def setup(bot):
  bot.add_cog(Gencog(bot))