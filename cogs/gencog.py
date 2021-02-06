from discord.ext import commands
import random

class Gencog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def who(self, ctx):
      await ctx.channel.send("I am MorganBot, a premium Discord concierge bot. \n \nBuilt by Chase Boyd in Python.")


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
  bot.add_cog(Gencog(bot))