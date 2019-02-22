#!/usr/bin/env python

#import logging
#import os
#from flask import Flask, request
#import telebot

import telegram
from flask import Flask, request

BOT_URL = 'https://api.telegram.org/bot663214217:AAErqvYgKbeE1EYLBwh5b4Pds59d1jqltPY/'
TOKEN = 'bot663214217:AAErqvYgKbeE1EYLBwh5b4Pds59d1jqltPY'

app = Flask(__name__)

global bot
bot = telegram.Bot(token=TOKEN)


@app.route('/HOOK', methods=['POST'])
def webhook_handler():
    if request.method == "POST":
        # retrieve the message in JSON and then transform it to Telegram object
        update = telegram.Update.de_json(request.get_json(force=True))

        chat_id = update.message.chat.id

        # Telegram understands UTF-8, so encode text for unicode compatibility
        text = update.message.text.encode('utf-8')

        # repeat the same message back (echo)
        bot.sendMessage(chat_id=chat_id, text=text)

    return 'ok'


@app.route('/set_webhook', methods=['GET', 'POST'])
def set_webhook():
    s = bot.setWebhook('https://aiabotpython.herokuapp.com/')
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"


@app.route('/')
def index():
return '.'

"""
bot = telebot.TeleBot(BOT_TOKEN)

#bot.send_message(460390112, 'ПРТ!')

@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    bot.reply_to(message, message.text)

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, 'ПРИВЕТ!')

if "HEROKU" in list(os.environ.keys()):
    
    logger = telebot.logger
    telebot.logger.setLevel(logging.INFO)

    server = Flask(__name__)

    @server.route("/bot", methods=['POST'])
    def getMessage():
        bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
        return "!", 200

    @server.route("/")
    def webhook():
        bot.remove_webhook()
        bot.set_webhook(url="https://aiabotpython.herokuapp.com/bot") # тут url твого Хіроку додатка
        return "?", 200

    server.run(host="0.0.0.0", port=os.environ.get('PORT', '80'))
else:
    
    bot.remove_webhook()
    bot.polling(none_stop=True)
"""
