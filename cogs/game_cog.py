import discord
from discord.ext import commands



class GameCog(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.command(name="donothing")
	async def donothing(self):
		return

def setup(bot):
	bot.add_cog(GameCog(bot))