#dependencies 
import discord 
from discord.ext import commands
import os
import asyncio

#Imports the api keys.
from keys import *


intents = discord.Intents.all()
client = commands.Bot(command_prefix = '!', intents = intents)

#Removes help command inorder to add custom help command.
client.remove_command('help')

#Sends confirmation when bot is ready to use
@client.event
async def on_ready():
    print("MooBot is ready!")
    print("-----------------------")

#Basic greeting using ctx.send.
@client.command()
async def hello(ctx):
    await ctx.send("Hello! I'm MooBot type '!help' for a list of commands!")

#Event command that welcomes new users.
@client.event
async def on_member_join(member):

    #Gets the channel that the message needs to be sent to.
    channel = member.guild.system_channel

    #Mentions the user.
    await channel.send(f"{member.mention}")

    #An embeded welcome message for new users.
    embed = discord.Embed(title = f"Welcome to the server!", colour = discord.Colour.red())
    embed.add_field(name = 'My name is MooBot!', value = 'Type !help for a list of commands!', inline = False)

    #Outputs the embeded message into the channel.
    await channel.send(embed = embed)

#loads the files with the cogs
async def load():
    #checks the /cogs folder.
    for filename in os.listdir('./cogs'):
        #Checks for files that end with .py.
        if filename.endswith('.py'):
            #loads these files.
            await client.load_extension(f'cogs.{filename[:-3]}')

#Main function that loads the cogs and starts the bot.
async def main():
    await load()
    await client.start(BOTTOKEN)

#Event loop that runs the main function.
asyncio.run(main())