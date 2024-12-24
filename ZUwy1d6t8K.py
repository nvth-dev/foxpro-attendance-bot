from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
import requests
import logging
import json


# get jwt appauth
# get_jwt_url = "https://sapi.fpt.vn:443/token/GenerateToken"
# get_jwt_headers = {"Accept": "application/json, text/plain, */*", "Accept-Encoding": "gzip, deflate", "User-Agent": "HRISProject/1995 CFNetwork/1492.0.1 Darwin/23.3.0", "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8", "Authorization": "Basic dGh1eWhrMkBmcHQuY29tLnZuOjEyMzQ1Ng=="}
# response = requests.get(get_jwt_url, headers=get_jwt_headers)

# app_auth = response.text.strip(' " ')

# token
TOKEN = "7584388846:AAHVAt679cJF4eR4k2x3OZRdcPtgLiW_xZE"
#app_auth = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ0aHV5aGsyQGZwdC5jb20udm4iLCJleHAiOjE3MzQ2MDE1MTh9.RCsfvyBf4i7gwQpUlb1sYDrbEg9JBaaOwPvQ42RDCtg"
auth_app = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1laWRlbnRpZmllciI6IjYwMTY3IiwiaHR0cDovL3NjaGVtYXMueG1sc29hcC5vcmcvd3MvMjAwNS8wNS9pZGVudGl0eS9jbGFpbXMvbmFtZSI6ImhpZXBudnRAY3lyYWRhci5jb20iLCJBc3BOZXQuSWRlbnRpdHkuU2VjdXJpdHlTdGFtcCI6Ik5RVlpHRE40V05JV1pUR0ZVQjZQUkRHNFdVTk5WRlBDIiwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2NsYWltcy9yb2xlIjoiRW1wbG95ZWUiLCJodHRwOi8vd3d3LmFzcG5ldGJvaWxlcnBsYXRlLmNvbS9pZGVudGl0eS9jbGFpbXMvdGVuYW50SWQiOiIxIiwiRW1wbG95ZWVJZENsYWltIjoiNTk4MDQiLCJzdWIiOiI2MDE2NyIsImp0aSI6IjliZWE0ZTQ3LWY4N2ItNDgyZi1hY2EyLTc4ZjM5OGMwYjY2ZSIsImlhdCI6MTczNDM0NDIzOCwibmJmIjoxNzM0MzQ0MjM4LCJleHAiOjE3MzY5MzYyMzgsImlzcyI6IkhSSVMiLCJhdWQiOiJIUklTIn0.c5Xjb6_llMkr-dVOnS5Tk_Dnvm7giypBPz2NGGKZBjo"
YOUR_USER_ID=1659283040
# data
url = "https://sapi.fpt.vn:443/hrapi/api/services/app/Checkin/Checkin"

burp0_in={"CheckinType": 1, "SmartPhoneDeviceIMEI": "016E157F-90A6-4DCD-B3FB-439AD49EC713"}
burp0_out={"CheckinType": 2, "SmartPhoneDeviceIMEI": "016E157F-90A6-4DCD-B3FB-439AD49EC713"}

class UnauthorizedUserException(Exception):
    pass
# hello command

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
    if update.message.from_user.id == 1659283040:
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