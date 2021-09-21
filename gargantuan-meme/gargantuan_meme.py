import discord
from datetime import datetime as d

start = d.timestamp(d.now())

#Import 'commands' which allows the creation of commands that are 'invoked' by a certain keyword
#e.g. 'help', which displays the default help command. This keyword must have the 'prefix' before it
#for example if the prefix is '.', then the command would be activated by sending '.help' in a Discord
#channel that the bot has access to and can send messages to.
from discord.ext import commands

cogs = ["music.py"]

def get_prefix(bot, message):
	prefixes = ["."]

	return commands.when_mentioned_or(*prefixes)(bot, message)

bot = commands.Bot(
	command_prefix = get_prefix,
	description = "Big Chunky Bulgarian Bloke",
	owner_id = 354995879565852672,
	case_insensitive = True
)

@bot.event
async def on_ready():
    print(f'Load time: {( d.timestamp( d.now() ) - start ) } seconds.')
    print(f'Logged in as {bot.user} [id: {bot.user.id}]')
    print(f'Latency: {bot.latency}')
    print(f'Created at: {bot.user.created_at.hour}:{bot.user.created_at.minute} {bot.user.created_at.day}/{bot.user.created_at.month}/{bot.user.created_at.year}')
    print('---Ready---')
    await bot.change_presence(activity=discord.Activity(name=f'{len(bot.users)*1420} chungas', status=discord.Status.offline, type=3))
    for cog in cogs:
        bot.load_extension(cog)
    channel = ''
    guild = ''
    return

@bot.event
async def on_message(message):
    if isinstance(message.channel, discord.TextChannel):
        if message.author != bot.user:
            if message.guild.me.permissions_in(message.channel).send_messages:
                await bot.process_commands(message)
            else:
                print("Can't send message")

        if message.author.id == 267395298370781194:
            await message.channel.send("Stinky")

bot.run("ODg3NzI1MDg4ODQ0MTc3NDE5.YUIUag.KxsCc5L5McEV6BFy0nqvW1ezoq4", bot=True, reconnect=True)