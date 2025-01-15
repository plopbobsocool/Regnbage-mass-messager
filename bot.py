import discord
from discord.ext import commands

# Intents setup
intents = discord.Intents.default()
intents.members = True  # Required to fetch members
bot = commands.Bot(command_prefix="!", intents=intents)

# Replace with your bot token
BOT_TOKEN = "MTMyOTA2Mzk5NjY0NDUyODE2OA.G-siZW.nwna3VNuXjf4PRUIiEbx8WduOBYbvaVenN6-pI"

@bot.event
async def on_ready():
    print(f"Bot is logged in as {bot.user}")

@bot.command()
async def message_all(ctx, *, message: str):
    """Command to message all server members"""
    if ctx.author.guild_permissions.administrator:
        members = ctx.guild.members
        for member in members:
            try:
                if not member.bot:  # Skip bot accounts
                    await member.send(message)
                    print(f"Messaged {member.name}")
            except Exception as e:
                print(f"Could not message {member.name}: {e}")
        await ctx.send("Finished messaging all members.")
    else:
        await ctx.send("You do not have permission to use this command.")

bot.run(BOT_TOKEN)
