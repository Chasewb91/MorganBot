from discord.ext import commands
import cryptocompare


class Crypto(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def price(self, ctx, arg):
      coin = cryptocompare.get_price([arg], ['USD'])
      await ctx.channel.send(coin)



def setup(bot):
  bot.add_cog(Crypto(bot)) 