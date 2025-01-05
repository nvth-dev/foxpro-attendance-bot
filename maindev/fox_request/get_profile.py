from telegram import Update
from telegram.ext import CallbackContext
import requests
from auth import *
from dev import *
from auth import is_valid_user

# get your profile and seniority
def p_process(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("checking profile ... ")
    rs = auth(update, context)
    get_p_url = "https://sapi.fpt.vn/hrapi/api/services/app/Employee/GetProfile"
    if rs == 1:
        app_jwt=get_jwt_token()
        your_jwt=get_your_jwt()
        burp0_headers = {"Content-Type": "application/json", "Pragma": "no-cache", "Accept": "application/json, text/plain, */*", "Authorization": f"Bearer {app_jwt}", "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8", "Cache-Control": "no-cache, no-store, must-revalidate", "Platform": "ios", "Accept-Encoding": "gzip, deflate", "App-Authorization": f"Bearer {your_jwt}", "User-Agent": "HRISProject/1995 CFNetwork/1492.0.1 Darwin/23.3.0"}
        response = requests.get(get_p_url, headers=burp0_headers)
        data = response.json()
        full_name = data["result"]["fullName"]
        seniority = data["result"]["seniority"]
        update.message.reply_text(f"You are {full_name}, seniority {seniority}")
    else:
        update.message.reply_text("not you, exiting ...")

def p_exec(update: Update, context: CallbackContext) -> None:
    rs = auth(update, context)
    if rs == 1:
        is_exp = istoken_expired(update, context)
        if is_exp == 1:
            p_process(update, context)  
        else:
            update.message.reply_text("Token maybe expired, please /getcode to get new your jwt, exitting ...")
    else:
        update.message.reply_text("not you, exiting ...")     
    update.message.reply_text(build_version())