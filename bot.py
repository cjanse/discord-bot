import discord
import random
import time
from datetime import datetime
import json
import HungerGames
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

#Using json to hide token but still use token
with open("config.json","r") as f:
    temp = json.load(f)
TOKEN = temp["token"]

description = '''Bella_Bot'''
bot = commands.Bot(command_prefix="?", description=description, intents=intents)

#global variables (please forgive me good coding practices)
game = HungerGames.hungerGames()

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('Coming online at ' + datetime.now().strftime("%m/%d/%Y %H:%M:%S"))
    print('------')

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(919618504091652109)
    await channel.send("Hello! Welcome to the server. We're happy you're here. \n\n¡Hola! Bienvenidos al servidor. Estamos felices que estés aquí.")

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(919618504091652109)
    await channel.send("Goodbye \n\nAdiós")

@bot.command()
async def helloWorld(ctx):
    print(str(ctx.author.name) + ' used helloWorld command at ' + datetime.now().strftime("%m/%d/%Y %H:%M:%S"))
    await ctx.send("Hola mundo")
    
@bot.command()
async def hungerGames(ctx, arg1=None, arg2=None, arg3=None, arg4=None, arg5=None, arg6=None, arg7=None, arg8=None, arg9=None,arg10=None,arg11=None,arg12=None, arg13=None, arg14=None, arg15=None, arg16=None, arg17=None,arg18=None,arg19=None,arg20=None):
    print(str(ctx.author.name) + ' used hungerGames command at ' + datetime.now().strftime("%m/%d/%Y %H:%M:%S"))
    tributes = [arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16, arg17, arg18, arg19, arg20]
    try:
        while True:
            tributes.remove(None)
    except ValueError:
        pass
    if (arg1==None):
        await ctx.send("You need to include at least one tribute!")
    else:
        await ctx.send("Executing Hunger Games Simulator...")
        gameString = game.runGame(tributes)
        await ctx.send(gameString)
        
@bot.command()
async def bellaPhoto(ctx):
    print(str(ctx.author.name) + ' used bellaPhoto command at ' + datetime.now().strftime("%m/%d/%Y %H:%M:%S"))
    choice = random.randrange(0,20)
    while True:
        if choice == 0:
            await ctx.send(file=discord.File(r'bella01.jpeg'))
            break
        elif choice == 1:
            await ctx.send(file=discord.File(r'bella02.jpg'))
            break
        elif choice == 2:
            await ctx.send(file=discord.File(r'bella03.JPG'))
            break
        elif choice == 3:
            await ctx.send(file=discord.File(r'bella04.jpg'))
            break
        elif choice == 5:
            await ctx.send(file=discord.File(r'bella06.jpg'))
            break
        elif choice == 6:
            await ctx.send(file=discord.File(r'bella07.jpg'))
            break
        elif choice == 7:
            await ctx.send(file=discord.File(r'bella08.jpg'))
            break
        elif choice == 8:
            await ctx.send(file=discord.File(r'bella09.jpg'))
            break
        elif choice == 10:
            await ctx.send(file=discord.File(r'bella11.jpg'))
            break
        elif choice == 11:
            await ctx.send(file=discord.File(r'bella12.jpg'))
            break
        elif choice == 12:
            await ctx.send(file=discord.File(r'bella13.jpg'))
            break
        elif choice == 13:
            await ctx.send(file=discord.File(r'bella14.jpg'))
            break
        elif choice == 15:
            await ctx.send(file=discord.File(r'bella16.jpg'))
            break
        else:
            choice = random.randrange(0,20)
    
bot.run(TOKEN)
