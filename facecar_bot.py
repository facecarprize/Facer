
import telebot
import os
import random

STARTERS = [
    "Очередной зверь в работе.",
    "Чистим грязь, как с души.",
    "Взялись за этого клиента всерьёз.",
]

MIDDLES = [
    "Химчистка потолка и пола — минимум.",
    "Уже видно прогресс по салону.",
    "Грязь отмывается — стиль возвращается.",
]

ENDINGS = [
    "Вечером покажем результат.",
    "Клиент ахнет.",
    "FaceCar снова делает красиво.",
]

TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет! Я FaceCar-бот. Напиши /пост — получишь готовый текст.")

@bot.message_handler(commands=['пост'])
def post_message(message):
    post = f"{random.choice(STARTERS)} {random.choice(MIDDLES)} {random.choice(ENDINGS)}"
    bot.send_message(message.chat.id, post)

bot.polling()
