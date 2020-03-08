import discord
from discord.ext import commands
import asyncio
import datetime

class ErrorCog(commands.Cog, name='Help'):

    """Displays this help command."""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        try:
            if hasattr(ctx.command, 'on_error') :
                return
            else:
                embed = discord.Embed(title=f'Error in {ctx.command}', description=f'`{ctx.command.qualified_name} {ctx.command.signature}` \n{error}', color=0x43780)
                await ctx.send(embed=embed)
        except:
            embed = discord.Embed(title=f'Error in {ctx.command}', description=f'{error}', color=0x43780)
            await ctx.send(embed=embed)

    @commands.command()
    async def help(self, ctx, *cog):
        embed = discord.Embed(title="Bot Help", description="**Created by Placid#9684**", color=0xff003d)

        embed.set_footer(text=f'Do <prefix> help <command> for more info on a command.')
        embed.timestamp = datetime.datetime.utcnow()
        embed.add_field(name="**Public [12]**", value="`help`, `ping`, `say`, `support`, `userinfo`, `invite`, `joined`, `roles`, `id`, `delta`, `botinfo`, `avatar`")
        embed.add_field(name="**Fun [6]**", value="`8ball`, `roll`, `flip`, `fact`, `bottles`, `slap`")
        embed.add_field(name="**Moderation [7]**", value="`ban`, `kick`, `purge`, `unban`, `mute`, `unmute`, `softban`")
        embed.add_field(name="**Music [8]**", value="`join`, `leave`, `play`, `pause`, `resume`, `stop`, `queue`, `next`")
        embed.add_field(name="**Config [1]**", value="`prefix`")

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(ErrorCog(bot))
    print('Error is loaded')
