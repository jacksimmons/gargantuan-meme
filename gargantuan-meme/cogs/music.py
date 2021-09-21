import discord
import youtube_dl
import json

from discord.ext import commands

class Music(commands.Cog):

	@commands.command(
		name="join", 
		description="Joins your current voice channel.")
	async def music_join(self, ctx):
		if ctx.author.voice is not None: # If the invoker is in a voice chat...
			if ctx.voice_client is None: # If the bot is not in a voice chat...
				await ctx.author.voice.channel.connect() # Simply connect to their voice chat.
			else:
				await ctx.voice_client.move_to(ctx.author.voice.channel)


def setup(bot):
	bot.add_cog(Music(bot))