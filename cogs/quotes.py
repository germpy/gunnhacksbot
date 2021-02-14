#Inspirational quotes provided by https://zenquotes.io/
import discord
import requests
import json

from discord.ext import commands

class Quotes(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def quote(self, ctx):
		url = "https://zenquotes.io/api/random"
		response = requests.get	(url)
		json_data = json.loads(response.text)
		quote = json_data[0]["q"] + " -" + json_data[0]["a"]
		await ctx.send(quote)
	
	@commands.command(name="quote1")
	async def quote1(self, ctx, arg):
		url =  "https://zenquotes.io/api/quotes/author/sun-tzu/key"
		response = requests.get(url)
		json_data = json.loads(response.text)
		quote = json_data[0]["q"] + " -" + json_data[0]["a"]
		await ctx.send(quote)
	
		

def setup(bot):
	bot.add_cog(Quotes(bot))
