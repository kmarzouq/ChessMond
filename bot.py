
class pbord:
    def __init__(self,pq,r,c,p):
        self.pq = pq # piece
        self.r = r #row
        self.c = c #column
        self.p = p # which player 1 is White, 2 is Black, # 0 is nothing

from board import *
import numpy as np
import math
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix='$', intents=intents)

#def readboard ():

global c 
c = False


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message: discord.Message):
    chan = message.channel #finds channel of message
    print(chan)
    chann = chan.id
    print(chann)
    m = discord.utils.get(message.guild.text_channels, name=chan)
    print (m)
    m2 = await m.history(limit=10)
    m3 = m2.flatten()
    print (m3)
    board=[]
    global c
    if message.author == client.user:
        return
    
    if message.content.startswith('$hello'):
        men = "__Hello!" + message.author.mention + "\n" + client.user.mention + "__" 
        await message.channel.send(men)

    if message.content.startswith('$help'):
        await message.channel.send("to move piece, type \" $move *board location* to *board location* \" \nEX: $move G8 to H6")
        await message.channel.send("to castle, just say \"$castle\"")

    if message.content.startswith('$start'):
        if (message.mentions==None):
            await message.channel.send("Please @ you are challenging")
        else:
            challenged = message.mentions[0]
            resp = challenged.mention + "Do you accept a match with " + message.author.mention + " ?:"
            await message.channel.send( resp)
            c=True
            print(c)
    

    if message.content.startswith('$yes' or '$y') and c:
        challenger = message.author #change
        makeBoard(board)
        newBoard(board)
        boardstr=printboard(board)
        boardstr= client.user.mention + "\nWhite: " + message.author.mention + "\n" + "Black:" + challenger.mention + "\n" + boardstr
        await message.channel.send(boardstr)
        c = False
        print(c)
    if message.content.startswith('$no' or '$n') and c:
        resp = message.author.mention + "said no"
        await message.channel.send(resp)
        c=False
        print(c)

    if message.content.startswith('$board'):
        boardstr=printboard(board)
        await message.channel.send(boardstr)
    

client.run('MTA4MzQ5NzUzMDgzMjE5OTczMA.GieV3F.Gorz6-9DTL30TJ-Ef20fRie7p5Ig6Mp4GV--Mo')
