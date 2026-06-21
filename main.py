import discord
import os

# Токен берётся из Railway Variables
token = os.getenv("DISCORD_TOKEN")

if not token:
    print("❌ DISCORD_TOKEN не найден")
    exit()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"✅ Бот запущен как {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower() == "привет":
        await message.channel.send("Привет! Я работаю 24/7 🚀")

client.run(token)
