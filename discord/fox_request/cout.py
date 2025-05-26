import requests
from fox_request import *
from data import *
from db import *
#define the headers and JSON payload for the HTTP request


def execute_command_out():
    authorization = token_generation_auth()
    app_authorization = token_generation_app_authorization()
    your_imei = get_your_imei()

    burp0_headers = {
        "Content-Type": "application/json",
        "Pragma": "no-cache",
        "Accept": "application/json, text/plain, */*",
        "Authorization": f"Bearer {authorization}",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
        "Cache-Control": "no-cache, no-store, must-revalidate",
        "Platform": "ios",
        "Accept-Encoding": "gzip, deflate",
        "App-Authorization": f"Bearer {app_authorization}",
        "User-Agent": "HRISProject/1995 CFNetwork/1492.0.1 Darwin/23.3.0"
    }

    burp0_json = {
        "CheckinType": 2, # Assuming 2 is the type for check-out
        "SmartPhoneDeviceIMEI": your_imei
    }    
    url = "https://sapi.fpt.vn:443/hrapi/api/services/app/Checkin/Checkin"
    response = requests.post(url, headers=burp0_headers, json=burp0_json)

    if response.status_code == 200:
        return f"Check out successfully! \n{response.text}"
    else:
        return f"Check out failed with status code: \n{response.status_code} {response.text}"