import os
import asyncio
import discord

from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="onpeutpasenleverctemerde?",intents=intents,help_command=None)

@bot.event
async def on_ready():
    print(f"{bot.user} est prêt.")
    await bot.tree.sync()
    print(f"Commandes syncronisées !")

async def load_cogs():
    await bot.load_extension('cogs.info')

async def main():
    await load_cogs()
    await bot.start(TOKEN)

asyncio.run(main())
