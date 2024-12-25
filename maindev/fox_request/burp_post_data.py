from token_data import *
# data
def burp_token():

    url = "https://sapi.fpt.vn:443/hrapi/api/services/app/Checkin/Checkin"
    burp0_in={"CheckinType": 1, "SmartPhoneDeviceIMEI": f"{your_imei()}"}
    burp0_out={"CheckinType": 2, "SmartPhoneDeviceIMEI": f"{your_imei()}"}
    return url, burp0_in, burp0_out