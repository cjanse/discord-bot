import discord
import json
from discord.ext import commands

#Using json to hide token but still use token
with open("config.json","r") as f:
    temp = json.load(f)
TOKEN = temp["token"]

description = '''Bella_Bot'''
bot = commands.Bot(command_prefix="?", description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def helloWorld(ctx):
    print('helloWorld command used')
    await ctx.send("Hola mundo")
    
@bot.command()
async def testArgs(ctx, arg1):
    await ctx.send(arg1[0] + arg1[2:])
    
bot.run(TOKEN)
