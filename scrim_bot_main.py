#Instinct Project

import discord
import itertools
from discord.ext import commands
import discord.utils
#Importing Cogs
import scrim
import results
import info_help

bot = commands.Bot(command_prefix='?')

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('Testing Commands'))
    print(f'Logged in as: {bot.user.name}')
    print(f'With ID: {bot.user.id}')

 




bot.add_cog(scrim.Scrim(bot))
bot.add_cog(results.Results(bot))
bot.add_cog(info_help.Info_Help(bot))

with open('scrim_bot_token.txt', 'r') as f:
    bot.run(f.read().strip())