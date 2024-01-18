import discord 
from discord.ext import commands
import aiohttp

from keys import *

class chat(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def chat(self, ctx: commands.Context, *, question : str):    
        async with aiohttp.ClientSession() as session:
            payload = {
                "model": "gpt-3.5-turbo-instruct",
                "prompt": question,
                "temperature": 0.5,
                "max_tokens": 50,
                "presence_penalty": 0,
                "frequency_penalty": 0,
                "best_of": 1
            }

            headers = {"Authorization": f"Bearer {GPTKEY2}"}

            async with session.post("https://api.openai.com/v1/completions", json = payload, headers = headers) as resp:
                try:
                    response = await resp.json()
                    # Check if 'choices' key exists in the response
                    if 'choices' in response:
                        text_response = response["choices"][0]["text"]
                    else:
                        text_response = "Error: 'choices' key not found in the response."
                    embed = discord.Embed(title="ChatGPT's response:", description = text_response)
                    await ctx.reply(embed=embed)
                    print(response)
                except Exception as e:
                    print(f"Error processing API response: {e}")

async def setup(client):
    await client.add_cog(chat(client))