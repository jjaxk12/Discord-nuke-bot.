import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time
import logging
bot = commands.Bot(command_prefix='*')
@bot.command()
async def spam(ctx):
    while True:        
        await ctx.send("ANALLY RAPED BY ME! @everyone @here")
@bot.command(pass_cotext=True)
async def roles(ctx):
    await ctx.message.delete()
    while True:
        guild = ctx.guild
        await guild.create_role(name="BUTT RAPED (.) (.) _1_")
##MAKE CHANNELS##
@bot.command(pass_context=True)
async def channels(ctx):
    await ctx.message.delete()
    guild = ctx.message.guild
    while True:
        await guild.create_text_channel('FUCK YOU CYKA BLYAT')
bot.run("ur token")
