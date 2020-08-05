#INFO & HELP COMMANDS FOR THE INSTINCT SCRIM BOT

import discord
import itertools
from discord.ext import commands
import discord.utils
from discord.utils import get



class Info_Help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def info(self, ctx):
        

        sven_id = 317105924231921675
        shep_id = 498331656822849536

        msg = ctx.message
        bot_prefix = await self.bot.get_prefix(msg)

        help_embed = discord.Embed(
            title='INFO',
            description=f'Information about {self.bot.user.name}\nMade by {self.bot.get_user(shep_id).mention} & {self.bot.get_user(sven_id).mention}',
            color=discord.Color.blue()
        )
        help_embed.add_field(name='Scrim Command', value=f'Called by typing {bot_prefix}scrim into a discord channel\n-\nSets up a custom scrim!', inline=True)
        help_embed.add_field(name='Result Command', value=f'Called by typing {bot_prefix}result into a discord channel\n-\nSends a results embed to a specific channel!', inline=True)
        
        help_embed.add_field(name='Want a Bot?', value='[Click Here](https://discord.gg/tEzJRfw)', inline=False)
        help_embed.set_thumbnail(url=self.bot.user.avatar_url)
        
        await ctx.send(embed=help_embed)