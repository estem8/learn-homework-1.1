from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, CommandHandler

import requests
import json
from setting import BOT_TOKEN

WEBHOOK_URL = 'http://127.0.0.1:5000/'

async def start(update, context):
    await update.message.reply_text("Enter city")

async def handle_city(update, context):
    city = update.message.text
    data={'city':city}
    # print(data)
    requests.post(WEBHOOK_URL,json=data)

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler('start', start))
    app.add_handler(MessageHandler(filters.TEXT, handle_city))
    app.run_polling()


if __name__=='__main__':
    main()
