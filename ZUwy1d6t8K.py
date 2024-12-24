from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
import requests
import logging
import json


#THE INFORMATION NEED CHANGE
# token
TOKEN = "YOUR_BOT_TOKEN" #CHANGE YOUR BOT TOKEN EXP (7584388836:AAHVAt679cJF4eR4k2x3OZRdcPtgLiW_xZE)

auth_app = "YOUR_JWT_LOGIN" #CHANGE YOUR JWT
YOUR_USER_ID="TELEGRAM_USER_ID"# CHANGE YOUR TELEGRAM USERID FROM TELEGRAM BOT: @userinfobot
# data
url = "https://sapi.fpt.vn:443/hrapi/api/services/app/Checkin/Checkin"

burp0_in={"CheckinType": 1, "SmartPhoneDeviceIMEI": "016E157F-90A6-4DCD-B3FB-439AD49EC713"} #CHANGE YOUR IMEI IS MOBILE DEVICES YOU ACTIVE CHECKIN
burp0_out={"CheckinType": 2, "SmartPhoneDeviceIMEI": "016E157F-90A6-4DCD-B3FB-439AD49EC713"} #CHANGE YOUR IMEI IS MOBILE DEVICES YOU ACTIVE CHECKIN

class UnauthorizedUserException(Exception):
    pass
# hello command
#END CHANGE
build_version = 12242024
dev = f"build {build_version} by vekman"

def get_jwt_token():
    get_jwt_url = "https://sapi.fpt.vn:443/token/GenerateToken"
    get_jwt_headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate",
        "User-Agent": "HRISProject/1995 CFNetwork/1492.0.1 Darwin/23.3.0",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
        "Authorization": "Basic dGh1eWhrMkBmcHQuY29tLnZuOjEyMzQ1Ng=="
    }

    try:
        response = requests.get(get_jwt_url, headers=get_jwt_headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        # get jwt 
        app_auth = response.text.strip(' " ')
        # return jwt
        return app_auth
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! Send /c go in.')
    update.message.reply_text('Hello! Send /whoami to scan yourself.')
    update.message.reply_text(dev)

# toilaai
def whoami(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f"chưa dev")
    update.message.reply_text(dev)

# check auth to use bot
def auth(update: Update, context: CallbackContext) -> None:
    if update.message.from_user.id == YOUR_USER_ID:
        return 1
    else:
        return 0
# in
def c(update: Update, context: CallbackContext) -> None:
    rs = auth(update, context)
    if rs == 1:
        app_auth=get_jwt_token()
        burp0_headers = {"Content-Type": "application/json", "Pragma": "no-cache", "Accept": "application/json, text/plain, */*", "Authorization": f"Bearer {app_auth}", "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8", "Cache-Control": "no-cache, no-store, must-revalidate", "Platform": "ios", "Accept-Encoding": "gzip, deflate", "App-Authorization": f"Bearer {auth_app}", "User-Agent": "HRISProject/1995 CFNetwork/1492.0.1 Darwin/23.3.0"}
        update.message.reply_text("onstage ...")
        response = requests.post(url, headers=burp0_headers, json=burp0_in)
        update.message.reply_text(f"Response: {response.text}")
    else:
        update.message.reply_text("not you, exiting ...")
    update.message.reply_text(dev)
# out
def o(update: Update, context: CallbackContext) -> None:
    rs = auth(update, context)
    if rs == 1:
        app_auth=get_jwt_token()
        burp0_headers = {"Content-Type": "application/json", "Pragma": "no-cache", "Accept": "application/json, text/plain, */*", "Authorization": f"Bearer {app_auth}", "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8", "Cache-Control": "no-cache, no-store, must-revalidate", "Platform": "ios", "Accept-Encoding": "gzip, deflate", "App-Authorization": f"Bearer {auth_app}", "User-Agent": "HRISProject/1995 CFNetwork/1492.0.1 Darwin/23.3.0"}
        update.message.reply_text("outstage ...")
        response = requests.post(url, headers=burp0_headers, json=burp0_out)
        update.message.reply_text(f"Response: {response.text}")
    else:
        update.message.reply_text("not you, exiting ...")
    update.message.reply_text(dev)

# calendar
def cal(update: Update, context: CallbackContext) -> None:
    rs = auth(update, context)
    if rs == 1:
        user_input = update.message.text.split()

        app_auth=get_jwt_token()
        burp0_headers = {"Content-Type": "application/json", "Pragma": "no-cache", "Accept": "application/json, text/plain, */*", "Authorization": f"Bearer {app_auth}", "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8", "Cache-Control": "no-cache, no-store, must-revalidate", "Platform": "ios", "Accept-Encoding": "gzip, deflate", "App-Authorization": f"Bearer {auth_app}", "User-Agent": "HRISProject/1995 CFNetwork/1492.0.1 Darwin/23.3.0"}
        
        # input /cal
        if len(user_input) == 1:
            update.message.reply_text("Enter month year (exp: \cal 12 2024).")
        # input /cal month year
        elif len(user_input) == 3:
            month = user_input[1]
            year = user_input[2]
            
            url_cal = "https://sapi.fpt.vn/hrapi/api/services/app/Checkin/GetListCheckinLogStatisticInMonth"
            burp0_json = {"Month": f"{month}", "Year": f"{year}"}
            
            response = requests.post(url_cal, headers=burp0_headers, json=burp0_json)
            data = response.json()
            #debug
            #print (data)
            result = data.get('result', {})
            if result is not None:
                checkin_logs = result.get('checkinLogStatus', [])
                
                message = ""

                for log in checkin_logs:
                    date = log.get('date', '')
                    in_status = log.get('checkinStatus', '')
                    out_status = log.get('checkoutStatus', '')
                    isAttdEnabled = log.get('isAttdEnabled', '')
                    
                    message += f"Date: {date}\nIn Status: {in_status}\nOut Status: {out_status}\nisAttendent: {isAttdEnabled}\n\n"
                
                if message:
                    update.message.reply_text(message)
                else:
                    update.message.reply_text("no data check-in log.")
            else:
                update.message.reply_text("Can't get smt data")
        else:
            update.message.reply_text("Enter time to check month year (exp: /cal 12 2024).")
    else:
        update.message.reply_text("not you, exitting...")
    update.message.reply_text(dev)
# main
def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("hello", hello))
    #dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, whoami))
    dispatcher.add_handler(CommandHandler("c", c))
    dispatcher.add_handler(CommandHandler("o", o))
    dispatcher.add_handler(CommandHandler("a", cal))
    dispatcher.add_handler(CommandHandler("whoami", whoami))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()