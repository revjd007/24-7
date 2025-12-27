import discord
from discord.ext import commands
import asyncio

TOKEN = "MTQzNjQzODMwNDM2MjA3MDEzNw.G_EK16.RsULYOB6CRAo-5Mc4Dlx4QkmXIqZxfkLey1T0E"
ROLE_NAME = "MEMBER"  # role to give everyone

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

    for guild in bot.guilds:
        role = discord.utils.get(guild.roles, name=ROLE_NAME)
        if not role:
            print(f"Role not found in {guild.name}")
            continue

        print(f"Checking members in {guild.name}...")

        for member in guild.members:
            if role not in member.roles:
                try:
                    await member.add_roles(role)
                    print(f"Gave role to {member.name}")
                    await asyncio.sleep(0.5)  # prevents rate limits
                except Exception as e:
                    print(f"Failed for {member.name}: {e}")

@bot.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name=ROLE_NAME)
    if role:
        try:
            await member.add_roles(role)
            print(f"Auto-role given to {member.name}")
        except Exception as e:
            print(f"Failed to give role: {e}")

bot.run(TOKEN)
