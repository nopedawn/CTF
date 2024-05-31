import requests

url = 'https://spinner.web.actf.co'
endpoint = '/falg'

response = requests.post(url + endpoint)

print(response.text)
