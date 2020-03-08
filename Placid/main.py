import discord
from discord.ext import commands
import asyncio
import datetime
import sys
import sqlite3
import json
import random
import typing
from discord.utils import get
import youtube_dl
import os
import shutil
from os import system




def get_prefix(bot, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

bot = commands.Bot(command_prefix = get_prefix)

initial_extensions = ['cogs.help']



@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('A multipurpose discord bot. k!help for more info.'))
    print('Bot is online')

bot.help_command = None


#Ping command
@bot.command()
async def ping(ctx):
    embed = discord.Embed(title="**Ping**", description=f'Pong! My ping is: `{round(bot.latency * 1000)}ms`', color=discord.Color.red())
    embed.set_footer(text='Bot made by Placid#9684')
    embed.timestamp = datetime.datetime.utcnow()

    await ctx.send(embed=embed)

@bot.command(aliases=['helpping'])
async def pinghelp(ctx):
    embed = discord.Embed(title="**Pinghelp**", description=f'Shows my ping to discord. Correct usage:\n\n`<prefix> ping`', color=discord.Color.red())
    embed.set_footer(text='Bot made by Placid#9684')
    embed.timestamp = datetime.datetime.utcnow()

    await ctx.send(embed=embed)

#Flip command
@bot.command(aliases=['coin'])
async def flip(ctx):
    responses = ['Heads',
                 'Tails']

    embed = discord.Embed(title="**Dice**", description=f'Congrats! Your coin landed on `{random.choice(responses)}`!', color=discord.Color.red())
    embed.set_footer(text='Bot made by Placid#9684')
    embed.timestamp = datetime.datetime.utcnow()

    await ctx.send(embed=embed)

@bot.command(aliases=['helpflip'])
async def fliphelp(ctx):
    embed = discord.Embed(title="**Fliphelp**", description=f'Flips a coin and returns an output of either `heads` or `tails`.\n\nCorrect usage: `<prefix> flip`', color=discord.Color.red())
    embed.set_footer(text='Bot made by Placid#9684')
    embed.timestamp = datetime.datetime.utcnow()

    await ctx.send(embed=embed)

#Fact command
@bot.command(aliases=['interesting'])
async def fact(ctx):
    responses = ['Some cats are actually allergic to humans',
                 'There is a fruit that tastes like chocolate pudding.',
                 'Competitive art used to be in the Olympics.',
                 'A chefs hat has exactly 100 pleats.',
                 'The majority of your brain is fat.',
                 'Oranges arent naturally occurring fruits.',
                 'Most wasabi in the U.S. isnt really wasabi.',
                 'Stop signs used to be yellow.',
                 'Green Eggs and Ham started as a bet.',
                 'Too much water can kill you.',
                 'The hottest temperature ever recorded on Earth was 2 billion degrees kelvin.',
                 'High heels were originally worn by men.',
                 'You might be drinking water that is older than the solar system.',
                 'Queen Elizabeth II is a trained mechanic.',
                 'New York was briefly named "New Orange."',
                 'Moonshiners used "cow shoes" to disguise their footprints during Prohibition.',
                 'It takes 364 licks to get to the center of a Tootsie Pop.',
                 'Tree rings get wider during wet years.',
                 'The hottest inhabited place in the world is in Ethiopia.',
                 'Sea otters hold hands while they sleep.',
                 'Chainsaws, the horror-movie murder weapon of choice, were invented for aid in childbirth 😊',
                 'Theres an island in Japan you can visit thats inhabited only by friendly bunnies.']
    embed = discord.Embed(title="**Fact**", description=f'{random.choice(responses)}', color=discord.Color.red())
    embed.set_footer(text='Bot made by Placid#9684')
    embed.timestamp = datetime.datetime.utcnow()

    await ctx.send(embed=embed)

@bot.command(aliases=['helpfact'])
async def facthelp(ctx):
    embed = discord.Embed(title="**Facthelp**", description=f'Tells you a cool random fact. Correct usage:\n\n`<prefix> fact`', color=discord.Color.red())
    embed.set_footer(text='Bot made by Placid#9684')
    embed.timestamp = datetime.datetime.utcnow()

    await ctx.send(embed=embed)

