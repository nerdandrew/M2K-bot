import discord
import asyncio
import re


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

client.run('bot id here')
