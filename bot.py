import discord
from discord.ext import commands
from discord.ui import View, Button

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="/", intents=intents)


@bot.event
async def on_ready():
    print(f"{bot.user} is now running!")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)


@bot.tree.command(name="veto-create")
async def hello(interaction: discord.Interaction):
    embed = discord.Embed(
        title="Veto BOT",
        description="Tutaj będziesz mieć możliwość przeprowadzenia veto map",
        color=0x0099FF,
    )
    embed.set_author(
        name="Veto BOT",
        icon_url="https://i.imgur.com/AfFp7pu.png",
        url="https://discord.js.org",
    )

    button1 = Button(label="Button 1", style=discord.ButtonStyle.secondary)
    button2 = Button(label="Button 2", style=discord.ButtonStyle.secondary)

    view = View()
    view.add_item(button1)
    view.add_item(button2)

    message = await interaction.response.send_message(embed=embed, ephemeral=True, view=view)

    @bot.event
    async def on_button_click(interaction: discord.Interaction):
        try:
            if interaction.custom_id == "button1":
                await interaction.message.edit(embed=discord.Embed(title="Button 1 Clicked", color=0x0099FF))
            elif interaction.custom_id == "button2":
                await interaction.message.edit(embed=discord.Embed(title="Button 2 Clicked", color=0x0099FF))
        except discord.NotFound:
            # Obsługa błędu w przypadku, gdy wiadomość nie została znaleziona
            print("Wiadomość nie została znaleziona.")

    # Przypisanie obsługi zdarzeń przycisków do bota
    bot.add_listener(on_button_click, "on_button_click")


def run_discord_bot():
    with open("config.txt", "r") as file:
        token = file.read().strip()

    bot.run(token)
