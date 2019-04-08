
from telegram.ext import Updater, CommandHandler
import settings
import api
import os
# from database import *

def reply_to_start_command(bot, update):
    update.message.reply_text(
        "Помочь советом - это мое призвание!\n"
        "Даю советы через команду /advice",
    )


def get_advice(bot, update):
    adv = api.get_random_advise()
    update.message.reply_text(adv)

    user = update.message.from_user
    id = str(user.id)
    first_name = str(user.first_name)
    last_name = str(user.last_name)
    username = str(user.username)
    s = id + first_name + last_name + username
    print(s)
    # adv = api.get_random_advise()
    # update.message.reply_text(adv)

def start_bot():
    print('bot started')
    PORT = int(os.environ.get('PORT', '8443'))

    updater = Updater(settings.TELEGRAM_API_KEY)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", reply_to_start_command))
    dp.add_handler(CommandHandler("advice", get_advice))

    updater.start_webhook(listen="0.0.0.0",
                          port=PORT,
                          url_path=settings.TELEGRAM_API_KEY)
    updater.bot.set_webhook("https://aiabotpython.herokuapp.com/" + settings.TELEGRAM_API_KEY)
    updater.idle()


if __name__ == "__main__":
    start_bot()
