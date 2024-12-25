from telegram import Update
from telegram.ext import CallbackContext
from dev import build_version

def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! Send /c go in.')
    update.message.reply_text('Hello! Send /whoami to scan yourself.')
    update.message.reply_text(build_version())