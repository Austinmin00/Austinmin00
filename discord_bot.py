import discord
import requests
import json
import traceback
import random


client = discord.Client()


sad_words = ["sad" , "depressed" , "unhappy" , "annoyed" , "heartbroken" , "insecure"]


encouragments = ["cheer up" , "hang in there" , "i think you're cool" , "things will get better" , "would you like to play some video games?"]


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    print(response)
    json_data = json.loads(response.text)
    print(json_data)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    print(quote)
    return(quote)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if message.content.startswith('!inspire'):
        try:
            quote = get_quote()
            await message.channel.send(quote)
        except Exception:
            traceback.print_exc()

    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(encouragments))


client.run('ODY2NzkwMDkxNDUxNzkzNDM4.YPXrLQ.HlCJWwQSWTZtXkQtp4r_JEOozk8')
