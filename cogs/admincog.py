import discord
from discord.ext import commands

class Admin(commands.Cog):
    def __init__(self, bot,):
        self.bot = bot
        
    @commands.command()
    @commands.has_role('Admin')
    async def make(self, ctx, *, arg):
	    guild = ctx.channel.guild
	    await guild.create_text_channel(arg)  

    @commands.command()
    @commands.has_role('Admin')
    async def remove(self, ctx, channel: discord.TextChannel, reason =None):
      await channel.delete()

    @commands.command()
    @commands.has_role('Admin')
    async def addrole(self, ctx, member: discord.Member, role: discord.Role, atomic = True):
      await member.add_roles(role)

    @commands.command()
    @commands.has_role('Admin')
    async def removerole(self, ctx, member: discord.Member, role: discord.Role, atomic = True):
      await member.remove_roles(role)

    

        
def setup(bot):
  bot.add_cog(Admin(bot)) 