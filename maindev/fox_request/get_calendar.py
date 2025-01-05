from telegram import Update
from telegram.ext import CallbackContext
import requests
from token_data import *
from fox_request import *
from auth import *
from dev import *

# calendar
def cal_process(update: Update, context: CallbackContext) -> None:
    user_input = update.message.text.split()

    #get jwt
    app_jwt=get_jwt_token()
    your_jwt=get_your_jwt()

    burp0_headers = {"Content-Type": "application/json", "Pragma": "no-cache", "Accept": "application/json, text/plain, */*", "Authorization": f"Bearer {app_jwt}", "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8", "Cache-Control": "no-cache, no-store, must-revalidate", "Platform": "ios", "Accept-Encoding": "gzip, deflate", "App-Authorization": f"Bearer {your_jwt}", "User-Agent": "HRISProject/1995 CFNetwork/1492.0.1 Darwin/23.3.0"}
    
    # input /cal
    if len(user_input) == 1:
        update.message.reply_text("Enter month year (exp: /a 12 2024).")
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
                checkinTime = log.get('checkinTime', '')
                checkoutTime = log.get('checkoutTime', '')
                
                message += f"Date: {date}\nIn Status: {in_status}\nIn Time: {checkinTime}\nOut Status: {out_status}\nOut Time: {checkoutTime}\nisAttendent: {isAttdEnabled}\n\n"
            
            if message:
                update.message.reply_text(message)
            else:
                update.message.reply_text("no data check-in log.")
        else:
            update.message.reply_text("Can't get smt data")
    else:
        update.message.reply_text("Enter time to check month year (exp: /a 12 2024).")

def cal_exec(update: Update, context: CallbackContext) -> None:
    rs = auth(update, context)
    if rs == 1:
        is_exp = istoken_expired(update, context)
        if is_exp == 1:
            update.message.reply_text('Listing ...')
            cal_process(update, context)  
        else:
            update.message.reply_text("Token maybe expired, please /getcode to get new your jwt, exitting ...")
    else:
        update.message.reply_text("not you, exiting ...")     
    update.message.reply_text(build_version())