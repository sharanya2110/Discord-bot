import os
import discord
import requests
import json
import random


client =  discord.Client()

sad_words = ["sad","depressed","unhappy","angry","miserable","depressing","suffocating"]

starter_encouragements = ["Cheer up!","Hang in there", "You are a great person"]

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  #refer to documentation of api for loading syntax
  json_data = json.loads(response.text)
  # 'q' is the key for quote; 'a' is the key for author as per the api doc
  quote = json_data[0]['q'] + "-" + json_data[0]['a']
  return quote

#register the event
@client.event
async def on_ready():
  #event called when bot is ready to be used
  #0 is replaced with the client
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  #dont do anything if message is from self
  if message.author == client.user:
    return
  #type '$hello' on discord and the bot will reply

  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')

  msg = message.content

  #type '$inspire' and the bot displays an inspirational quote 

  if message.content.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)

  #when bot comes across any words from the sad_words list the bot responds with a random string fromt he starter_encouragements list

  if any(word in msg for word in sad_words):
    await message.channel.send(random.choice(starter_encouragements))

client.run(os.getenv('TOKEN'))
  
  



  
  


