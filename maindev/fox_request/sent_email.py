from telegram import Update
from telegram.ext import CallbackContext
import requests
from token_data import *
import json
from auth import *
from dev import *
from db import *
import sqlite3


user_data = {}

def sent_mail(update: Update, context: CallbackContext) -> None:
    app_jwt  = get_jwt_token()
    sent_mail_url = "https://sapi.fpt.vn:443/hrapi/api/TokenAuth/FindUserByEmailEmployee"
    sent_mail_headers = {"Content-Type": "application/json", "Abp.tenantid": "1", "Accept": "application/json, text/plain, */*", "Authorization": f"Bearer {app_jwt}", "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8", "Cache-Control": "no-cache, no-store, must-revalidate", "Platform": "ios", "Accept-Encoding": "gzip, deflate", "Abp-Tenantid": "1", "User-Agent": "HRISProject/2003 CFNetwork/1492.0.1 Darwin/23.3.0"}
    sent_mail_json={"email": f"{your_email()}"}
    requests.post(sent_mail_url, headers=sent_mail_headers, json=sent_mail_json)


def process(update: Update, context: CallbackContext) -> None:
    rs = auth(update, context)
    if rs == 1:
        sent_mail(update, context)
        
        user_data[update.message.from_user.id] = {'waiting_for_otp': True}
        update.message.reply_text('Enter OTP:') 
    else:
        update.message.reply_text("not you, exiting ...")         

def get_jwt_refresh_token_process(update: Update, context: CallbackContext) -> None:
#callback
    # variable app_jwt
    user_id = update.message.from_user.id
    if user_id in user_data and user_data[user_id].get('waiting_for_otp', False):
        code_otp = update.message.text
        print(code_otp)

        #get app_jwt authorize
        app_jwt  = get_jwt_token()

        refresh_url = "https://sapi.fpt.vn:443/hrapi/api/TokenAuth/AuthenticateEmployee"
        refresh_headers = {"Content-Type": "application/json", "Abp.tenantid": "1", "Accept": "application/json, text/plain, */*", "Authorization": f"Bearer {app_jwt}", "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8", "Cache-Control": "no-cache, no-store, must-revalidate", "Platform": "ios", "Accept-Encoding": "gzip, deflate", "Abp-Tenantid": "1", "User-Agent": "HRISProject/2003 CFNetwork/1492.0.1 Darwin/23.3.0"}
        refresh_json={"deviceIMEI": f"{your_imei()}", "deviceName": "iPhone", "deviceToken": f"{your_device_token()}", "password": f"{code_otp}", "platform": "ios", "rememberClient": True, "userNameOrEmail": f"{your_email()}"}
        resp = requests.post(refresh_url, headers=refresh_headers, json=refresh_json)
        print (resp)
        if resp.status_code == 200:
            refresh_jwt = resp.text.strip()
            response_data = json.loads(refresh_jwt)
            
            if response_data is not None and 'result' in response_data and 'accessToken' in response_data['result']:
                access_token = response_data['result']['accessToken']
                refresh_token = response_data['result']['refreshToken']
                update_jwt_in_db(access_token, refresh_token)
                print(access_token)
                print(refresh_token)
                # Reset user status
                user_data[user_id] = {}
                update.message.reply_text("please dev.")
                #return access_token, refresh_token

            else:
                print("accessToken not found.")
        else:
            print("get JWT token error.")
    else:
        update.message.reply_text("please enter otp after sent email.")
    update.message.reply_text(build_version())

def get_jwt_refresh_token_exec(update: Update, context: CallbackContext) -> None:
    rs = auth(update, context)
    if rs == 1:
        get_jwt_refresh_token_process(update, context)
    else:
        update.message.reply_text('not you, exiting ...')
# update jwt to db
def update_jwt_in_db(access_token, refresh_token):
    db_path = get_db_path()
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("UPDATE users SET jwt_token = ?, refresh_token = ? WHERE user_id = 1", (access_token, refresh_token))

    conn.commit()
    conn.close()

    