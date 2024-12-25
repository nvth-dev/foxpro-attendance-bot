from telegram import Update
from telegram.ext import CallbackContext
from token_data import *

# check auth to use bot
def auth(update: Update, context: CallbackContext) -> None:
    YOUR_USER_ID = your_user_id()
    if update.message.from_user.id == YOUR_USER_ID:
        return 1
    else:
        return 0