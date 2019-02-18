#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This is a simple echo bot using decorators and webhook with CherryPy
# It echoes any incoming text messages and does not use the polling method.
import requests
import telebot

BOT_URL = 'https://api.telegram.org/bot663214217:AAErqvYgKbeE1EYLBwh5b4Pds59d1jqltPY/'
BOT_TOKEN = 'bot663214217:AAErqvYgKbeE1EYLBwh5b4Pds59d1jqltPY'
bot = telebot.TeleBot(BOT_TOKEN)

# Перевіряємо чи є змінна середовище Хіроку
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
        bot.set_webhook(url="https://aiabotpython.herokuapp.com/") # тут url твого Хіроку додатка
        return "?", 200
    server.run(host="0.0.0.0", port=os.environ.get('PORT', 80))
else:
    #якщо змінної середовища HEROKU нема, отже запуск з консолі.  
    # Видаляємо про всяк випадок вебхук і запускаємо з звичайним полілнгом.
    bot.remove_webhook()
    bot.polling(none_stop=True)
    

