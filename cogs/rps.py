import discord 
from discord.ext import commands
import random

class rps(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def rps(self, ctx, choice):

        choices = ["rock", "paper", "scissors"]

        compChoice = random.choice(choices)

        if choice not in choices:
            await ctx.send("Invaild input, please choose between : rock, paper or scissors!")
        else:
            compChoice = random.choice(choices)

            if choice == "rock":
                if compChoice == "rock":
                    await ctx.send("I got rock! Its a tie!")
                elif compChoice == "paper":
                    await ctx.send("I got paper! You lose!")
                else:
                    await ctx.send("I got scissors! You win!")

            if choice == "paper":    
                if compChoice == "rock":
                    await ctx.send("I got rock! You win!")
                elif compChoice == "paper":
                    await ctx.send("I got paper! Its a tie!")
                else:
                    await ctx.send("I got scissors! You lose!")
                    
            if choice == "scissors":    
                if compChoice == "rock":
                    await ctx.send("I got rock! You lose!")
                elif compChoice == "paper":
                    await ctx.send("I got paper! You win!")
                else:
                    await ctx.send("I got scissors! Its a tie!")

async def setup(client):
    await client.add_cog(rps(client))