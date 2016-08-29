import discord
import asyncio
import re
import urllib.request
from PIL import Image
import requests
import io

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in')

async def notfound(msg,cmd):
    '''when the "define" is given something that isn't in the database'''
    await client.send_message(msg.channel,'Sorry, I didn\'t find '+cmd+' in my database. \
If you would like it added, please PM my creator (<@162627499497488384>) about it \
or submit it through the form (https://goo.gl/forms/lvMzTKFihA7bMiCk1) and \
he\'ll get to it as soon as he can')
    
async def EOM(msg):
    '''end of message. it's just done as a closing thing to each sentence'''

    await client.send_message(msg.channel,'If you found anything wrong with this \
definition or would like to add to it, please PM my creator (<@162627499497488384>) about \
the definition and he\'ll get to it as soon as he can.')








###Commands########################################################################################

async def wavedash(msg):
    await client.send_message(msg.channel,'')
    await EOM(msg)

async def shitpost(msg):
    await client.send_message(msg.channel,'To make shitty posts on an internet messageboard\n\
example: https://i.imgur.com/y8bdpgR.jpg')
    await EOM(msg)
    
async def shitposting(msg):
    '''links to shitpost()'''
    await shitpost(msg)
async def shitposts(msg):
    '''links to shitpost()'''
    await shitpost(msg)
async def taunt(msg):
    await client.send_message(msg.channel,'A move intentionally designed to provoke, annoy, \
disrespect, or mock opponents. It can be performed by pressing d-pad up. While taunts can \
sometimes be used to please the crowd and therefore provide a moral boost to the one taunting, \
some taunts are not well used and will have the opposite effect (see: SFAT)\n\
More info: http://www.ssbwiki.com/Taunt \n\
Example: http://www.ssbwiki.com/images/9/93/CaptainFalcon-Right-Taunt-SSBM.gif')
    await EOM(msg)


with open('articles/list of terms.txt') as f:
    listofterms = f.readlines()
###################################################################################################

@client.event
async def on_message(message):
    global listoftech
    if message.content.startswith('!define '.lower()):
        command = re.sub('!define ','',message.content)       
        try:
            listofterms.index(command)
            if command in ['taunts','taunting']:
                command = 'taunt'
            elif command in ['shitposting','shitposts','shit post','shit posting']:
                command = 'shitpost'
            elif command in ['wavedashing','wave dash','wave dashing']:
                command = 'wavedash'
            tempf = open('articles/'+command+'.txt','r+')
            await client.send_message(message.channel,tempf.read())
        except ValueError:
            await notfound(message,command)
    elif message.content.startswith('!shitpost'):
        await client.send_message(message.channel,'*LOUDLY SHITPOSTS*')
client.run('MjE5Mjc4MDIxMjkzNTA2NTc0.CqPaIg.tBEh-iArAI7dcn9w1y9uE7ge4uw')
