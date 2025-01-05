import json

# Chuỗi JSON từ phản hồi request
response_json = '{"result":{"accessToken":"a.b.c","refreshToken":"0c45a011-e69e-4d94-9c0a-3921271ef2da","encryptedAccessToken":"wNYmO41/48SHNstaLVXxHCC","expireInSeconds":2592000,"userId":1266016705,"tenantId":1},"targetUrl":null,"success":true,"error":null,"unAuthorizedRequest":false,"__abp":true}'

# Phân tích chuỗi JSON thành đối tượng Python
response_data = json.loads(response_json)

# Lấy giá trị của accessToken
access_token = response_data['result']['accessToken']
refreshToken = response_data['result']['refreshToken']

# In ra giá trị accessToken
print(access_token)
print (refreshToken)