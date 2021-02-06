import discord
from discord.ext import commands

class Admincog(commands.Cog):
    def __init__(self, bot,):
        self.bot = bot
      

    @commands.command()
    async def make(self, ctx, *, arg):
	    guild = ctx.channel.guild
	    await guild.create_text_channel(arg)  

    @commands.command()
    async def remove(self, ctx, channel: discord.TextChannel, reason =None):
        await channel.delete()
        

        
def setup(bot):
  bot.add_cog(Admincog(bot)) 