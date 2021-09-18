import discord
import os
from datetime import datetime
import json
import requests
import randfacts
import pyjokes

client=discord.Client()

def get_quote():
  response = requests.get('https://zenquotes.io/api/random')
  json_data= json.loads(response.text)
  quote=json_data[0]['q'] + " -" + json_data[0]['a']
  return (quote)



@client.event
async def on_ready():
  print('we have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
 if message.author==client.user:
   return

 if message.content.startswith('$hello'):
   await message.channel.send('Hello!')
 
 if message.content.startswith('$motivate me'):
   quote=get_quote()
   await message.channel.send(quote)

 if message.content.startswith('$fact'):
   fact=randfacts.get_fact()
   await message.channel.send(fact)
 
 if message.content.startswith('$jokes'):
   jokes=pyjokes.get_joke(language='en',category='all')
   await message.channel.send(jokes)
 
 new_message = datetime.now()
 currentTime = new_message.strftime("%H:%M:%S")
 if message.content.startswith('$time'):
   await message.channel.send(f"Time{currentTime}")





client.run('Nzk2MzkyNzY1NDc0NzM0MDkw.X_XQjw.chCjXe0uJozQgoGwW0MB50jZ_74')




