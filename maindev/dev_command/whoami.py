from telegram import Update
from telegram.ext import CallbackContext
# toilaai
def whoami(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f"chưa dev")
    update.message.reply_text(build_version())