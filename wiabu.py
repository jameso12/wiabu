from http import client
from pydoc import cli
import requests, json,discord, os, time, random
from dotenv import load_dotenv
from discord.ext import commands

# load token
load_dotenv('D:\code\discordBots\wiabu\.env')
TOKEN = os.environ.get('wiabuKey')
if not TOKEN:
    TOKEN = os.getenv("KEY")

# get env var for bot key
def quoteGenerator():
    r = requests.get("https://animechan.vercel.app/api/random")
    requestDictionary = json.loads(r.text)
    print(requestDictionary)
    anime, character, qoute = requestDictionary["anime"],requestDictionary["character"],requestDictionary["quote"]
    
    return f'"{qoute}" \n-{character}\n{anime}'

bot = discord.ext.commands.Bot(command_prefix='!')
# tow ways of making a bot: discord.Cient or discord.ext.commands.Bot(command_prefix='!')

@bot.command(name="quote")
async def animeQuote(ctx):
        await ctx.send(quoteGenerator())

bot.run(TOKEN)

# random.randrange(1,10)
# time snippet
# now = datetime.now()
# current_time = now.strftime("%H:%M:%S") # 07:41:19
# print("Current Time =", current_time)