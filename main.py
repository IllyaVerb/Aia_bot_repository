from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, TelegramError
# import collections
import settings
import api
import os
#from db_connector import DB_connector
DEBUG = True
import time
NEW_ADVICE = 1
TELEGRAM_API_KEY = "bot663214217:AAErqvYgKbeE1EYLBwh5b4Pds59d1jqltPY"

class Bot():

    def __init__(self):
        #self.db_conn = DB_connector(settings.host, settings.database, settings.user, settings.password)
        print("popopo")
        self.start_bot()

    def reply_to_start_command(self, bot, update):
        user = update.message.from_user
        m = bot.sendMessage(update.message.chat_id, "lolololoo")
        #if self.db_conn.get_user_by_id(str(user.id)) == None:
            #id = str(user.id)
            #first_name = str(user.first_name)
            #last_name = str(user.last_name)
            #username = str(user.username)
            ## s = str(id) + first_name + last_name + username
            ## print(s)
            #self.db_conn.add_user(id=id, first_name=first_name,
            #                      last_name=last_name, username=username)
            #admin_msg = 'Новый пользователь ' + first_name + ' был добавлен в базу'
            #m = bot.sendMessage(user.id, admin_msg, user.id)
            #print('user added')
        #else:
            #print('user already exist')

        update.message.reply_text(
            "Помочь советом - это мое призвание!\n"
            "Даю советы через команду /advice"
        )
        m = bot.sendMessage(update.message.chat_id, "кто-то нажал старт :)")

    def get_advice(self, bot, update):

        print('get_advice')
        adv = api.get_random_advise()
        # ===============================================
        # add advice to db
        adv_id = self.db_conn.get_advice_by_text(adv)
        if adv_id == None:
            adv_id = self.db_conn.add_advice(adv)
        # ================================================
        keyboard = [[InlineKeyboardButton("👍", callback_data='1'),
                     InlineKeyboardButton("👎", callback_data=adv_id)]]
        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text(adv, reply_markup=reply_markup)

        user = update.message.from_user
        s = str(user.first_name) + " нажал advice :)"
        #m = bot.sendMessage(460390112, s)

        id = self.db_conn.get_user_by_id(str(user.id))
        if not id:
            # m = bot.sendMessage(460390112, 'starting edding new user')
            id = str(user.id)
            first_name = str(user.first_name)
            last_name = str(user.last_name)
            username = str(user.username)

            self.db_conn.add_user(id=id, first_name=first_name,
                                  last_name=last_name, username=username)
            admin_msg = 'Новый пользователь ' + first_name + '(@' + username + ')' + ' был добавлен в базу'
            #m = bot.sendMessage(460390112, admin_msg)

        datetime = time.ctime()
        self.db_conn.add_logs(r'\action', datetime, user_id=user.id, reply_text=adv)
        # m = bot.sendMessage(460390112, s)

        # print(update.message.from_user)
        # print('user')

    def get_users_list(self, bot, update):
        user = update.message.from_user

        if user.id == 460390112:
            user_list = self.db_conn.show_all_users()
            m = bot.sendMessage(460390112, user_list)

    def get_users_number(self, bot, update):
        user = update.message.from_user

        n = self.db_conn.get_users_number()
        if user.id == 460390112:
            msg = 'Всего {} пользователей'.format(n)
            m = bot.sendMessage(460390112, msg)

    def get_logs_number(self, bot, update):
        user = update.message.from_user

        n = self.db_conn.get_logs_len()
        if user.id == 460390112:
            msg = 'Всего {} раз вызвана команда /advice'.format(n)
            m = bot.sendMessage(460390112, msg)

    def get_avrg_clicks(self, bot, update):
        user = update.message.from_user

        n = self.db_conn.get_logs()
        if user.id == 460390112:
            msg = 'Всего {} пользователей'.format(n)
            m = bot.sendMessage(460390112, msg)

    def get_users_saved_adv(self, bot, update):
        try:
            user_id = update.message.from_user.id
            adv_list = self.db_conn.get_users_adv_list(user_id)
            if adv_list is not None:
                for i in adv_list:
                    # print(i[0])
                    self.send_msg_to_user(bot, update, user_id, msg=i[0])
        except:
            pass

    def send_msg_to_user(self, bot, update, user_id, msg, reply_markup=None):

        bot.sendMessage(user_id, msg, reply_markup=reply_markup)
        # print('sent')

    def send_msg_to_all_users(self, bot, update):
        adv = update.message.text
        msg = 'Совет дня😏👌\n' + adv

        adv_id = self.db_conn.get_advice_by_text(adv)
        if adv_id == None:
            adv_id = self.db_conn.add_advice(adv, is_daily_advice=1)

        # print(len(adv))
        keyboard = [[InlineKeyboardButton("👍", callback_data='1'),
                     InlineKeyboardButton("👎", callback_data=adv_id)]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        users_id = self.db_conn.get_all_user_id()
        # try:
        #     self.send_msg_to_user(bot, update, user_id=460390112, msg=msg, reply_markup=reply_markup)
        # except Exception as ex:
        #     print(ex)
        n = 0
        n_users = len(users_id)
        # print(len(users_id))
        for user_id in users_id:
                user_id = user_id[0]

                try:

                    self.send_msg_to_user(bot, update, user_id=user_id, msg=msg, reply_markup=reply_markup)
                    n += 1
                except:
                    error_msg = 'error with id: ' + str(user_id)
                    # print(error_msg)
                    self.send_msg_to_user(bot, update, user_id=460390112, msg=error_msg)
        msg = 'Рассылка окончена. \n' \
              'Сообщение получили ' + str(n) + ' пользователей из ' + str(n_users)
        self.send_msg_to_user(bot, update, user_id=460390112, msg=msg)

        return ConversationHandler.END

    def send_info(self, bot, update):
        # adv = update.message.text
        msg = 'Теперь ты можешь сохранить себе лучшие советы, нажав 👍\n' \
              'Ты можешь посмотреть сохраненные советы через команду /saved\n' \
              'Хочешь новый совет? Нажми /advice 😏'

        # adv_id = self.db_conn.get_advice_by_text(adv)
        # if adv_id == None:
        #     adv_id = self.db_conn.add_advice(adv, is_daily_advice=1)

        # print(len(adv))
        # keyboard = [[InlineKeyboardButton("👍", callback_data='1'),
        #              InlineKeyboardButton("👎", callback_data=adv_id)]]
        # reply_markup = InlineKeyboardMarkup(keyboard)
        users_id = self.db_conn.get_all_user_id()
        # try:
        #     self.send_msg_to_user(bot, update, user_id=460390112, msg=msg, reply_markup=reply_markup)
        # except Exception as ex:
        #     print(ex)
        n = 0
        n_users = len(users_id)
        # print(len(users_id))
        for user_id in users_id:
                user_id = user_id[0]

                try:

                    self.send_msg_to_user(bot, update, user_id=user_id, msg=msg)
                    n += 1
                except:
                    error_msg = 'error with id: ' + str(user_id)
                    # print(error_msg)
                    self.send_msg_to_user(bot, update, user_id=460390112, msg=error_msg)
        msg = 'Рассылка окончена. \n' \
              'Сообщение получили ' + str(n) + ' пользователей из ' + str(n_users)
        self.send_msg_to_user(bot, update, user_id=460390112, msg=msg)

        return

    def start_mailing(self, bot, update):
        self.send_msg_to_user(bot, update, user_id=460390112, msg='Дай мне совет, который я всем разошлю')
        return NEW_ADVICE

    def fallback(self, bot, update):
        self.send_msg_to_user(bot, update, user_id=460390112, msg='не понимаю')
        return NEW_ADVICE

    def button(self, bot, update):
        query = update.callback_query
        msg_text = query.message.text

        user_id = query.from_user.id
        if query.data == '1':
            if '📌' not in msg_text:
                text = '📌' + msg_text
                self.add_saved_advice(user_id=user_id, adv=msg_text)
            adv_id = self.db_conn.get_advice_by_text(msg_text)
        else:
            adv_id = query.data
            if '📌' not in msg_text:
                return
            adv = self.db_conn.get_advice_by_id(adv_id)
            text = adv
            self.db_conn.drop_saved_advice(advice=adv)

        bot.edit_message_text(chat_id=query.message.chat_id,
                                  message_id=query.message.message_id,
                                  text=text)


        keyboard = [[InlineKeyboardButton("👍", callback_data='1'),
                     InlineKeyboardButton("👎", callback_data=adv_id)]]
        reply_markup = InlineKeyboardMarkup(keyboard)

        bot.edit_message_reply_markup(
            chat_id=query.message.chat_id,
            message_id=query.message.message_id,
            reply_markup=reply_markup)

    def add_saved_advice(self, user_id, adv):
        # print('start save advice')
        adv_id = self.db_conn.get_advice_by_text(adv)
        if adv_id == None:
            adv_id = self.db_conn.add_advice(adv)
        self.db_conn.add_users_advice(user_id=user_id, advice_id=adv_id)
        # print('advice saved')





    def start_bot(self):
        print('bot started')

        if DEBUG == False:
            PORT = int(os.environ.get('PORT', '8443'))

            updater = Updater(token=TELEGRAM_API_KEY)
            
            m = bot.sendMessage(460390112, 'Дайkjhgfdsdfgh', reply_markup=None)
            
            dp = updater.dispatcher
            dp.add_handler(CommandHandler("start", self.reply_to_start_command))
            dp.add_handler(CommandHandler("advice", self.get_advice))
            dp.add_handler(CommandHandler("users_list", self.get_users_list))
            dp.add_handler(CommandHandler("number", self.get_users_number))
            dp.add_handler(CommandHandler("number_logs", self.get_logs_number))
            dp.add_handler(CommandHandler("saved", self.get_users_saved_adv))
            dp.add_handler(CommandHandler("send_info", self.send_info))

            #dp.add_handler(CallbackQueryHandler(self.button))
            #conv_handler = ConversationHandler(
            #    entry_points=[CommandHandler('send', self.start_mailing)],
            #    states={
            #        NEW_ADVICE: [MessageHandler(Filters.text, self.send_msg_to_all_users)],
            #    },
            #    fallbacks=[CommandHandler('cancel', self.fallback)]
            #)

            #dp.add_handler(conv_handler)
            updater.start_webhook(listen="0.0.0.0",
                                  port=PORT,
                                  url_path=TELEGRAM_API_KEY)
            updater.bot.set_webhook("https://aiabotpython.herokuapp.com/" + TELEGRAM_API_KEY)
            updater.idle()
        else:

            updater = Updater(TELEGRAM_API_KEY)

            dp = updater.dispatcher
            dp.add_handler(CommandHandler("start", self.reply_to_start_command))
            dp.add_handler(CommandHandler("advice", self.get_advice))
            dp.add_handler(CommandHandler("users_list", self.get_users_list))
            dp.add_handler(CommandHandler("number", self.get_users_number))
            dp.add_handler(CommandHandler("number_logs", self.get_logs_number))
            dp.add_handler(CommandHandler("saved", self.get_users_saved_adv))
            dp.add_handler(CommandHandler("send_info", self.send_info))

            #dp.add_handler(CallbackQueryHandler(self.button))
            #conv_handler = ConversationHandler(
            #    entry_points=[CommandHandler('send', self.start_mailing)],
            #    states={
            #        NEW_ADVICE: [MessageHandler(Filters.text, self.send_msg_to_all_users)],
            #    },
            #    fallbacks=[CommandHandler('cancel', self.fallback)]
            #)

            #dp.add_handler(conv_handler)
            updater.start_polling()
            updater.idle()
            m = bot.sendMessage(460390112, 'Дайkjhgfdsdfgh', reply_markup=None)



if __name__ == "__main__":
    bot = Bot()
