import discord
from discord.ext import commands
from translate import Translator

class TranslateCog(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def help(self, ctx):
		await ctx.author.send("Thank you for choosing our translation bot. Here are the commands.")
		await ctx.author.send("`!translate [language] [string]`: Make sure to include quotations if your string has several words.")

	@commands.command()
	async def translate(self, ctx, arg1, arg2):
			translator= Translator(to_lang= arg1)
			translation = translator.translate(arg2)
			await ctx.send(translation)
	




def setup(bot):
	bot.add_cog(TranslateCog(bot))