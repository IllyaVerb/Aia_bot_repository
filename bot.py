#coding:utf-8

import requests  
import datetime
from random import randint
from mainClassAia import *
from AiaFrases import *

greet_bot = BotHandler("663214217:AAErqvYgKbeE1EYLBwh5b4Pds59d1jqltPY")
frases = botAiaFrases()  

now = datetime.datetime.now()


def main():  
    new_offset = None
    today = now.day
    hour = now.hour

    while True:
        greet_bot.get_updates(new_offset)

        last_update = greet_bot.get_last_update()

        last_update_id = last_update['update_id']
        last_chat_text = last_update['message']['text']
        last_chat_id = last_update['message']['chat']['id']
        last_chat_name = last_update['message']['chat']['first_name']

        #greet_bot.send_message("460390112", str(greet_bot.get_updates))
        #greet_bot.send_message(last_chat_id, str(today))
        #greet_bot.send_message(last_chat_id, str(last_chat_id))
        #greet_bot.send_message(last_chat_id, str(hour))

        if last_chat_text.lower() in frases.greetings and today == now.day:

            s = "Good "

            if  6 <= hour < 12:
                s += "morning, "

            elif 12 <= hour < 17:
                s += "afternoon, "

            elif 17 <= hour <= 23:
                s += "evening, "

            elif 0 <= hour < 6:
                s += "night, "
            
            s += str(last_chat_name)
            greet_bot.send_message(last_chat_id, s)
            #today += 1

        if last_chat_text == 'rasism?':
            greet_bot.send_message(last_chat_id, frases.rass_jokes[randint(0, len(frases.rass_jokes)-1)])
        elif last_chat_text == 'child?':
            greet_bot.send_message(last_chat_id, frases.child_jokes[randint(0, len(frases.child_jokes)-1)])

        new_offset = last_update_id + 1

if __name__ == '__main__':  
    try:
        main()
    except KeyboardInterrupt:
        exit()
