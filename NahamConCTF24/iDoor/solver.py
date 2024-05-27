import re
import hashlib
import requests
from bs4 import BeautifulSoup

base_url = "http://challenge.nahamcon.com:31646/"

for i in range(20):
    sha256_hash = hashlib.sha256(str(i).encode()).hexdigest()
    url = base_url + sha256_hash
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    card_body = soup.find('div', class_='card-body')
    print(f"URL: {url}")
    print(f"Response:\n{card_body}\n")

    flag = re.findall(r'flag{.*}', str(card_body))
    
    if flag:
        print(flag[0])
        break
