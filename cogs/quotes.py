#Inspirational quotes provided by https://zenquotes.io/
import discord 
import requests
import json

from discord.ext import commands

class Quotes(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.command() #random quote
	async def quote(self, ctx):
		url = "https://zenquotes.io/api/random"
		response = requests.get	(url)
		json_data = json.loads(response.text)
		quote = json_data[0]["q"] + " -" + json_data[0]["a"]
		await ctx.send(quote)
	
	@commands.command(name="quotetoday") #today's quote
	async def quotetoday(self, ctx):
		url =  "https://zenquotes.io/api/today"
		response = requests.get(url)
		json_data = json.loads(response.text)
		quote = json_data[0]["q"] + " -" + json_data[0]["a"]
		await ctx.send(quote)

	@commands.command()
	async def quotenumber(self, ctx, arg):
		url = "https://zenquotes.io/api/quotes"
		response = requests.get(url)
		json_data = json.loads(response.text)
		for x in range(int(arg)):
			await ctx.send(json_data[x]["q"] + " -" + json_data[x]["a"])
		#await ctx.send(nice_formatted)
	
		

def setup(bot):
	bot.add_cog(Quotes(bot))
