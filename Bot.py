#necessary imports
import discord
from discord import app_commands
from discord.ext import commands
import requests

#Intents are a feature of Discord that tells the gateway exactly which events to send your bot.
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

#token
TOKEN = 'Enter-Your-Toker-Here'


#establishing connection.
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

    try:
	#syncs number of commands defined, in this case it will be 7.
        synced = await bot.tree.sync()
        print(f'Synced {len(synced)} command(s)')
    except Exception as e:
        print(e)

#slash commands can be defined by doing so, basic and rudiemntary
@bot.tree.command(name="jok", description="Fetches a random joke")
async def joke(interaction: discord.Interaction):
    await interaction.response.defer()
    response = requests.get('https://v2.jokeapi.dev/joke/Any')
    joke = response.json()
    joke_text = f"**{joke['setup']}**\n{joke['delivery']}"
    await interaction.followup.send(joke_text)

@bot.tree.command(name="pjok", description="Fetches a random joke for you Privately")
async def pjok(interaction: discord.Interaction):
    response = requests.get('https://v2.jokeapi.dev/joke/Any')
    joke = response.json()
    joke_text = f"**{joke['setup']}**\n{joke['delivery']}"
    await interaction.response.send_message(joke_text, ephemeral=True)
    
@bot.tree.command(name="pun", description="Fetches a punny joke")
async def joke(interaction: discord.Interaction):
    await interaction.response.defer()
    response = requests.get('https://v2.jokeapi.dev/joke/Pun')
    joke = response.json()
    joke_text = f"**{joke['setup']}**\n{joke['delivery']}"
    await interaction.followup.send(joke_text)
    
@bot.tree.command(name="ppun", description="Fetches a punny joke for you Privately")
async def pjok(interaction: discord.Interaction):
    response = requests.get('https://v2.jokeapi.dev/joke/Pun')
    joke = response.json()
    joke_text = f"**{joke['setup']}**\n{joke['delivery']}"
    await interaction.response.send_message(joke_text, ephemeral=True)
    
    
@bot.tree.command(name="darkjoke", description="Fetches a dark joke")
async def joke(interaction: discord.Interaction):
    await interaction.response.defer()
    response = requests.get('https://v2.jokeapi.dev/joke/Dark')
    joke = response.json()
    joke_text = f"**{joke['setup']}**\n{joke['delivery']}"
    await interaction.followup.send(joke_text)


@bot.tree.command(name="pdarkjoke", description="Fetches a Dark joke for you Privately")
async def pjok(interaction: discord.Interaction):
    response = requests.get('https://v2.jokeapi.dev/joke/Dark')
    joke = response.json()
    joke_text = f"**{joke['setup']}**\n{joke['delivery']}"
    await interaction.response.send_message(joke_text, ephemeral=True)
    
@bot.tree.command(name="help", description="List of command")
async def help(interaction: discord.Interaction):
    help = "\njok: displays a random joke\n pjok: displays a random joke privately \n pun: displays a punny joke \n ppun: displays a punny joke privately \n darkjoke: displays a dark joke \n pdarkjoke: displays a dark joke privately \n help: Lists all the commands and the description"
    await interaction.response.send_message(help,ephemeral=True)
	
    
bot.run(TOKEN)
