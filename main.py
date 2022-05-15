import os
import discord
import requests
import json
import random
from replit import db


client =  discord.Client()

sad_words = ["sad","depressed","unhappy","angry","miserable","depressing","suffocating"]

starter_encouragements = ["Cheer up!","Hang in there", "You are a great person"]

if "responding" not in db.keys():
  db["responding"] = True
  

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  #refer to documentation of api for loading syntax
  json_data = json.loads(response.text)
  # 'q' is the key for quote; 'a' is the key for author as per the api doc
  quote = json_data[0]['q'] + "-" + json_data[0]['a']
  return quote

#add encouragements
def update_encouragements(encouraging_message):
  if "encouragements" in db.keys():
    encouragements = db["encouragements"]
    encouragements.append(encouraging_message)
    db["encouragements"] = encouragements
  else:
    db["encouragements"] = [encouraging_message]

#delete encouragements
def delete_encouragement(index):
  encouragements = db["encouragements"]
  if len(encouragements) > index:
    del encouragements[index]
    #save into the database again
    db["encouragements"] = encouragements
    
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

  if db["responding"]:
    options = starter_encouragements
    if "encouragements" in db.keys():
      options = options + list(db["encouragements"])
  
    if any(word in msg for word in sad_words):
      await message.channel.send(random.choice(options))

  if msg.startswith("$new"):
    encouraging_message = msg.split("$new ", 1)[1]
    update_encouragements(encouraging_message)
    await message.channel.send("New encouraging message added.")

  if msg.startswith("$del"):
    encouragements = []
    if "encouragements" in db.keys():
      index = int(msg.split("$del ", 1)[1])
      delete_encouragement(index)
      encouragements = db["encouragements"]
    await message.channel.send(encouragements)

  if msg.startswith("$list"):
    encouragements = []
    if "encouragements" in db.keys():
      encouragements = db["encouragements"]
    await message.channel.send(encouragements)

  if msg.startswith("$responding"):
    value = msg.split("$responding ",1)[1]

    if value.lower() == "true":
      db["responding"] = True
      await message.channel.send("Responding is on.")
    else:
      db["responding"] = False
      await message.channel.send("Responding is off.")

client.run(os.getenv('TOKEN'))
  
  



  
  


