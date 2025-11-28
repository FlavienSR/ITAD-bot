import discord
from discord.ext import commands
from discord import app_commands
from utils.game_info import game_info,game_price

PERSO = 1098342509324800000
ROOTFARM = 1288930612048166962

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="ping", description="Pour test le bot + latence")
    @app_commands.guilds(discord.Object(id=PERSO),discord.Object(id=ROOTFARM))
    async def ping(self, interaction: discord.Interaction):
        latency_ms = round(interaction.client.latency * 1000)
        await interaction.response.send_message(f"Pong ! {latency_ms} ms")

    @app_commands.command(name="gameinfo", description="Avoir la description d'un jeu")
    @app_commands.guilds(discord.Object(id=PERSO),discord.Object(id=ROOTFARM))
    async def gameinfo(self, interaction: discord.Interaction, game: str):
        jeu = game_info(game)
        boxart_url = jeu["assets"].get("boxart")
        embed_info = discord.Embed(
                title = jeu["title"],
                color = discord.Color.green()
                )
        if boxart_url:
            embed_info.set_image(url=boxart_url)
        else:
            embed_info.set_footer(text="No boxart available")
        embed_info.add_field(name="Developpeurs", value=jeu["developers"][0]["name"])
        embed_info.add_field(name="Date de sortie", value=jeu["releaseDate"])
        embed_info.add_field(name="URL", value=f"[View on ITAD]({jeu['urls']['game']})")
        prix = game_price(game)
        embed_prix = discord.Embed(
                title = "Offres",
                color = discord.Color.green()
                )
        for shop in prix:
            for deal in shop["deals"]:
                boutique = deal["shop"]["name"]
                valeur = deal["price"]["amount"]
                devise = deal["price"]["currency"]
                url = deal["url"]
                embed_prix.add_field(name="", value=f"[{boutique} - {valeur} {devise}]({url})")
        await interaction.response.send_message(embeds=[embed_info, embed_prix])

async def setup(bot):
    await bot.add_cog(Info(bot))