#Roll command
@bot.command(aliases=['dice'])
async def roll(ctx):
    responses = ['1',
                 '2',
                 '3',
                 '4',
                 '5',
                 '6']
    embed = discord.Embed(title="**Dice**", description=f'Congrats! Your dice landed on `{random.choice(responses)}`!', color=discord.Color.red())
    embed.set_footer(text='Bot made by Placid#9684')
    embed.timestamp = datetime.datetime.utcnow()

    await ctx.send(embed=embed)

@bot.command(aliases=['helproll'])
async def rollhelp(ctx):
    embed = discord.Embed(title="**Rollhelp**", description=f'Rolls a dice and returns an output of `1-6`.\n\nCorrect usage: `<prefix> ping`', color=discord.Color.red())
    embed.set_footer(text='Bot made by Placid#9684')
    embed.timestamp = datetime.datetime.utcnow()

    await ctx.send(embed=embed)

#Prefix command
@bot.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = 'k!'

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@bot.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@bot.command()
@commands.has_permissions(manage_guild=True)
async def prefix(ctx, prefix):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

    embed = discord.Embed(title="**New Prefix**", description=f'Prefix changed to: `{prefix}`', color=discord.Color.red())
    embed.set_footer(text='Bot made by Placid#9684')
    embed.timestamp = datetime.datetime.utcnow()

    await ctx.send(embed=embed)

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}', file=sys.stderr)
            traceback.print_exc()

@bot.command(aliases=['helpprefix'])
async def prefixhelp(ctx):
    embed = discord.Embed(title="**Prefixhelp**", description=f'Changes the bot\'s prefix.\n\nCorrect usage: `<prefix> prefix <newprefix>`', color=discord.Color.red())
    embed.set_footer(text='Bot made by Placid#9684')
    embed.timestamp = datetime.datetime.utcnow()

    await ctx.send(embed=embed)

#Eightball command
@bot.command(aliases=['8ball', 'ask', 'curious'])
async def _8ball(ctx, *, question):
    responses = ['As I see it, yes.',
                'Ask again later.',
                'Better not tell you now.',
                'Cannot predict now.',
                'Concentrate and ask again.',
                'Don’t count on it.',
                'It is certain.',
                'It is decidedly so.',
                'Most likely.',
                'My reply is no.',
                'My sources say no.',
                'Outlook not so good.',
                'Outlook good.',
                'Reply hazy, try again.',
                'Signs point to yes.',
                'Very doubtful.',
                'Without a doubt.',
                'Yes.',
                'Yes – definitely.',
                'You may rely on it.']
    embed = discord.Embed(title="**8ball**", description=f'Question: {question}\nAnswer: {random.choice(responses)}', color=discord.Color.red())
    embed.set_footer(text='Bot made by Placid#9684')
    embed.timestamp = datetime.datetime.utcnow()

    await ctx.send(embed=embed)

@bot.command(aliases=['help8ball'])
async def _8ballhelp(ctx):
    embed = discord.Embed(title="**8ballhelp**", description=f'Answers a question you ask.\n\nCorrect usage: `<prefix> 8ball <question>`', color=discord.Color.red())
    embed.set_footer(text='Bot made by Placid#9684')
    embed.timestamp = datetime.datetime.utcnow()

    await ctx.send(embed=embed)

#Say command
@bot.command(aliases=['speak', 'tell'])
async def say(ctx, *, arg1):
    embed = discord.Embed(title="**Say**", description=('{}'.format(arg1)), color=discord.Color.red())
    embed.set_footer(text='Bot made by Placid#9684')
    embed.timestamp = datetime.datetime.utcnow()

    await ctx.send(embed=embed)

@bot.command(aliases=['helpsay'])
async def sayhelp(ctx):
    embed = discord.Embed(title="**Sayhelp**", description=f'Repeats what you wanted me to say.\n\nCorrect usage: `<prefix> say <text>`', color=discord.Color.red())
    embed.set_footer(text='Bot made by Placid#9684')
    embed.timestamp = datetime.datetime.utcnow()

    await ctx.send(embed=embed)

#Ban command
@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    embed = discord.Embed(title="**Ban**", description=f'Successfully banned {member.mention}!', color=discord.Color.red())
    embed.set_footer(text='Bot made by Placid#9684')
    embed.timestamp = datetime.datetime.utcnow()

    await ctx.send(embed=embed)

