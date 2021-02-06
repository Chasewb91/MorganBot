from discord.ext import commands
import random
import d20


class Dice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["r"], help="Can accept things like 1d6+4 or 4d6kh3")
    async def roll(self, ctx, *, rollStr: str = ''):
        result = d20.roll(rollStr)
        str(result)
        await ctx.channel.send(result)


def setup(bot):
    bot.add_cog(Dice(bot))
