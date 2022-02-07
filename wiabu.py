from http import client
from pydoc import cli
from urllib.error import HTTPError
import requests, json,discord, os, time, random
from dotenv import load_dotenv
from discord.ext import commands

# load token
load_dotenv('D:\code\discordBots\wiabu\.env')
TOKEN = os.environ.get('wiabuKey') # gets envoriment variable, in my case it is named wiabuKey
if not TOKEN:   # If token is empty(will happen when I deploy on heroku) get the enviroment var from the os
    TOKEN = os.getenv("KEY") # My key name in heroku

# get env var for bot key
def quoteGenerator():
    """ Gets a random qoute from the API and returns a formted f-string that cointains the quote and its details. """
    try:
        r = requests.get("https://animechan.vercel.app/api/random") # Get squote, which is on json format
        r.raise_for_status() # For exception handling 
        requestDictionary = json.loads(r.text) # Convert to python dictionary(now we can easily use it on our code).
        # Bellow the assigned the values the variables to keep the code clean. 
        anime, character, quote = requestDictionary["anime"],requestDictionary["character"],requestDictionary["quote"]
        rString = f'"{quote}" \n-{character}\n{anime}'
    except HTTPError as err:
        rString = err
    return "Something went wrong!\nData for nerds:\n"+rString

bot = discord.ext.commands.Bot(command_prefix='!')
# tow ways of making a bot: discord.Cient or discord.ext.commands.Bot(command_prefix='!')

@bot.command(name="quote")
async def animeQuote(ctx):
        #TODO change the function call quoteGenerator so that this works
        await ctx.send(quoteGenerator())
        
if __name__ == "__main__":
    bot.run(TOKEN)

# random.randrange(1,10)
# time snippet
# now = datetime.now()
# current_time = now.strftime("%H:%M:%S") # 07:41:19
# print("Current Time =", current_time)