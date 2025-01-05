import sqlite3
from db import *
#get jwt from db
def get_your_jwt():
    db_path = get_db_path()
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT jwt_token FROM users WHERE user_id = 1")
    jwt_token = cursor.fetchone()

    conn.close()

    if jwt_token:
        print (jwt_token[0])
        return jwt_token[0]
    else:
        return None 

#get_your_jwt()
#   change your user id here (go telegram @userinfobot)
def your_user_id():
    YOUR_USER_ID=YOUR_USER_ID  #CHANGE YOUR ID here (Requirement)
    return YOUR_USER_ID
#   change your imei device
def your_imei():
    your_imei = "YOUR_IMEI"
    return your_imei
#   change your email
def your_email():
    your_email = "your_email"
    return your_email
#   change your device token
def your_device_token():
    device_token = "your_device_token"
    return device_token

#   change your bot token here
#   bot token
def bot_token():
    TOKEN = "your_tele_bot_token" #change bot token here
    return TOKEN