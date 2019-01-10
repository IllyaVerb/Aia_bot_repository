#coding:utf-8

import requests  
import datetime
from random import randint
from mainClassAia import *
from AiaFrases import *

import os

TOKEN = "663214217:AAErqvYgKbeE1EYLBwh5b4Pds59d1jqltPY"
PORT = int(os.environ.get('PORT', '8443'))
updater = Updater(TOKEN)
# add handlers
updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN)
updater.bot.set_webhook("https://<appname>.herokuapp.com/" + TOKEN)
updater.idle()

