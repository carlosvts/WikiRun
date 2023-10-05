import os

from dotenv import load_dotenv
from interactions import Client, Intents, SlashContext, listen, slash_command

load_dotenv()

bot = Client(intents=Intents.DEFAULT)


@listen()
async def on_ready():
    print("Bot is ready")


# running the bot
bot.start(os.getenv('BOT-TOKEN'))
