# data
def burp_token():
    url = "https://sapi.fpt.vn:443/hrapi/api/services/app/Checkin/Checkin"
    burp0_in={"CheckinType": 1, "SmartPhoneDeviceIMEI": "016E157F-90A6-4DCD-B3FB-439AD49EC713"}
    burp0_out={"CheckinType": 2, "SmartPhoneDeviceIMEI": "016E157F-90A6-4DCD-B3FB-439AD49EC713"}
    return url, burp0_in, burp0_out