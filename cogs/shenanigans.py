import discord
from discord.ext import commands
import random


class Shenanigans(commands.Cog): #random things lol

	def __init__(self, bot):
		self.bot = bot

	@commands.command(name="low") # string to lowercase
	async def lowercase(self, ctx, arg="​​​no text given to make lowercase"):
		await ctx.send(arg.lower())

	@commands.command(name="up") #string to uppercase
	async def capitalize(self, ctx, arg="​​​no text given to capitalize"):
		await ctx.send(arg.upper())

	@commands.command(name = "ping") #PING PONG PING PONG PING
	async def ping(self, ctx):
		await ctx.send("pong!")

	@commands.command(name="scream") #mix of upper and lower
	async def scream(self, ctx, arg="​​​no text given to scream"):
		await ctx.send("".join(
			[random.choice([i.upper(), i.lower()]) for i in arg]
			))

	@commands.command() #random number b/w num1 and num2
	async def random(self, ctx, num1, num2):
		await ctx.send(random.randint(int(num1), int(num2)))
	@commands.command()

	async def dice(self, ctx): #dice
		await ctx.send("You rolled a " + str(random.randint(1,6)) +"!")

def setup(bot):
	bot.add_cog(Shenanigans(bot))