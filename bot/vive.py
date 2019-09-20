from discord.ext import commands
import discord
import random
prefix = "?"
bot = commands.Bot(command_prefix=prefix)

@bot.event
async def on_ready():
    print(bot.user.name)
    print(bot.user.id)

@bot.command()
async def ping(ctx):
    '''Shows the bot\'s latency'''
    latency = bot.latency
    await ctx.send("**Pong!** Latency is {}".format(latency))

@bot.command()
async def nsfwpic(ctx):
	'''pull an nsfw pic from the github repo'''
	images = ['https://raw.githubusercontent.com/secrethay/post/master/Art/All/001690acb8bdbadbb32a031aad8d4a09.png','https://raw.githubusercontent.com/secrethay/post/master/Art/All/4d615acf39c5826d76a6f798eeb2f2df.jpeg','https://raw.githubusercontent.com/secrethay/post/master/Art/All/5f2f6203c29e354f4053b6abe34f6e99.png']
    nsfw = random.choice(images)
	await ctx.send(nsfw)

bot.run('')
