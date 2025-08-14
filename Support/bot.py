import os
import discord
from discord.ext import commands

OWNER_ID = 1282714989223743581  # Replace with your Discord User ID

intents = discord.Intents.default()
intents.messages = True
intents.dm_messages = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user} (ID: {bot.user.id})")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if isinstance(message.channel, discord.DMChannel):
        owner = await bot.fetch_user(OWNER_ID)
        user_info = f"📩 User who DMed me: {message.author} (ID: {message.author.id})"
        try:
            await owner.send(user_info)
            print(f"Sent DM to owner: {user_info}")
        except discord.Forbidden:
            print("❌ Could not DM owner — DMs might be disabled or no mutual server.")

    await bot.process_commands(message)

bot.run(os.getenv("BOT_TOKEN"))