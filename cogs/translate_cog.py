import discord
import discord.abc
from discord.ext import commands
#translations provided by google translate and mymemory
from translate import Translator
from googletrans import Translator as gTranslate

trans = gTranslate()
class TranslateCog(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.command() #sweet sweet help command
	async def help(self, ctx):
		await ctx.author.send("Thank you for choosing our translation bot. Here are the commands.")
		await ctx.author.send("`!translate [language] [string]`: Translates an English string into a new language. Make sure to include quotations if your string has several words.")
		await ctx.author.send("`!English [string]`: Translates a nonenglish string into English. Make sure to include quotations if your string has several words.")
		await ctx.author.send("`!low [string]`: Converts a string into lowercase. Make sure to include quotations if your string has several words.")
		await ctx.author.send("`!up [string]`: Converts a string into uppercase. Make sure to include quotations if your string has several words.")
		await ctx.author.send("`!scream [string]`: Converts a string into a random combination of upper and lowercase. Make sure to include quotations if your string has several words.")
		await ctx.author.send("`!help`: Displays this command")
		await ctx.author.send("`!ping`: Pong!")
		await ctx.author.send("`!quote`: Displays a random quote.")
		await ctx.author.send("`!random [num1] [num2]`: Displays a random number between num1 and num2.")
		await ctx.author.send("`!dice`: Displays a random number between 1 and 6, akin to throwing a dice.")

	@commands.command() #translation command
	async def translate(self, ctx, arg1, arg2):
		translator = Translator(to_lang= arg1)
		translation = translator.translate(arg2)
		await ctx.send(arg2 + " in " + arg1 + " is " + translation)

class Eng(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.command(name="english") #english command
	async def english(self, ctx, arg):
		translator = Translator(to_lang = "English")
		translation = translator.translate(arg)
		await ctx.send(arg + "in English is " + translation)

def setup(bot): 
	bot.add_cog(TranslateCog(bot))
	bot.add_cog(Eng(bot))