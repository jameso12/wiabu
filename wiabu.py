from http import client
from pydoc import cli
import requests, json,discord, os, time, random
from dotenv import load_dotenv

# load token
load_dotenv('D:\code\discordBots\wiabu\.env')
TOKEN = os.environ.get('wiabuKey')


# get env var for bot key
def quoteGenerator():
    r = requests.get("https://animechan.vercel.app/api/random")
    requestDictionary = json.loads(r.text)
    print(requestDictionary)
    anime, character, qoute = requestDictionary["anime"],requestDictionary["character"],requestDictionary["quote"]
    
    return f'"{qoute}" \n-{character}\n{anime}'

client = discord.Client()

@client.event
async def on_message(message):
    await message.channel.send(quoteGenerator())

client.run(TOKEN)

# random.randrange(1,10)
# time snippet
# now = datetime.now()
# current_time = now.strftime("%H:%M:%S") # 07:41:19
# print("Current Time =", current_time)