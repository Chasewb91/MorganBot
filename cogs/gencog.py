from discord.ext import commands


class Gencog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def who(self, ctx):
      await ctx.channel.send("I am MorganBot, premium Discord concierge.")


def setup(bot):
  bot.add_cog(Gencog(bot))