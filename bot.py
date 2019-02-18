#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import logging
from telebot import types
import telebot

BOT_URL = 'https://api.telegram.org/bot663214217:AAErqvYgKbeE1EYLBwh5b4Pds59d1jqltPY/'
BOT_TOKEN = 'bot663214217:AAErqvYgKbeE1EYLBwh5b4Pds59d1jqltPY'

bot = telebot.TeleBot(BOT_TOKEN)
    
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
    bot.set_webhook(url="https://aiabotpython.herokuapp.com/") # тут url твого Хіроку додатка
    return "?", 200
server.run(host="0.0.0.0", port=os.environ.get('PORT', 80))

    

