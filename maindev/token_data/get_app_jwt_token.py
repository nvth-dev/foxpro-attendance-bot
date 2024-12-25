import requests

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
        jwt = response.text.strip(' " ')
        # return jwt
        return jwt
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None