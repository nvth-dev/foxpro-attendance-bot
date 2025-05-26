import requests, sqlite3

# Define the URL and headers for the token generation API
def token_generation_auth():
    """
    Generates a token by sending a GET request to the token generation API.
    """
    generate_api = "https://sapi.fpt.vn:443/token/GenerateToken"
    headers_generate_api = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate",
        "User-Agent": "HRISProject/1995 CFNetwork/1492.0.1 Darwin/23.3.0",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
        "Authorization": "Basic dGh1eWhrMkBmcHQuY29tLnZuOjEyMzQ1Ng=="
    }
    resp = requests.get(generate_api, headers=headers_generate_api)
    authorization_token = resp.text.strip('"')  # Remove quotes from the token string
    if resp.status_code == 200:
        print ("Token generated successfully!")
        print ("Authorization token:", authorization_token)
    else:
        raise Exception(f"Failed to generate token: {resp.status_code} {resp.text}")
    return authorization_token


def token_generation_app_authorization():
    conn = sqlite3.connect('jwt.db')
    cursor = conn.cursor()

    # Retrieve the app authorization token from the database
    cursor.execute("SELECT app_authorization FROM users WHERE user_id = 1")
    row = cursor.fetchone()

    if row:
        app_token = row[0]
        print("App Authorization token retrieved successfully:", app_token)
        return app_token
    else:
        print("App Authorization token not found.")
        return None
    conn.close()    