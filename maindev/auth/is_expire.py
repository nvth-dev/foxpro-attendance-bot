from telegram import Update
from telegram.ext import CallbackContext
import requests
from token_data import *

proxy = {
    'http': 'http://127.0.0.1:8080',  
    'https': 'http://127.0.0.1:8080'
}

def istoken_expired(update: Update, context: CallbackContext) -> None:
    app_jwt = get_jwt_token()
    your_jwt = get_your_jwt()
    #your_jwt = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1laWRlbnRpZmllciI6IjYwMTY3IiwiaHR0cDovL3NjaGVtYXMueG1sc29hcC5vcmcvd3MvMjAwNS8wNS9pZGVudGl0eS9jbGFpbXMvbmFtZSI6ImhpZXBudnRAY3lyYWRhci5jb20iLCJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9lbWFpbGFkZHJlc3MiOiJoaWVwbnZ0QGN5cmFkYXIuY29tIiwiQXNwTmV0LklkZW50aXR5LlNlY3VyaXR5U3RhbXAiOiJOUVZaR0RONFdOSVdaVEdGVUI2UFJERzRXVU5OVkZQQyIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvcm9sZSI6IkVtcGxveWVlIiwiaHR0cDovL3d3dy5hc3BuZXRib2lsZXJwbGF0ZS5jb20vaWRlbnRpdHkvY2xhaW1zL3RlbmFudElkIjoiMSIsIkVtcGxveWVlSWRDbGFpbSI6IjU5ODA0Iiwic3ViIjoiNjAxNjciLCJqdGkiOiIwMGI3MDYyNC03NWI5LTQ5ZGMtOWQ3Zi1hYzgyZDVjZTg0ZDYiLCJpYXQiOjE3MzU2MzgxODgsIm5iZiI6MTczNTYzODE4OCwiZXhwIjoxNzM4MjMwMTg4LCJpc3MiOiJIUklTIiwiYXVkIjoiSFJJUyJ9.w7l_27-zG7jlQR8UqqJ2MuIluahpZ8kFXpBAPOjB-P8'
    expire_url_ = "https://sapi.fpt.vn:443/hrapi/api/services/app/Post/ListBannerForAppPaging"
    expire_headers = {"Content-Type": "application/json", "Pragma": "no-cache", "Accept": "application/json, text/plain, */*", "Authorization": f"Bearer {app_jwt}", "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8", "Cache-Control": "no-cache, no-store, must-revalidate", "Platform": "ios", "Accept-Encoding": "gzip, deflate", "App-Authorization": f"Bearer {your_jwt}", "User-Agent": "HRISProject/2003 CFNetwork/1492.0.1 Darwin/23.3.0"}
    expire_json={"pageIndex": 1, "pageSize": 5}
    resp = requests.post(expire_url_, headers=expire_headers, json=expire_json)
    print (resp)
    if resp.status_code == 200:
        return 1        
    else:
        return 0      

