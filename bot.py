#coding:utf-8

import requests  
import datetime
from mainClassAia import *

greet_bot = BotHandler("663214217:AAErqvYgKbeE1EYLBwh5b4Pds59d1jqltPY")  
greetings = ('hello', 'hi', 'Hello', 'Hi')  
rass_jokes = ('В чём разница между негром и апельсином?\nКогда апельсин снимают с дерева - он ещё живой.','В машине сидят негр и мексиканец. Кто за рулём?\nПолицейский.','Что надо сделать, если вам навстречу бежит окровавленный негр?\nПерезарядить.', 'Какие у негра есть три белых вещи?\nГлаза, зубы и хозяин.', 'Негр и мексиканец падают с небоскрёба. Кто упадёт первым?\nКакая разница?', 'Что вы скажете, увидев негра, по шею закатанного в бетон?\nМало бетона.', 'Почему в гарлеме так много деревьев?\nОбщественный транспорт', 'Как называется один белый в окружении тысячи негров?\nНадсмотрщик.', 'Почему, когда какие-либо приборы не работают - по ним бьют?\nС рабами это срабатывало.', 'Как называется негр на велосипеде?\nВор.', 'Что надо сказать негру в зале суда?\nПодсудимый, встаньте!', 'Почему в Нью Йорке так много негров, а в Калифорнии - землетрясений?\nКалифорния выбирала первой.', 'Негр и мексиканец падают с дерева. Кто упадёт на землю первым?\nМексиканец. Негр не долетит - ему помешает верёвка.', 'Как чёрная женщина борется с преступностью?\nДелает аборт.', 'Какие три самых сложных года в жизни негра?\nПервый класс.', 'Как называется негр в университете?\nУборщик.', 'Что надо бросить тонущему негру?\nЕго семью.', 'Я очень люблю негров. У меня даже было несколько хороших друзей среди них...Это пока отец их не продал.', 'Как бы вы назвали негра на луне?\nПроблема.\nКак бы вы назвали сто негров на луне?\nПроблема.\nКак бы вы назвали всех негров на луне?\nРешение проблемы.', 'Как сделать так что бы негр перестал тонуть?\nНадо просто убрать ногу с его головы.', 'Как снять негра с дерева?\nПеререзать веревку.', 'Как вы назовете 50 негров на дне океана?\nХорошее начало.', 'В чем разница между негром и луком? Когда режешь лук, на глазах выступают слезы.', 'Как назвать ниггеpа с IQ 15? Одаренный. А с IQ 150? Племя.' )
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

        if last_chat_text.lower() in greetings and today == now.day:

            s = "Good "

            if  6 <= hour < 12:
                s += "morning, "

            elif 12 <= hour < 17:
                s += "day, "

            elif 17 <= hour <= 23:
                s += "evening, "

            elif 0 <= hour < 6:
                s += "night, "
            
            s += str(last_chat_name)
            greet_bot.send_message(last_chat_id, s)
            today += 1

        new_offset = last_update_id + 1

if __name__ == '__main__':  
    try:
        main()
    except KeyboardInterrupt:
        exit()
