import discord
from discord.ext import commands

class HelloPlugin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def say(self, ctx):
        await ctx.reply("Hello, {ctx.author.mention}!")

def setup(bot):
    bot.add_cog(HelloPlugin(bot))