@bot.command(aliases=['helpban'])
async def banhelp(ctx):
    embed = discord.Embed(title="**Banhelp**", description=f'Ban\'s a user from the guild.\n\nCorrect usage: `<prefix> ban <member>`', color=discord.Color.red())
    embed.set_footer(text='Bot made by Placid#9684')
    embed.timestamp = datetime.datetime.utcnow()

    await ctx.send(embed=embed)

#Purge command
@bot.command(aliases=['clear'])
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@bot.command(aliases=['helppurge'])
async def purgehelp(ctx):
    embed = discord.Embed(title="**Purgehelp**", description=f'Purges the specified amount of messages.\n\nCorrect usage: `<prefix> purge <amount>` (Default value for purge is 5 messages.)', color=discord.Color.red())
    embed.set_footer(text='Bot made by Placid#9684')
    embed.timestamp = datetime.datetime.utcnow()

    await ctx.send(embed=embed)

#Unban command
@bot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if(user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            embed = discord.Embed(title="**Unban**", description=f'Successfully unbanned {user.mention}!', color=discord.Color.red())
            embed.set_footer(text='Bot made by Placid#9684')
            embed.timestamp = datetime.datetime.utcnow()

            await ctx.send(embed=embed)
            return

@bot.command(aliases=['helpunban'])
async def unbanhelp(ctx):
    embed = discord.Embed(title="**Unbanhelp**", description=f'Unbans a user already banned in the guild.\n\nCorrect usage: `<prefix> unban <user>`', color=discord.Color.red())
    embed.set_footer(text='Bot made by Placid#9684')
    embed.timestamp = datetime.datetime.utcnow()

    await ctx.send(embed=embed)

#Kick command
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    embed = discord.Embed(title="**Kick**", description=f'Successfully kicked {member.mention}!', color=discord.Color.red())
    embed.set_footer(text='Bot made by Placid#9684')
    embed.timestamp = datetime.datetime.utcnow()

    await ctx.send(embed=embed)

@bot.command(aliases=['helpkick'])
async def kickhelp(ctx):
    embed = discord.Embed(title="**Kickhelp**", description=f'Kicks the specified user.\n\nCorrect usage: `<prefix> kick <user>`', color=discord.Color.red())
    embed.set_footer(text='Bot made by Placid#9684')
    embed.timestamp = datetime.datetime.utcnow()

    await ctx.send(embed=embed)

#Random Nickname thing
@bot.event
async def on_member_update(before, after):
    n = after.nick
    if n:
        if n.lower().count("Placid") > 0:
            last = before.nick
            if last:
                await after.edit(nick=last)
            else:
                await after.edit(nick="NO STOP THAT lul")

#Mute command
@bot.command()
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member : discord.Member):
    guild = ctx.guild

    for role in guild.roles:
        if role.name == "Muted":
            await member.add_roles(role)
            embed = discord.Embed(title="**Mute**", description=("{} has been muted.".format(member.mention,ctx.author.mention)), color=discord.Color.blue())
            embed.set_footer(text='Bot made by Placid#9684')
            embed.timestamp = datetime.datetime.utcnow()

            await ctx.send(embed=embed)
            return

            overwrite = discord.PermissionsOverwrite(send_messages=False)
            newRole = await guild.create_role(name="Muted")

            for channel in guild.text_channels:
                await channel.set_permissions(newRole,overwrite=overwrite)

            await member.add_roles(newRole)
            await ctx.send("{} has been muted" .format(member.mention,ctx.author.mention))

@bot.command(aliases=['helpmute'])
async def mutehelp(ctx):
    embed = discord.Embed(title="**Mutehelp**", description=f'Mutes the specified user (Server must already have role named "Muted" for this command to work; you must also assign the role to every channel where anyone with the role cannot speak in the channel.).\n\nCorrect usage: `<prefix> mute <member>`', color=discord.Color.red())
    embed.set_footer(text='Bot made by Placid#9684')
    embed.timestamp = datetime.datetime.utcnow()

    await ctx.send(embed=embed)

#Unmute command
@bot.command()
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member :  discord.Member):
    guild = ctx.guild

    for role in guild.roles:
        if role.name == "Muted":
            await member.remove_roles(role)
            embed = discord.Embed(title="**Unmute**", description=("{} has been unmuted." .format(member.mention,ctx.author.mention)), color=discord.Color.blue())
            embed.set_footer(text='Bot made by Placid#9684')
            embed.timestamp = datetime.datetime.utcnow()

            await ctx.send(embed=embed)
            return

