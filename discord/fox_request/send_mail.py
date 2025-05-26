import requests, json
from data import *
from db import *
# Define the URL, headers, and JSON payload for the HTTP request

proxy = {
    "http": "http://127.0.0.1:8081",
    "https": "http://127.0.0.1:8081"
}


def sent_email(): # get OTP code from email

    authorization_token = token_generation_auth()
    url_sent_mail = "https://sapi.fpt.vn:443/hrapi/api/TokenAuth/FindUserByEmailEmployee"
    headers_sentmail = {
        "Content-Type": "application/json",
        "Abp.tenantid": "1",
        "Accept": "application/json, text/plain, */*",
        "Authorization": f"Bearer {authorization_token}",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
        "Cache-Control": "no-cache, no-store, must-revalidate",
        "Platform": "ios",
        "Accept-Encoding": "gzip, deflate",
        "Abp-Tenantid": "1",
        "User-Agent": "HRISProject/2003 CFNetwork/1492.0.1 Darwin/23.3.0"
    }
    burp0_json = {"email": f"{get_your_email()}"}
    resp = requests.post(url_sent_mail, headers=headers_sentmail, json=burp0_json)
    if resp.status_code == 200:
        print ("OTP has been sent to your email. Please check your inbox.")
    else:
        raise Exception(f"Failed to send OTP: {resp.status_code} {resp.text}")
    return resp.text

def verify_otp(otp):
    authorization_token = token_generation_auth()
    burp0_url = "https://sapi.fpt.vn:443/hrapi/api/TokenAuth/AuthenticateEmployee"
    burp0_headers = {
        "Content-Type": "application/json",
        "Abp.tenantid": "1",
        "Accept": "application/json, text/plain, */*",
        "Authorization": f"Bearer {authorization_token}",  # using the OTP as the Bearer token
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
        "Cache-Control": "no-cache, no-store, must-revalidate",
        "Platform": "ios",
        "Accept-Encoding": "gzip, deflate",
        "Abp-Tenantid": "1",
        "User-Agent": "HRISProject/2003 CFNetwork/1492.0.1 Darwin/23.3.0"
    }
    burp0_json = {
        "deviceIMEI": f"{get_your_imei()}",
        "deviceName": "iPhone",
        "deviceToken": f"{get_your_device_token()}",
        "password": f"{otp}",
        "platform": "ios",
        "rememberClient": True,
        "userNameOrEmail": f"{get_your_email()}"
    }

    # Check if the user_id exists in the user_data dictionary
    verify_otp_res = requests.post(burp0_url, headers=burp0_headers, json=burp0_json)
    print (verify_otp_res.text)

    # Check if the response status code is 200 (OK)
    if verify_otp_res.status_code == 200:
        refresh_jwt = verify_otp_res.text.strip()
        response_data = json.loads(refresh_jwt) # Convert the response to a dictionary
        if response_data is not None and 'result' in response_data and 'accessToken' in response_data['result']:
            access_token = response_data['result']['accessToken']
            update_jwt_in_db(access_token)
            print(access_token)
            return True
        else:
            print("accessToken not found in the response.")
            return None
    else:
        print("accessToken not found.")


# update the JWT token and refresh token in the database
def update_jwt_in_db(access_token):
    conn = sqlite3.connect('jwt.db')
    cursor = conn.cursor()

    cursor.execute("UPDATE users SET app_authorization = ? WHERE user_id = 1", (access_token,))

    conn.commit()
    conn.close()

