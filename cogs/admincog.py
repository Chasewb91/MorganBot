import discord
from discord.ext import commands
from typing import Optional


class Admin(commands.Cog):
    def __init__(self, bot,):
        self.bot = bot
        
    @commands.command()
    @commands.has_role('Admin')
    async def makechan(self, ctx, channel, category: Optional[discord.CategoryChannel]):
      await ctx.guild.create_text_channel(channel, category=category) 

    @commands.command()
    @commands.has_role('Admin')
    async def makecat(self, ctx, category):
      await ctx.guild.create_category(category)


    @commands.command()
    @commands.has_role('Admin')
    async def removechan(self, ctx, channel: discord.TextChannel, reason =None):
      await channel.delete()

    @commands.command()
    @commands.has_role('Admin')
    async def removecat(self, ctx, category: discord.CategoryChannel):
      await discord.CategoryChannel.delete(category)


    @commands.command()
    @commands.has_role('Admin')
    async def addrole(self, ctx, member: discord.Member, role: discord.Role, atomic = True):
      await member.add_roles(role)

    @commands.command()
    @commands.has_role('Admin')
    async def removerole(self, ctx, member: discord.Member, role: discord.Role, atomic = True):
      await member.remove_roles(role)

    @commands.command()
    @commands.has_role('Admin')
    async def kick(self, ctx, user: discord.Member):
      await ctx.guild.kick(user)


    @commands.command()
    @commands.has_role('Admin')
    async def ban(self, ctx, user: discord.Member):
      await ctx.guild.ban(user)


    

        
def setup(bot):
  bot.add_cog(Admin(bot)) 