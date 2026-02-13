import os
from telegram import Bot

TOKEN = os.getenv("BOT_TOKEN")
GROUP_ID = os.getenv("GROUP_ID")

bot = Bot(token=TOKEN)

bot.send_message(chat_id=GROUP_ID, text="✅ Bot is running on Render!")