@bot.command(aliases=['helpunmute'])
async def unmutehelp(ctx):
    embed = discord.Embed(title="**Unmutehelp**", description=f'Unmutes the specified member (See the command "mutehelp" for more info).\n\nCorrect usage: `<prefix> unmute <member>`', color=discord.Color.red())
    embed.set_footer(text='Bot made by Placid#9684')
    embed.timestamp = datetime.datetime.utcnow()

    await ctx.send(embed=embed)



#Support command
@bot.command()
async def support(ctx):
    embed = discord.Embed(title="**Support**", description="Support me! https://www.youtube.com/channel/UC3wAKfPNFys8Sb9VhhITyxQ?view_as=subscriber", color=discord.Color.red())
    embed.set_footer(text='Bot made by Placid#9684')
    embed.timestamp = datetime.datetime.utcnow()

    await ctx.send(embed=embed)

@bot.command(aliases=['helpsupport'])
async def supporthelp(ctx):
    embed = discord.Embed(title="**Supporthelp**", description=f'Supports my creator, Placid#9684.\n\nCorrect usage: `<prefix> support`', color=discord.Color.red())
    embed.set_footer(text='Bot made by Placid#9684')
    embed.timestamp = datetime.datetime.utcnow()

    await ctx.send(embed=embed)

#Invite command
@bot.command()
async def invite(ctx):
    embed = discord.Embed(title="**Invite**", description="Invite me here: https://discordapp.com/api/oauth2/authorize?client_id=666682664303984646&permissions=8&scope=bot", color=discord.Color.blue())
    embed.set_footer(text='Bot made by Placid#9684')
    embed.timestamp = datetime.datetime.utcnow()

    await ctx.send(embed=embed)

@bot.command(aliases=['helpinvite'])
async def invitehelp(ctx):
    embed = discord.Embed(title="**Invitehelp**", description=f'Sends you my invite link. Correct usage:\n\n`<prefix> invite`', color=discord.Color.red())
    embed.set_footer(text='Bot made by Placid#9684')
    embed.timestamp = datetime.datetime.utcnow()

    await ctx.send(embed=embed)

#Userinfo command
@bot.command(aliases=['ui'])
async def userinfo(ctx, member: discord.Member = None):
    member = ctx.author if not member else member
    roles = [role for role in member.roles]

    embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

    embed.set_author(name=f"User Info - {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

    embed.add_field(name="ID:", value=member.id)
    embed.add_field(name="Guild name:", value=member.display_name)

    embed.add_field(name="Created at:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Joined at:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

    embed.add_field(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles]))
    embed.add_field(name="Highest role:", value=member.top_role.mention)

    embed.add_field(name="Bot?", value=member.bot)

    await ctx.send(embed=embed)

@bot.command(aliases=['helpuserinfo'])
async def userinfohelp(ctx):
    embed = discord.Embed(title="**Userinfohelp**", description=f'Sends you info about the specified user.\n\nCorrect usage: `<prefix> userinfo <user>`', color=discord.Color.red())
    embed.set_footer(text='Bot made by Placid#9684')
    embed.timestamp = datetime.datetime.utcnow()

    await ctx.send(embed=embed)

#Delta command
class JoinDistance:
    def __init__(self, joined, created):
        self.joined = joined
        self.created = created

    @classmethod
    async def convert(cls, ctx, argument):
        member = await commands.MemberConverter().convert(ctx, argument)
        return cls(member.joined_at, member.created_at)

    @property
    def delta(self):
        return self.joined - self.created

@bot.command()
async def delta(ctx, *, member: JoinDistance):
    is_new = member.delta.days < 100
    if is_new:
        embed = discord.Embed(title="**New**", description='Hey you\'re pretty new to this server!', color=discord.Color.red())
    else:
        embed = discord.Embed(title="**Old**", description='Hey you\'re not so new to this server.', color=discord.Color.red())

    await ctx.send(embed=embed)


@bot.command(aliases=['helpdelta'])
async def deltahelp(ctx):
    embed = discord.Embed(title="**Deltahelp**", description=f'Tells whether or not your account joined the server 100+ days ago.\n\nCorrect usage: `<prefix> delta <member>`', color=discord.Color.red())
    embed.set_footer(text='Bot made by Placid#9684')
    embed.timestamp = datetime.datetime.utcnow()

    await ctx.send(embed=embed)


