import discord
from discord.ext import commands
from discord.ui import View, Button

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="/", intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user} is now running!')
    try:
        synced = await bot.tree.sync()
        print(f'Synced {len(synced)} command(s)')
    except Exception as e:
        print(e)


@bot.tree.command(name="veto-create")
async def hello(interaction: discord.Interaction):
    embed = discord.Embed(title="Veto BOT", description="Tutaj będziesz mieć możliwość przeprowadzenia veto map", color=0x0099FF)
    embed.set_author(name="Veto BOT", icon_url="https://i.imgur.com/AfFp7pu.png", url="https://discord.js.org")
    await interaction.response.send_message(embed=embed, ephemeral=True)

with open('config.txt', 'r') as file:
    token = file.read().strip()

bot.run(token)
