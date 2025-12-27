import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

TOP1_ROLE_ID = 123456789012345678  # ID do cargo Top 1
CHANNEL_ID = 123456789012345678   # ID do canal de anúncio

@bot.event
async def on_ready():
    print(f"Bot online como {bot.user}")

@bot.event
async def on_member_update(before, after):
    role = after.guild.get_role(TOP1_ROLE_ID)
    channel = after.guild.get_channel(CHANNEL_ID)

    if role is None or channel is None:
        return

    # Se o usuário ganhou o cargo Top 1
    if role not in before.roles and role in after.roles:
        await channel.send(
            f"👑 **{after.mention} alcançou o TOP 1 DO SERVIDOR!** 👑\n"
            "Agora ocupa a posição mais alta do ranking.\n\n"
            "_Essa conquista pertence a poucos._\n"
            "_Manter o trono… é ainda mais difícil._"
        )

bot.run(os.getenv("DISCORD_TOKEN"))
