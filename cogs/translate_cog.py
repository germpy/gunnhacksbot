import discord
import discord.abc
from discord.ext import commands
#translations provided by google translate
from translate import Translator
from googletrans import Translator as gTranslate

trans = gTranslate()
class TranslateCog(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def help(self, ctx):
		await ctx.author.send("Thank you for choosing our translation bot. Here are the commands.")
		await ctx.author.send("**translation**")
		await ctx.author.send("`!translate [language] [string]`: Translates an English string into a new language. Make sure to include quotations if your string has several words.")
		await ctx.author.send("**shenanigans/other**")
		await ctx.author.send("`!low [string]`: Converts a string into lowercase. Make sure to include quotations if your string has several words.")
		await ctx.author.send("`!up [string]`: Converts a string into uppercase. Make sure to include quotations if your string has several words.")
		await ctx.author.send("`!scream [string]`: Converts a string into a random combination of upper and lowercase. Make sure to include quotations if your string has several words.")
		await ctx.author.send("`!help`: Displays this command")
		await ctx.author.send("`!ping`: Pong!")
		await ctx.author.send("`!quote`: Displays a random quote.")
 

	@commands.command()
	async def translate(self, ctx, arg1, arg2):
		translator = Translator(to_lang= arg1)
		translation = translator.translate(arg2)
		await ctx.send(translation)


class Eng(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	# @bot.event
	# async def on_reaction_add(reaction, user):
	# 	if str(reaction.emoji) == "\U0001F534":
	# 		# do a thing
	# 		pass

	@commands.command(name="english")
	async def english(self, ctx, arg):
		translator = Translator(to_lang = "English")
		translation = translator.translate(arg)
		await ctx.send(translation)
		#msg = await ctx.fetch_message(ID)
		#msg = ID.content
		# print("CONTENT: ",msg,"\n")
		# res = trans.translate(msg)
		# print(res)
		#translator = Translator(to_lang = "English")
		#translation = translator.translate(msg)
		await ctx.send(arg)	

def setup(bot): #uh how do we get eng to work
	bot.add_cog(TranslateCog(bot))
	bot.add_cog(Eng(bot))