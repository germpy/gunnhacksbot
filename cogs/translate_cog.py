import discord
import discord.abc
from discord.ext import commands
from translate import Translator
from googletrans import Translator

trans = Translator()
class TranslateCog(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def help(self, ctx):
		await ctx.author.send("Thank you for choosing our translation bot. Here are the commands.")
		await ctx.author.send("`!translate [language] [string]`: Make sure to include quotations if your string has several words.")
		await ctx.author.send("`!low [string]`: Converts a string into lowercase. Make sure to include quotations if your string has several words.")
		await ctx.author.send("`!up [string]`: Converts a string into uppercase. Make sure to include quotations if your string has several words.")
		await ctx.author.send("`!scream [string]`: Converts a string into a random combination of upper and lowercase. Make sure to include quotations if your string has several words.")
		await ctx.author.send("`!help`: displays this command")
		await ctx.author.send("`!ping`: pong!")

	@commands.command()
	async def translate(self, ctx, arg1, arg2):
		translator = Translator(to_lang= arg1)
		translation = translator.translate(arg2)
		await ctx.send(translation)

class Eng(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.command(name="english") #this feels harder than it should be lol
	async def english(self, ctx, ID: discord.Message):
		# print("\n\n",msgID,"\n\n")
		# print(msgID.content)
		#msg = await ctx.fetch_message(msgID)
		#translator = Translator(to_lang = "English")
		#translation = translator.translate(msgID.content)
		#await ctx.send(translation)
		msg = await ctx.fetch_message(ID)
		trans.translate(msg)
		
def setup(bot): #uh how do we get eng to work

	bot.add_cog(TranslateCog(bot))
	bot.add_cog(Eng(bot))#what