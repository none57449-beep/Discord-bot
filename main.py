import discord
import os

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Бот запущен как {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower() == "привет":
        await message.channel.send("Привет! Я работаю 24/7 через Railway 🚀")

token = os.getenv("TOKEN")
client.run(token)
