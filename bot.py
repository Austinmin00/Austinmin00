import discord
import requests
import json
import traceback
import random


client = discord.Client()

bad_word = ["lesbian" , "Lesbian" , "lesbians" , "Lesbians" , "lesbo" , "Lesbo" , "lesbianz" , "Lesbianz"]

bad_response = ["Who you calling a lesbian" , "We are all lesbians" , "Look whos talking" , "Im just a bot lol" , ""]

sad_words = ["sad" , "depressed" , "unhappy" , "annoyed" , "heartbroken" , "insecure"]

encouragments = ["cheer up" , "hang in there" , "i think you're cool" , "things will get better" , "would you like to play some video games?"]

# @client.command()
# async def ping(ctx):
#     await ctx.send(f'Pong! {round(client.latency * 1000)}ms')
#
# @client.command(aliases=["8ball", "test"])
# async def _8ball(ctx, *, question):
#     responses = ["it is certain"
#         "it is decidely so"
#         "without a doubt"
#         "yes, definitely"
#         "you may rely on it"
#         "as i see it, yes"
#         "most likely"
#         "outlook good"
#         "yes"
#         "signs point to yes"
#         "reply hazy, try again"
#         "ask again later"
#         "better not tell you now"
#         "cannot predict now"
#         "concentrate and ask again"
#         "dont count on it"
#         "my reply is no"
#         "my source says no"
#         "outlook not so good"
#         "very doubtful"]
#
#     await ctx.send(f"Question: {question}\nAnswer: {random.choice(responses)}")

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

    if any(word in msg for word in bad_word):
        await message.channel.send(random.choice(bad_response))









client.run('ODY2NzkwMDkxNDUxNzkzNDM4.YPXrLQ.HlCJWwQSWTZtXkQtp4r_JEOozk8')