#Joined command
@bot.command()
async def joined(ctx, *, member: discord.Member = None):
    member = ctx.author if not member else member
    embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)
    embed.set_author(name=f"Joined - {member}")
    embed.add_field(name="Joined at:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.set_footer(text='Bot made by Placid#9684')
    embed.timestamp = datetime.datetime.utcnow()

    await ctx.send(embed=embed)

@bot.command(aliases=['helpjoined'])
async def joinedhelp(ctx):
    embed = discord.Embed(title="**Joinedhelp**", description=f'Tells when the specified user joined the server.\n\nCorrect usage: `<prefix> joined <user>`', color=discord.Color.red())
    embed.set_footer(text='Bot made by Placid#9684')
    embed.timestamp = datetime.datetime.utcnow()

    await ctx.send(embed=embed)

#Created command
@bot.command()
async def created(ctx, *, member: discord.Member =  None):
    member = ctx.author if not member else member
    embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)
    embed.set_author(name=f"Created - {member}")
    embed.add_field(name="Created at:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.set_footer(text='Bot made by Placid#9684')
    embed.timestamp = datetime.datetime.utcnow()

    await ctx.send(embed=embed)

@bot.command(aliases=['helpcreated'])
async def createdhelp(ctx):
    embed = discord.Embed(title="**Createdhelp**", description=f'Tells you when the specified user created their account.\n\nCorrect usage: `<prefix> created <user>`', color=discord.Color.red())
    embed.set_footer(text='Bot made by Placid#9684')
    embed.timestamp = datetime.datetime.utcnow()

    await ctx.send(embed=embed)

#Roles command
@bot.command()
async def roles(ctx, *, member: discord.Member =  None):
    member = ctx.author if not member else member
    roles = [role for role in member.roles]
    embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)
    embed.set_author(name=f"Roles - {member}")
    embed.add_field(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles]))
    embed.set_footer(text='Bot made by Placid#9684')
    embed.timestamp = datetime.datetime.utcnow()

    await ctx.send(embed=embed)

@bot.command(aliases=['helproles'])
async def roleshelp(ctx):
    embed = discord.Embed(title="**Roleshelp**", description=f'Tells you how many roles the specified user has.\n\nCorrect usage: `<prefix> roles <user>`', color=discord.Color.red())
    embed.set_footer(text='Bot made by Placid#9684')
    embed.timestamp = datetime.datetime.utcnow()

    await ctx.send(embed=embed)

#ID command
@bot.command()
async def id(ctx, *, member: discord.Member =  None):
    member = ctx.author if not member else member
    embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)
    embed.set_author(name=f"ID - {member}")
    embed.add_field(name="ID:", value=member.id)
    embed.set_footer(text='Bot made by Placid#9684')
    embed.timestamp = datetime.datetime.utcnow()

    await ctx.send(embed=embed)

@bot.command(aliases=['helpid'])
async def idhelp(ctx):
    embed = discord.Embed(title="**IDhelp**", description=f'Tell you the specified user\'s Discord ID.\n\nCorrect usage: `<prefix> id <user>`', color=discord.Color.red())
    embed.set_footer(text='Bot made by Placid#9684')
    embed.timestamp = datetime.datetime.utcnow()

    await ctx.send(embed=embed)

#Botinfo command
@bot.command(aliases=['bi'])
async def botinfo(ctx):
    embed = discord.Embed(title="Bot Info", color=0xff003d)
    embed.add_field(name="**Bot Version**", value="`v1.3`")
    embed.add_field(name="**Language**", value="`Python`")
    embed.add_field(name="**Library**", value="`Discord.py`")
    embed.add_field(name="**Bot Owner**", value="`Placid#9684`")
    embed.add_field(name="**Python**", value="`Version 3.8.1`")
    embed.add_field(name="**Default Prefix**", value="`k!`")
    embed.add_field(name="**Bot Name**", value="`MPDb`")
    embed.add_field(name="**Bot Discriminator**", value="`3678`")
    embed.set_footer(text='Bot made by Placid#9684')
    embed.timestamp = datetime.datetime.utcnow()

    await ctx.send(embed=embed)

