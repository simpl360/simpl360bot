import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')
bot = commands.Bot(command_prefix="?")

@bot.event
async def on_ready():
    print('Bot is Enabled')

@bot.command()
async def rape(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)

@bot.command()
async def molest(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

@bot.command()
async def harass(ctx, user : discord.Member, message):
    await user.send(message)

bot.run(TOKEN)