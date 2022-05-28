import discord
import os
from keep_alive import keep_alive
client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$echo'):
    msg = message.content
    print(msg)
    finalmsg = msg.replace('$echo','')
    print(finalmsg)
    await message.channel.send(finalmsg)

keep_alive()
#client.run(os.getenv('TOKEN'))
client.run('OTc5Nzk3MDUwMjU2NDAwNDQ0.GEv0Af.Jo1Lg5OXElTn54cXBeJhIkCLIJzGwTHjsqLjgw')