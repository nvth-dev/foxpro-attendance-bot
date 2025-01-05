from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from fox_request import *
from dev_command import *
from token_data import *


class UnauthorizedUserException(Exception):
    pass

def main() -> None:
    TOKEN = bot_token()
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    #check expired token
    dispatcher.add_handler(CommandHandler("val", istoken_expired))

    dispatcher.add_handler(CommandHandler("hello", hello))
    dispatcher.add_handler(CommandHandler("c", c_exec))
    dispatcher.add_handler(CommandHandler("o", o_exec))
    dispatcher.add_handler(CommandHandler("a", cal_exec))
    dispatcher.add_handler(CommandHandler("p", p_exec))
    # get jwt after expired
    dispatcher.add_handler(CommandHandler("getcode", process))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, get_jwt_refresh_token_exec))
    
    dispatcher.add_handler(CommandHandler("whoami", whoami))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()