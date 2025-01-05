from telegram import Update
from telegram.ext import CallbackContext
from token_data import *
from auth import *

def auth_check():
    authck = auth()
    if authck == 1:
        is_token = istoken_expired()
        if  is_token == 1: # token not expired
            return 1
        else:
            return 0 # token expired
    else:
        return 0
