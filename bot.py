#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import logging
import os
import flask
from telebot import types
import telebot

BOT_URL = 'https://api.telegram.org/bot663214217:AAErqvYgKbeE1EYLBwh5b4Pds59d1jqltPY/'
BOT_TOKEN = 'bot663214217:AAErqvYgKbeE1EYLBwh5b4Pds59d1jqltPY'

bot = telebot.TeleBot(BOT_TOKEN)

if "HEROKU" in list(os.environ.keys()):
    
    logger = telebot.logger
    telebot.logger.setLevel(logging.INFO)

    server = flask.Flask(__name__)

    @server.route("/bot", methods=['POST'])
    def getMessage():
        bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
        return "!", 200

    @server.route("/")
    def webhook():
        bot.remove_webhook()
        bot.set_webhook(url="https://aiabotpython.herokuapp.com/") # тут url твого Хіроку додатка
        return "?", 200
    
    bot.send_message(460390112, 'ПРТ!')

    @bot.message_handler(func=lambda message: True, content_types=['text'])
    def echo_message(message):
        bot.reply_to(message, message.text)

    @bot.message_handler(commands=['start'])
    def handle_start(message):
        bot.send_message(message.chat.id, 'ПРИВЕТ!')

    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', '8443')))
else:
    #якщо змінної середовища HEROKU нема, отже запуск з консолі.  
    # Видаляємо про всяк випадок вебхук і запускаємо з звичайним полілнгом.
    bot.remove_webhook()
    bot.polling(none_stop=True)