@bot.command(aliases=['helpbotinfo'])
async def botinfohelp(ctx):
    embed = discord.Embed(title="**Botinfohelp**", description=f'Gives you the stats and information on myself.\n\nCorrect usage: `<prefix> botinfo`', color=discord.Color.red())
    embed.set_footer(text='Bot made by Placid#9684')
    embed.timestamp = datetime.datetime.utcnow()

    await ctx.send(embed=embed)


#Eval command
def is_owner():
    async def predicate(ctx):
        return ctx.author.id == 490686384210837505
    return commands.check(predicate)

@bot.command(name='eval')
@is_owner()
async def _eval(ctx, *, code):
    embed = discord.Embed(title="**Eval**", description=(eval(code)), color=discord.Color.red())
    embed.set_footer(text='Bot made by Placid#9684')
    embed.timestamp = datetime.datetime.utcnow()

    await ctx.send(embed=embed)

#Slap command
@bot.command()
async def slap(ctx, members: commands.Greedy[discord.Member], *, reason='no reason'):
    slapped = ", ".join(x.name for x in members)
    embed = discord.Embed(title="**Slap**", description=('{} just got slapped for {}'.format(slapped, reason)), color=discord.Color.red())
    embed.set_footer(text='Bot made by Placid#9684')
    embed.timestamp = datetime.datetime.utcnow()

    await ctx.send(embed=embed)

@bot.command(aliases=['helpslap'])
async def slaphelp(ctx):
    embed = discord.Embed(title="**Slaphelp**", description=f'Slaps the specified member!\n\nCorrect usage: `<prefix> slap <member>`', color=discord.Color.red())
    embed.set_footer(text='Bot made by Placid#9684')
    embed.timestamp = datetime.datetime.utcnow()

    await ctx.send(embed=embed)

#Bottles command
@bot.command()
async def bottles(ctx, amount: typing.Optional[int] = 99, *, liquid="beer"):
    embed = discord.Embed(title="**Bottles**", description=('{} bottles of {} on the wall!'.format(amount, liquid)), color=discord.Color.red())
    embed.set_footer(text='Bot made by Placid#9684')
    embed.timestamp = datetime.datetime.utcnow()

    await ctx.send(embed=embed)

@bot.command(aliases=['helpbottles'])
async def bottleshelp(ctx):
    embed = discord.Embed(title="**Bottleshelp**", description=f'99 bottles of beer on the wall!\n\nCorrect usage: `<prefix> <numberofbottles> <typeofliquid>`', color=discord.Color.red())
    embed.set_footer(text='Bot made by Placid#9684')
    embed.timestamp = datetime.datetime.utcnow()

    await ctx.send(embed=embed)


#Music commands
@bot.command(pass_context=True, aliases=['j', 'joi'])
async def join(ctx):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    await voice.disconnect()

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        print(f"The bot has connected to {channel}\n")

    embed = discord.Embed(title="**Join**", description=(f"Joined {channel}"), color=discord.Color.red())
    embed.set_footer(text='Bot made by Placid#9684')
    embed.timestamp = datetime.datetime.utcnow()

    await ctx.send(embed=embed)


