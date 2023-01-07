import os
import discord
from discord.ext import commands
from discord import client
from dotenv import load_dotenv

intents = discord.Intents.default
intents.members= True

client = commands.Bot(command_prefix="!", intents=intents)

load_dotenv()
TOKEN = os.getenv('OTg4NjcwODM2NzI4NzkxMDQw.GUlfKI.Lt_oN_ZIC1VKomqk0S_xkvQ-dcoDXR9B4lP3ug')

bot = commands.bot(command_prefix='!')

@bot.command(name='Which Party Pack?')
async def Party_Packs(ctx):
    JackboxNames = [
        "THE JACKBOX PARTY PACK 9",
        "JACKBOX PARTY STARTER",
        "THE JACKBOX PARTY PACK 8",
        "THE JACKBOX PARTY PACK 7",
        "THE JACKBOX PARTY PACK 6",
        "THE JACKBOX PARTY PACK 5",
        "THE JACKBOX PARTY PACK 4",
        "THE JACKBOX PARTY PACK 3",
        "THE JACKBOX PARTY PACK 2",
        "THE JACKBOX PARTY PACK",
    ]

    response = random.choice(JackboxNames)
    await ctx.send(response)

@bot.command(name="Which game from Jackbox Party Pack 9?")
async def JBGames(ctx):
    Jackbox9 = [
        "Fibbage 4 (2-8 players)",
        "Nonsensory (1-10 players)",
        "Quixort",
        "Junktopia",
        "Roomerang",
    ]
    response = random.choice(Jackbox9)
    await ctx.send(response)

@bot.command(name="Which game from Jackbox Party Starter?")
async def JBPS(ctx):
    JackboxPartyStarter = [
        "Quiplash 3",
        "Tee K.O",
        "Trivia Murder Party 2"
    ]
    response = random.choice(JackboxPartyStarter)
    await ctx.send(response)

@bot.command(name="Which game from Jackbox Party Pack 8?")
async def JBPP8(ctx):
    PartyPackEight =[
        "Drawful Animate",
        "Job Job",
        "The Wheel of Enormous Proportions",
        "Poll Mine",
        "Weapons Drawn"
    ]
    response = random.choice(PartyPackEight)
    await ctx.send(response)

@bot.command(name="Which game from Jackbox Party Pack 7?")
async def JBPP7(ctx):
    PartyPackSeven = [
        "Quiplash 3 (3-8 Players)",
        "The Devils and the Details (3-8 Players)",
        "Champ'd up (3-8 Players)",
        "Talking Points (3-8 Players)",
        "Blather 'Round (2-6 Players",
    ]
    response = random.choice(PartyPackSeven)
    await ctx.send(response)

@bot.command(name="Which game from Jackbox Party Pack 6?")
async def JBPP6(ctx):
    PartyPackSix = [
        "Trivia Murder Party 2 (1-8 Players)",
        "Role Models (3-6 Players)",
        "Joke Boat (3-8 Players)",
        "Dictionarium (3-8 Players)",
        "Push The Button (4-10 Players)"
    ]
    response = random.choice(PartyPackSix)
    await ctx.send(response)

@bot.command(name="Which game from Jackbox Party Pack 5?")
async def JBPP5(ctx):
    PartyPackFive = [
       "YOU DON’T KNOW JACK: Full Stream (1-8 players)",
       "Split the Room (3-8 Players)",
       "Mad Verse City (3-8 players)",
       "Patently Stupid (3-8 players)",
       "Crab Nebula, Zeeple Dome (1-6 players)",
    ]
    response = random.choice(PartyPackFive)
    await ctx.send(response)

@bot.command(name="Which game from Jackbox Party Pack 4?")
async def JBPP4(ctx):
    PartyPackFour = [
        "Fibbage 3 (2-8 Players)",
        "Survive the Internet (3-8 Players)",
        "Monster Seeking Monster (3-7 Players)",
        "Bracketeering (3-16 Players)",
        "Civic Doodle (3-8 Players)",
    ]
    response = random.choice(PartyPackFour)
    await ctx.send(response)

@bot.command(name="Which game from Jackbox Party Pack 3?")
async def JBPP3(ctx):
    PartyPackThree = [
        "Quiplash 2 (3-8 Players)",
        "Trivia Murder Party (",
        "Guesspionage (",
        "Tee K.O",
        "Fakin It"
    ]
    response = random.choice(PartyPackThree)
    await ctx.send(response)

@bot.command(name="Which game from Jackbox Party Pack 2?")
async def JBPP2(ctx):
    PartyPackTwo = [
    "Fibbage 2 (2-8 Players)",
    "Earwax (3-8 Players)",
    "Bidiots (3-6 Players)",
    "Quiplash XL (3-8 Players)",
    "Bomb Corp (1-4 Players)"
    ]
    response = random.choice(PartyPackTwo)
    await ctx.send(response)

@bot.command(name="Which game from The Jackbox Party Pack")
async def JBPP(ctx):
    PartyPack = [
    "You Don't Know Jack 2015(1-4 Players)",
    "Fibbage XL (2-8 Players)",
    "Drawful (3-8 Players)",
    "Word Spud (2-8 Players)",
    "Lie Swatter (1-100 Players)",
    ]
    response = random.choice(PartyPack)
    await ctx.send(response)


 





























bot.run('')