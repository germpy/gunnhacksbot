import discord
from discord.ext import commands
import random

class Shenanigans(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.command(name="low")
	async def lowercase(self, ctx, arg="​​​no text given to make lowercase"):
		await ctx.send(arg.lower())

	@commands.command(name="up")
	async def capitalize(self, ctx, arg="​​​no text given to capitalize"):
		await ctx.send(arg.upper())

	@commands.command(name = "ping")
	async def ping(self, ctx):
		await ctx.send("pong!")

	@commands.command(name="scream")
	async def scream(self, ctx, arg="​​​no text given to scream"):
		await ctx.send("".join(
			[random.choice([i.upper(), i.lower()]) for i in arg]
			))

	

def setup(bot):
	bot.add_cog(Shenanigans(bot))