@bot.command(pass_context=True, aliases=['l', 'lea'])
async def leave(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.disconnect()
        print(f"The bot has left {channel}")
        print("Bot was told to leave voice channel, but was not in one")
        embed = discord.Embed(title="**Leave**", description=(f"Left {channel}"), color=discord.Color.red())
        embed.set_footer(text='Bot made by Placid#9684')
        embed.timestamp = datetime.datetime.utcnow()

        await ctx.send(embed=embed)
    else:
        print("Bot was told to leave voice channel, but was not in one")
        embed = discord.Embed(title="**Leave**", description=("Don't think I am in a voice channel"), color=discord.Color.red())
        embed.set_footer(text='Bot made by Placid#9684')
        embed.timestamp = datetime.datetime.utcnow()

        await ctx.send(embed=embed)


@bot.command(pass_context=True, aliases=['p', 'pla'])
async def play(ctx, url: str):

    def check_queue():
        Queue_infile = os.path.isdir("./Queue")
        if Queue_infile is True:
            DIR = os.path.abspath(os.path.realpath("Queue"))
            length = len(os.listdir(DIR))
            still_q = length - 1
            try:
                first_file = os.listdir(DIR)[0]
            except:
                print("No more queued song(s)\n")
                queues.clear()
                return
            main_location = os.path.dirname(os.path.realpath(__file__))
            song_path = os.path.abspath(os.path.realpath("Queue") + "\\" + first_file)
            if length != 0:
                print("Song done, playing next queued\n")
                print(f"Songs still in queue: {still_q}")
                song_there = os.path.isfile("song.mp3")
                if song_there:
                    os.remove("song.mp3")
                shutil.move(song_path, main_location)
                for file in os.listdir("./"):
                    if file.endswith(".mp3"):
                        os.rename(file, 'song.mp3')

                voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: check_queue())
                voice.source = discord.PCMVolumeTransformer(voice.source)
                voice.source.volume = 0.07

            else:
                queues.clear()
                return

        else:
            queues.clear()
            print("No songs were queued before the ending of the last song\n")



    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
            queues.clear()
            print("Removed old song file")
    except PermissionError:
        print("Trying to delete song file, but it's being played")
        print("Bot was told to leave voice channel, but was not in one")
        embed = discord.Embed(Error="**Error**", description=("ERROR: Music playing"), color=discord.Color.red())
        embed.set_footer(text='Bot made by Placid#9684')
        embed.timestamp = datetime.datetime.utcnow()

        await ctx.send(embed=embed)
        return


    Queue_infile = os.path.isdir("./Queue")
    try:
        Queue_folder = "./Queue"
        if Queue_infile is True:
            print("Removed old Queue Folder")
            shutil.rmtree(Queue_folder)
    except:
        print("No old Queue folder")

    embed = discord.Embed(Error="**Ready**", description=("Getting everything ready now"), color=discord.Color.red())
    embed.set_footer(text='Bot made by Placid#9684')
    embed.timestamp = datetime.datetime.utcnow()

    await ctx.send(embed=embed)

    voice = get(bot.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            print("Downloading audio now\n")
            ydl.download([url])
    except:
        print("FALLBACK: youtube-dl does not support this URL, using Spotify (This is normal if Spotify URL)")
        c_path = os.path.dirname(os.path.realpath(__file__))
        system("spotdl -f " + '"' + c_path + '"' + " -s " + url)

    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            name = file
            print(f"Renamed File: {file}\n")
            os.rename(file, "song.mp3")

    voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: check_queue())
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.07

    nname = name.rsplit("-", 2)
    embed = discord.Embed(Error="**Play**", description=(f"Playing: {nname[0]}"), color=discord.Color.red())
    embed.set_footer(text='Bot made by Placid#9684')
    embed.timestamp = datetime.datetime.utcnow()

    await ctx.send(embed=embed)
    print("playing\n")


@bot.command(pass_context=True, aliases=['pa', 'pau'])
async def pause(ctx):

    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_playing():
        print("Music paused")
        voice.pause()
        embed = discord.Embed(Error="**Pause**", description=("Music paused"), color=discord.Color.red())
        embed.set_footer(text='Bot made by Placid#9684')
        embed.timestamp = datetime.datetime.utcnow()

        await ctx.send(embed=embed)
    else:
        print("Music not playing failed pause")
        embed = discord.Embed(Error="**Not Playing**", description=("Music not playing failed pause"), color=discord.Color.red())
        embed.set_footer(text='Bot made by Placid#9684')
        embed.timestamp = datetime.datetime.utcnow()

        await ctx.send(embed=embed)


@bot.command(pass_context=True, aliases=['r', 'res'])
async def resume(ctx):

    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_paused():
        print("Resumed music")
        voice.resume()
        print("Music not playing failed pause")
        embed = discord.Embed(Error="**Resumed**", description=("Resumed music"), color=discord.Color.red())
        embed.set_footer(text='Bot made by Placid#9684')
        embed.timestamp = datetime.datetime.utcnow()

        await ctx.send(embed=embed)
    else:
        print("Music is not paused")
        embed = discord.Embed(Error="**Not paused**", description=("Music is not paused"), color=discord.Color.red())
        embed.set_footer(text='Bot made by Placid#9684')
        embed.timestamp = datetime.datetime.utcnow()

        await ctx.send(embed=embed)


