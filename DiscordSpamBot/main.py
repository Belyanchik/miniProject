import discord
from discord.ext import commands
import asyncio

PREFIX = "!"

client = commands.Bot(command_prefix = PREFIX)
client.remove_command("help")

DSTOKEN = ""    #Your Discord Bot Token

spam = False    #Variable for spam status

@client.event
async def on_ready():
    print("The bot was connected to the server under the tag {0.user}!".format(client))


@client.command()
@commands.is_owner()    #We limit the possibility of using
async def spam(ctx, member: discord.Member, repeats = 60):      #Spam in the current channel
    global spam
    spam = True
    for i in range(repeats):
        if(spam == False):
            break
        else:
            await ctx.send(f"{member.mention}, hi")
            await asyncio.sleep(1)
    spam = False

@spam.error
async def spam_error(ctx, error):   #Dealing with spam errors in the channel
    if isinstance (error, commands.MissingRequiredArgument):
        emb = discord.Embed(title = "Missing mention!", color = 0xff0505)
        await ctx.send(embed = emb)
    if isinstance (error, commands.NotOwner):
        emb = discord.Embed(title = "You need to be a Belyanchik to use this command", color = 0xff0505)
        await ctx.send(embed = emb)
    if isinstance (error, commands.BadArgument):
        emb = discord.Embed(title = "The entered argument is incorrect", color = 0xff0505)
        await ctx.send(embed = emb)


@client.command()
@commands.is_owner()    #We limit the possibility of using
async def pspam(ctx, member: discord.Member, repeats = 60):     #Spam in private messages
    global spam
    spam = True
    for i in range(repeats):
        if(spam == False):
            break
        else:
            await member.send(f"{member.mention}, hi")
            await asyncio.sleep(1)
    spam = False

@pspam.error
async def pspam_error(ctx, error):      #Dealing with spam errors in private messages
    if isinstance (error, commands.MissingRequiredArgument):
        emb = discord.Embed(title = "Missing mention!", color = 0xff0505)
        await ctx.send(embed = emb)
    if isinstance (error, commands.NotOwner):
        emb = discord.Embed(title = "You need to be a Belyanchik to use this command", color = 0xff0505)
        await ctx.send(embed = emb)
    if isinstance (error, commands.BadArgument):
        emb = discord.Embed(title = "The entered argument is incorrect", color = 0xff0505)
        await ctx.send(embed = emb)


@client.command()
@commands.is_owner()    #We limit the possibility of using
async def aspam(ctx, member: discord.Member, repeats = 60):     #Spam in the selected channel and in private messages
    global spam
    spam = True
    for i in range(repeats):
        if(spam == False):
            break
        else:
            await ctx.send(f"{member.mention}, hi")
            await member.send(f"{member.mention}, hi")
            await asyncio.sleep(1)
    spam = False

@aspam.error
async def aspam_error(ctx, error):      #Dealing with spam errors in the selected channel and in private messages
    if isinstance (error, commands.MissingRequiredArgument):
        emb = discord.Embed(title = "Missing mention!", color = 0xff0505)
        await ctx.send(embed = emb)
    if isinstance (error, commands.NotOwner):
        emb = discord.Embed(title = "You need to be a Belyanchik to use this command", color = 0xff0505)
        await ctx.send(embed = emb)
    if isinstance (error, commands.BadArgument):
        emb = discord.Embed(title = "The entered argument is incorrect", color = 0xff0505)
        await ctx.send(embed = emb)


@client.command()
@commands.is_owner()    #We limit the possibility of using
async def sspam(ctx):   #Stopping Spam
    global spam
    spam = False

@sspam.error
async def sspam_error(ctx, error):      #Dealing with Spam Stop Errors
    if isinstance (error, commands.NotOwner):
        emb = discord.Embed(title = "You need to be a Belyanchik to use this command", color = 0xff0505)
        await ctx.send(embed = emb)


@client.command()
async def help(ctx):    #Message with commands
    emb = discord.Embed(title = "Help for spam bot", color = 0xde2f60)
    emb.add_field(name = "{}spam".format(PREFIX), value = "Spam in the current channel")
    emb.add_field(name = "{}pspam".format(PREFIX), value = "Spam in private messages")
    emb.add_field(name = "{}aspam".format(PREFIX), value = "Spam in the current channel and in private messages")
    emb.add_field(name = "{}sspam".format(PREFIX), value = "Stop Spam")
    emb.add_field(name = "Open source", value = "[GitHub project](https://github.com/Belyanchik)")
    await ctx.send(embed = emb)


client.run(DSTOKEN)
