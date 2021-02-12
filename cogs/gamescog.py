from discord.ext import commands
import random
import d20

class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["r"], help="Can accept things like 1d6+4 or 4d6kh3")
    async def roll(self, ctx, *, rollStr: str = ''):
        result = d20.roll(rollStr)
        str(result)
        await ctx.channel.send(result)

    @commands.command(help = "guess a number 1-20")
    async def guess(self, ctx, arg):
      ran = random.randint(1,20)
      guess = int(arg) #converts the arg to an int 
      if ran == guess:
          await ctx.channel.send("You got it!")
      else:
          await ctx.channel.send(f"nope, too bad, the number was {ran}")
          print(f"random: {ran} guess: {guess}")


def setup(bot):
    bot.add_cog(Games(bot))