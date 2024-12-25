from telegram import Update
from telegram.ext import CallbackContext
import requests
from token_data import *
from auth import *
from fox_request.burp_post_data import *
from dev import *

# in
def c(update: Update, context: CallbackContext) -> None:
    rs = auth(update, context)
    if rs == 1:
        #get jwt
        app_jwt=get_jwt_token()
        your_jwt=get_your_jwt()
        #get url, data corresponds to value[1], value[2] .. 
        data_burp= burp_token()
        url=data_burp[0]
        data_in=data_burp[1]

        #get headers
        burp0_headers = {"Content-Type": "application/json", "Pragma": "no-cache", "Accept": "application/json, text/plain, */*", "Authorization": f"Bearer {app_jwt}", "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8", "Cache-Control": "no-cache, no-store, must-revalidate", "Platform": "ios", "Accept-Encoding": "gzip, deflate", "App-Authorization": f"Bearer {your_jwt}", "User-Agent": "HRISProject/1995 CFNetwork/1492.0.1 Darwin/23.3.0"}

        #execute
        update.message.reply_text("onstage ...")
        response = requests.post(url, headers=burp0_headers, json=data_in)
        update.message.reply_text(f"Response: {response.text}")
    else:
        update.message.reply_text("not you, exiting ...")
    update.message.reply_text(build_version())
# out
def o(update: Update, context: CallbackContext) -> None:
    rs = auth(update, context)
    if rs == 1:
        #get jwt
        app_jwt=get_jwt_token()
        your_jwt=get_your_jwt()

        #get headers
        burp0_headers = {"Content-Type": "application/json", "Pragma": "no-cache", "Accept": "application/json, text/plain, */*", "Authorization": f"Bearer {app_jwt}", "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8", "Cache-Control": "no-cache, no-store, must-revalidate", "Platform": "ios", "Accept-Encoding": "gzip, deflate", "App-Authorization": f"Bearer {your_jwt}", "User-Agent": "HRISProject/1995 CFNetwork/1492.0.1 Darwin/23.3.0"}

        #get url, data corresponds to value[1], value[2] .. 
        data_burp= burp_token()
        url=data_burp[0]
        data_out=data_burp[2]

        #execute
        update.message.reply_text("outstage ...")
        response = requests.post(url, headers=burp0_headers, json=data_out)
        update.message.reply_text(f"Response: {response.text}")
    else:
        update.message.reply_text("not you, exiting ...")
    update.message.reply_text(build_version())