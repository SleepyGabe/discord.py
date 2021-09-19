# bot.py
import os
import random, os, requests, discord
import random
#from dotenv import load_dotenv

def Generate_Code(): #function generates a random 6 digit number
    code = ''
    for i in range(6):
        code += str(random.randint(0,9))
    return code

def valid_url(): #function checks whether a doujin exists with the generated code
    valid = False

    while valid == False:
        url = 'https://nhentai.net/g/'+Generate_Code()+'/'
        r = requests.get(url)
        if r.status_code != 404:
            valid = True
    return url


#load_dotenv()
TOKEN = 'ODg4NDM1NTY5NjM2NTY1MDIy.YUSqGg.gpW33DZzDjszUsFVIlODsRBNOD8'

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return


    if message.content == '_imhorny':
        response = valid_url()
        await message.channel.send(response)
client.run(TOKEN)