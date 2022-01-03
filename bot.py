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
userTributes = []
bellaPhotoChoices = []

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
    if ctx.author.name not in userTributes:
        userTributes.append(ctx.author.name)
    try:
        while True:
            tributes.remove(None)
    except ValueError:
        pass
    if (arg1==None):
        await ctx.send("Welcome to the Quarter Quell where everyone who used the hungerGames command will now participate in their own Hunger Games!")
        gameString = game.runGame(userTributes)
        await ctx.send(gameString)
    else:
        await ctx.send("Executing Hunger Games Simulator...")
        gameString = game.runGame(tributes)
        await ctx.send(gameString)
        
@bot.command()
async def bellaPhoto(ctx, action=None):
    print(str(ctx.author.name) + ' used bellaPhoto command at ' + datetime.now().strftime("%m/%d/%Y %H:%M:%S"))
    if (not (action == None) and action.lower() == "status"):
        bellaString = ""
        for x in range (0,18):
            if x in bellaPhotoChoices:
                bellaString += "bella" + str(x+1) + " - found\n"
            else:
                bellaString += "bella" + str(x+1) + " - missing\n"
        await ctx.send(bellaString)
        return
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
        elif choice == 4:
            await ctx.send(file=discord.File(r'bella05.jpg'))
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
        elif choice == 9:
            await ctx.send(file=discord.File(r'bella10.jpg'))
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
        elif choice == 14:
            await ctx.send(file=discord.File(r'bella15.jpg'))
            break
        elif choice == 15:
            await ctx.send(file=discord.File(r'bella16.jpg'))
            break
        elif choice == 16:
            await ctx.send(file=discord.File(r'bella17.jpg'))
            break
        elif choice == 17:
            await ctx.send(file=discord.File(r'bella18.jpg'))
            break
        else:
            choice = random.randrange(0,20)
        
    if choice not in bellaPhotoChoices or len(bellaPhotoChoices) == 0:
        bellaString = "Congrats you a found a new Bella photo! bella" + str(choice+1)
        bellaPhotoChoices.append(choice)
        if len(bellaPhotoChoices) < 18:
            if len(bellaPhotoChoices) == 17:
                bellaString += "\nYou are still missing " + str(18-len(bellaPhotoChoices)) + " Bella Photo!"
            else:
                bellaString += "\nYou are still missing " + str(18-len(bellaPhotoChoices)) + " Bella Photos!"
        else:    
            bellaString += "\nYOU FOUND ALL THE BELLA PHOTOS!!!"
        await ctx.send(bellaString)
            
    
@bot.command(pass_context = True)
async def bellaVoice(ctx, action=None):
    if (action != None and action.lower() == 'join'):
        if (ctx.author.voice):
            channel = ctx.message.author.voice.channel
            await channel.connect()
        else:
            await ctx.send("You are not not in a voice channel, you must be in a voice channel to run this command")
    elif (action != None and action.lower() == 'leave'):
        if (ctx.voice_client):
            await ctx.guild.voice_client.disconect()
            await ctx.send("I left the voice channel")
        else:
            await ctx.send("I am not in a voice channel")

bot.run(TOKEN)
