import discord
import asyncio
import random

# Bot Configuration
TOKEN = 'MTIzNzg0Mzg3OTE0MzgwMDkzMg.GhO9iT.DzuErqaN8QUK_lW5Qh0aPcy_x4vCFB3WlIor_Q'  # Your bot's token
GUILD_ID = 949369997040422952  # Your guild's ID
CHANNEL_ID = 949369997707337790  # Your channel's ID where messages should be sent
USER_ID = 717080796850159738  # User ID you want to ping

# Define intents
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True

# List of random messages
messages = [
    "I told my wife she was drawing her eyebrows too high. She looked surprised.",
    "I threw a boomerang a few years ago. I now live in constant fear.",
    "My boss told me to have a good day. So I went home!",
    "Why do we tell actors to 'break a leg?' Because every play has a cast.",
    "Helvetica and Times New Roman walk into a bar. 'Get out of here!' shouts the bartender. 'We don't serve your type.'",
    "Yesterday I saw a guy spill all his Scrabble letters on the road. I asked him, 'What’s the word on the street?'",
    "Having a smoking section in a restaurant is like having a peeing section in a swimming pool.",
    "My dog used to chase people on a bike a lot. It got so bad I had to take his bike away.",
    "I'm on a whiskey diet. I've lost three days already.",
    "The man who survived mustard gas and pepper spray is now a seasoned veteran.",
    "I'm reading a book on the history of glue – can’t put it down.",
    "I wasn't originally going to get a brain transplant, but then I changed my mind.",
    "Why don't skeletons fight each other? They don't have the guts.",
    "I used to play piano by ear, but now I use my hands.",
    "Why don’t scientists trust atoms? Because they make up everything.",
    "I'd tell you a construction joke, but I'm still working on it.",
    "I used to be a baker, but I couldn't make enough dough.",
    "What do you get when you cross a snowman and a vampire? Frostbite.",
    "I told my computer I needed a break, and now it won’t stop sending me Kit-Kat ads.",
    "I’m only familiar with 25 letters in the English language. I don’t know why.",
    "I asked the librarian if the library had books on paranoia. She whispered, 'They're right behind you...'",
    "Why was the math book sad? It had too many problems.",
    "What do you call fake spaghetti? An impasta!",
    "I would avoid the sushi if I were you. It’s a little fishy.",
    "Why don’t oysters donate to charity? Because they are shellfish."
]

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    guild = discord.utils.get(client.guilds, id=GUILD_ID)
    if guild:
        channel = guild.get_channel(CHANNEL_ID)
        if channel:
            print(f"Bot is active in the channel: {channel.name}")
            target_user = f'<@{USER_ID}>'  # Formats the mention correctly
            while True:
                random_message = random.choice(messages)
                await channel.send(f'{target_user} {random_message} - Nick Leshay')
                await asyncio.sleep(30)  # Sends a message every 30 seconds
        else:
            print("Channel not found!")
    else:
        print("Guild not found!")

client.run(TOKEN)
