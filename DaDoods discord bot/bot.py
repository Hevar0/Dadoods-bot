import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix="e ")

@client.event
async def on_ready():
    print("DaDadoods bot is online!")

@client.command()
async def ping(ctx):
    await ctx.send(f"pong! ({round(client.latency * 1000)}ms)")

@client.command()
async def pong(ctx):
    await ctx.send(f"ping! ({round(client.latency * 1000)}ms)")

@client.command()
async def rick(ctx):
        await ctx.send("https://www.youtube.com/watch?v=ukaa9sXbTfw")

@client.command()
async def dadoods(ctx):
    await ctx.send("https://www.youtube.com/channel/UC16Q4ATvXHnkb93UjS-TqDQ")

@client.command()
async def wreckroll(ctx):
    await ctx.send("https://www.youtube.com/watch?v=xQNw8BBxRIs")
    
@client.command()
async def beg(ctx):
    await ctx.send("im more broke than you")

@client.command()
async def ih(ctx):
    await ctx.send("ih, how is u does?")

@client.command()
async def e(ctx):
    await ctx.send("ee")

@client.command()
async def ee(ctx):
    await ctx.send("eee")

@client.command()
async def eee(ctx):
    await ctx.send("eeee")

@client.command()
async def game(ctx):
    await ctx.send("reblex yas")

@client.command(aliases=["8ball", "test"])
async def askquestion(ctx, *, question):
    responses = ["It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes - definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful.",
	        "Don't rely on it"]
    await ctx.send(f"Question: {question} \nAnswer: {random.choice(responses)}")

@client.command()
async def shop(ctx):
    embed=discord.Embed(title="Shop", description="A place where you buy things. We currently only sell DaDoods smoothies", color=0x27b973)
    embed.set_author(name="Shop")
    embed.add_field(name="DaDoods smoothie", value="Costs 5 coins. One of the best, and finest smoothies out there in the world", inline=True)
    await ctx.send(embed=embed)
@client.command()
async def yeti(ctx):
    await ctx.send(f"@{ctx.message.author}")


client.run("bot_token")


