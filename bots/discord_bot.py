import discord
from agents.reputation_agent import ReputationAgent

TOKEN = "YOUR_DISCORD_BOT_TOKEN"

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
rep_agent = ReputationAgent()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if "upload" in message.content.lower():
        rep_agent.update_score(str(message.author), "upload")
        await message.channel.send(f"{message.author} earned points!")

client.run(TOKEN)