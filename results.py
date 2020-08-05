#File for the Results command for the Instinct Bot
import discord
import itertools
from discord.ext import commands
import discord.utils
from discord.utils import get
import asyncio


class Results(commands.Cog):
    """Cog for the Results command"""

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def result(self, ctx):
        channel = ctx.channel
        message = ctx.message
        author = ctx.message.author
        
        author_roles = [role.name for role in ctx.author.roles] #Gets all the roles that the author (person who called the command) has.

        check_role = 'Test'

       
        if check_role in author_roles:

            try:
                def msg_check(m):
                    return m.author == author and m.channel == channel

                #FIRST QUESTION
                await ctx.send('Enter the type of scrim you are hosting (Which Game)') #Question

                result_type_msg = await self.bot.wait_for('message', timeout=20.0, check=msg_check) #The bot waits for an answer to the question

                result_type = result_type_msg.content #Bot stores that information in a variable

                #SECOND QUESTION
                await ctx.send('Who were you playing against?')

                result_opponent_msg = await self.bot.wait_for('message', timeout=20.0, check=msg_check)

                result_opponent = result_opponent_msg.content

                #THIRD QUESTION
                win_emoji = '🤩'
                loss_emoji = '😔'

                outcome_emoji_list = [win_emoji, loss_emoji]


                result_outcome_msg = await ctx.send('Win or loss? React with 🤩 if you won, react with 😔 if you lost')

                for emoji in outcome_emoji_list:
                    await result_outcome_msg.add_reaction(emoji)

                def outcome_check(reaction, user):
                    return user == message.author and str(reaction.emoji) in outcome_emoji_list

                outcome_reaction, user = await self.bot.wait_for('reaction_add', timeout=20.0, check=outcome_check)

                if str(outcome_reaction) == win_emoji:
                    result_outcome = 'Win'
                elif str(outcome_reaction) == loss_emoji:
                    result_outcome = 'Loss'
                
                #FOURTH QUESTION

                await ctx.send("What was the score?")

                result_score_msg = await self.bot.wait_for('message', timeout=20.0, check=msg_check)

                result_score = result_score_msg.content

                #EMBED

                result_embed = discord.Embed(
                    title='SCRIM RESULT',
                    description=f'Results for a {result_type} scrim',
                    color=discord.Color.gold()
                )
                result_embed.add_field(name='OPPONENT', value=result_opponent, inline=False)
                result_embed.add_field(name='OUTCOME', value=result_outcome, inline=False)
                result_embed.add_field(name='SCORE', value=result_score, inline=False)

                #CONFIRM EMBED
                cancel_confirm_msg = await ctx.send(embed=result_embed)

                confirm_reaction = '✔'
                cancel_reaction = '❌' 

                cancel_confirm_reactions = [confirm_reaction, cancel_reaction] 

                for reaction in cancel_confirm_reactions: 
                    await cancel_confirm_msg.add_reaction(reaction) 

                def cancel_confirm_check(reaction, user):
                    return user == message.author and str(reaction.emoji) in cancel_confirm_reactions

                cancel_confirm_reaction, user = await self.bot.wait_for('reaction_add', timeout=20.0, check=cancel_confirm_check) 

                #POST RESULTS OR DELETE EMBED
                if str(cancel_confirm_reaction) == confirm_reaction:
                    await ctx.send("Posting the result!")
                    for channel in ctx.guild.text_channels:
                        if channel.name == 'scrim-results':
                            await channel.send(embed=result_embed) 

            except asyncio.TimeoutError: #If one of the bot.wait_for's times out, the data is scrapped
                await ctx.send("Timed out, please call the command again.") 
        else:
            await ctx.send(f"You don't have the proper credentials to run this command. You need the {check_role} role to call this command")


