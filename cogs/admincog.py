import discord
from discord.ext import commands


class Admin(commands.Cog):
    def __init__(self, bot,):
        self.bot = bot
        
    @commands.command()
    @commands.has_role('Admin')
    async def makechan(self, ctx, channel, category: discord.CategoryChannel):
      await ctx.guild.create_text_channel(channel, category=category) 

    @commands.command()
    @commands.has_role('Admin')
    async def makecat(self, ctx, category):
      await ctx.guild.create_category(category)


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