@bot.command(pass_context=True, aliases=['s', 'sto'])
async def stop(ctx):
    voice = get(bot.voice_clients, guild=ctx.guild)

    queues.clear()

    queue_infile = os.path.isdir("./Queue")
    if queue_infile is True:
        shutil.rmtree("./Queue")

    if voice and voice.is_playing():
        print("Music stopped")
        voice.stop()
        embed = discord.Embed(Error="**Stopped**", description=("Music stopped"), color=discord.Color.red())
        embed.set_footer(text='Bot made by Placid#9684')
        embed.timestamp = datetime.datetime.utcnow()

        await ctx.send(embed=embed)
    else:
        print("No music playing failed to stop")
        embed = discord.Embed(Error="**Not playing**", description=("No music playing failed to stop"), color=discord.Color.red())
        embed.set_footer(text='Bot made by Placid#9684')
        embed.timestamp = datetime.datetime.utcnow()

        await ctx.send(embed=embed)


queues = {}

@bot.command(pass_context=True, aliases=['q', 'que'])
async def queue(ctx, url: str):
    Queue_infile = os.path.isdir("./Queue")
    if Queue_infile is False:
        os.mkdir("Queue")
    DIR = os.path.abspath(os.path.realpath("Queue"))
    q_num = len(os.listdir(DIR))
    q_num += 1
    add_queue = True
    while add_queue:
        if q_num in queues:
            q_num += 1
        else:
            add_queue = False
            queues[q_num] = q_num

    queue_path = os.path.abspath(os.path.realpath("Queue") + f"\song{q_num}.%(ext)s")

    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
        'outtmpl': queue_path,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            print("Downloading audio now\n")
            ydl.download([url])
    except:
        print("FALLBACK: youtube-dl does not support this URL, using Spotify (This is normal if Spotify URL)")
        q_path = os.path.abspath(os.path.realpath("Queue"))
        system(f"spotdl -ff song{q_num} -f " + '"' + q_path + '"' + " -s " + url)


    embed = discord.Embed(Error="**Adding Song**", description=("Adding song " + str(q_num) + " to the queue"), color=discord.Color.red())
    embed.set_footer(text='Bot made by Placid#9684')
    embed.timestamp = datetime.datetime.utcnow()

    await ctx.send(embed=embed)

    print("Song added to queue\n")


@bot.command(pass_context=True, aliases=['n', 'nex'])
async def next(ctx):
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_playing():
        print("Playing Next Song")
        voice.stop()
        embed = discord.Embed(Error="**Adding Song**", description=("Next Song"), color=discord.Color.red())
        embed.set_footer(text='Bot made by Placid#9684')
        embed.timestamp = datetime.datetime.utcnow()

        await ctx.send(embed=embed)
    else:
        print("No music playing")
        embed = discord.Embed(Error="**No Music**", description=("No music playing failed"), color=discord.Color.red())
        embed.set_footer(text='Bot made by Placid#9684')
        embed.timestamp = datetime.datetime.utcnow()

        await ctx.send(embed=embed)


#Swear filter command
@bot.event
async def on_message(message):
    filter = ["fuck", "nigga", "nigger", "cunt", "corona"]

    for word in filter:
        if message.content.count(word) > 0:
            print('%s has cursed' % (message.author.id))
            await message.channel.purge(limit=1)
    await bot.process_commands(message)

@bot.event
async def convert(ctx, argument):
    argument = await commands.MemberConverter().convert(ctx, argument)
    permission = argument.guild_permissions.manage_messages




#Softban command
@bot.command()
async def softban(ctx, member : discord.Member, *, reason=None):
    if not member:
        return await ctx.send("You must specifiy a user.")

    try:
        await member.ban(reason=None)
        await member.unban()
        embed = discord.Embed(Error="**No Music**", description=f"{member.mention} has been softbanned.", color=discord.Color.red())
        embed.set_footer(text='Bot made by Placid#9684')
        embed.timestamp = datetime.datetime.utcnow()

        await ctx.send(embed=embed)
    except discord.Forbidden:
        return await ctx.send("forbidden")





@bot.command()
async def avatar(ctx, member: discord.Member = None):
    member = ctx.author if not member else member
    embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

    embed.set_author(name=f"Avatar of: {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

    await ctx.send(embed=embed)



























bot.run('NjY2NjgyNjY0MzAzOTg0NjQ2.XmL27A.y-_Bq_4BIDzDAgKxGc9c76j1lmo')
