
from telegram.ext import Updater, CommandHandler
import settings as settings
import api
# from api import get_random_advise
# from database import *
import os
# port = int(os.environ.get('PORT', 5000))
DEBUG = True
def reply_to_start_command(bot, update):
    update.message.reply_text(
        "Помочь советом - это мое призвание!\n"
        "Даю советы через команду /advice",
    )

def get_advice(bot, update):

    adv = api.get_random_advise()
    update.message.reply_text(adv)

    # m = bot.sendMessage(362212345, str(update.message.from_user))
    user = update.message.from_user
    s = str(user.first_name)
    print(s)
    # m = bot.sendMessage(362212345, s)

    # print(update.message.from_user)
    # print('user')
def start_bot():
    print('bot started')

    if DEBUG == False:
        PORT = int(os.environ.get('PORT', '8443'))

        updater = Updater(settings.TELEGRAM_API_KEY_test)

        dp = updater.dispatcher
        dp.add_handler(CommandHandler("start", reply_to_start_command))
        dp.add_handler(CommandHandler("advice", get_advice))

        updater.start_webhook(listen="0.0.0.0",
                              port=PORT,
                              url_path=settings.TELEGRAM_API_KEY_test)
        updater.bot.set_webhook("https://advice-bot.herokuapp.com/" + settings.TELEGRAM_API_KEY_test)
        updater.idle()
    else:

        my_bot = Updater(settings.TELEGRAM_API_KEY_test)

        dp = my_bot.dispatcher
        dp.add_handler(CommandHandler("start", reply_to_start_command))
        dp.add_handler(CommandHandler("advice", get_advice))

        my_bot.start_polling()
        my_bot.idle()
        my_bot.start_polling()
        my_bot.idle()


if __name__ == "__main__":
    # run(server='gevent', port=os.environ.get('PORT', 5000))
    start_bot()
