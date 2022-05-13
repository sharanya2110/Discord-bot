import os
import discord

client =  discord.Client()

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

  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')

client.run(os.getenv('TOKEN'))
  
  



  
  


