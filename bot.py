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
    # Handle '/start' and '/help'
    @bot.message_handler(commands=['help', 'start'])
    def send_welcome(message):
        bot.reply_to(message, "Hi there, I am EchoBot")

    # Handle all other messages with content_type 'text' (content_types defaults to ['text'])
    @bot.message_handler(func=lambda message: True)
    def echo_message(message):
        bot.reply_to(message, message.text)


    bot.polling()
"""
logger = telebot.logger
telebot.logger.setLevel(logging.INFO)

server = flask.Flask(__name__)

@server.route("/bot", methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@server.route("/")
def webhook():
    bot.deleteWebhook()
    bot.set_webhook(url="https://aiabotpython.herokuapp.com/") # тут url твого Хіроку додатка
    return "?", 200

webhook()

@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    bot.reply_to(message, message.text)
    
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, 'ПРИВЕТ!')

server.run(host="0.0.0.0", port=8443)
"""
