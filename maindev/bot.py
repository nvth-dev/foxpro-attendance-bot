from telegram.ext import Updater, CommandHandler
from auth import *
from token_data import *
from fox_request import *
from dev_command import *



def main() -> None:
    TOKEN = bot_token()
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("hello", hello))
    dispatcher.add_handler(CommandHandler("c", c))
    dispatcher.add_handler(CommandHandler("o", o))
    dispatcher.add_handler(CommandHandler("a", cal))
    dispatcher.add_handler(CommandHandler("p", p))
    dispatcher.add_handler(CommandHandler("whoami", whoami))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()