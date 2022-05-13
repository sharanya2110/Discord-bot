import os
import discord
import requests
import json


client =  discord.Client()

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

  #type '$inspire' and the bot displays an inspirational quote 

  if message.content.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)

client.run(os.getenv('TOKEN'))
  
  



  
  


