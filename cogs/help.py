import discord 
from discord.ext import commands

class help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context = True)
    async def help(self, ctx):

        print('Help command received')
        author = ctx.message.author
        print(author)

        embed = discord.Embed(colour = discord.Colour.orange())

        embed.set_author(name = 'Here is a list of commands!')
        embed.add_field(name = '-------------------------------', value = '', inline = False)
        embed.add_field(name = '!help', value = 'Help menu!', inline = False)
        embed.add_field(name = '!hello', value = 'Quick greeting from MooBot.', inline = False)
        embed.add_field(name = '!weather <city>', value = 'Tells you the weather of a city.', inline = False)
        embed.add_field(name = '!rps <choice>', value = 'Play a game of Rock, Paper, Scissors against me!', inline = False)
        embed.add_field(name = '!chat <question>', value = 'I have chatGPT build in, so ask me a question.', inline = False)

        await author.send(embed = embed)


async def setup(client):
    await client.add_cog(help(client))