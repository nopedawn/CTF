# FORENSICS

## Vastness of Space

<details>
  <summary>Description :</summary>
  
  > Is space really that empty?
  
</details>

Given the image file [Empty_Space.jpg](./Empty_Space.jpg) first You can get the password by checking the metadata by using `Exiftool`

```bash
$ exiftool Empty_Space.jpg
```

here's the password `xp_comment: The password is "BBCTF"`

Use [steghide](https://www.kali.org/tools/steghide/) to extract the embedded text file and enter passphrase as the password you got from exifdata 

```bash
$ steghide extract -sf Empty_Space.jpg
```

Got the [somedata.txt](./somedata.txt) then make a script to convert those numbers from `somedata.txt` into an image, here's the python3 script that I've coded

```python
from PIL import Image

width = None
height = None
data = []
with open("somedata.txt") as f:
    for line in f:
        x, y = map(int, line.split(","))
        data.append((x, y))
        if width is None or x > width:
            width = x
        if height is None or y > height:
            height = y

width += 20
height += 20
image = Image.new("RGB", (width, height), (255, 255, 255))
pixels = image.load()

for point in data:
    pixels[point[0]+5, point[1]+5] = (0, 0, 0)

image = image.resize((500,500), Image.NEAREST)
image.save("output.png")
```

Got the result in qr code [output.png](output.png) then scan it

<details>
  <summary>FLAG :</summary>
  
  > `flag{qUiCk_R3sP0nse_c0d3}`
  
</details>
<br>

## Random Requests

<details>
  <summary>Description :</summary>
  
  > I captured these very random http requests. Can you help me decode them? <br>
  > [random_requests.pcapng](./random_requests.pcapng)
  
</details>

Using the protocol layer statistics to understand the types of recorded packets and looking at them in various ways, you can see `http && ip.src_host == 142.250.67.132` characteristic requests.
`GET /flag=0` or `1` or `%20` is recorded after.

If you take them all in chronological order and change `%20` to a line break instead of a blank, it looks like the base64 encoded in 8 byte binary representation.

```bash
$ python3
>>> chr(int('01011010', 2))
'Z'
>>> chr(int('01101101', 2))
'm'
>>> chr(int('01111000', 2))
'x'
```

We need to extract that binary representated with this script, then save into file text

```python
#!/usr/bin/env python3
from scapy.all import *
from base64 import *

packets = rdpcap("random_requests.pcapng")

binary_output = ""

for packet in packets:
    if packet[IP].dst == "142.250.67.132" and packet.haslayer(Raw):
        binary_output += packet[Raw].load.split(b" ")[1].decode().split("=")[1]

output = binary_output.replace("%20", " ")

with open("output.txt", "w") as file:
    file.write(output)
```

Convert with [CyberChef](https://gchq.github.io/CyberChef/#recipe=From_Binary('Space',8)From_Base64('A-Za-z0-9%2B/%3D',true,false)&input=MDEwMTEwMTAgMDExMDExMDEgMDExMTEwMDAgMDExMDEwMDAgMDEwMTEwMTAgMDAxMTAwMTEgMDExMTAxMDAgMDExMTAxMDEgMDEwMTAxMDAgMDAxMTAwMDEgMDEwMTAwMTAgMDExMDAxMTAgMDEwMTAxMDEgMDAxMTAwMTAgMDAxMTEwMDEgMDExMDAxMTAgMDExMDAwMTEgMDExMDEwMTAgMDEwMTAwMTAgMDExMTAxMDEgMDEwMTEwMTAgMDEwMDAxMTEgMDAxMTEwMDEgMDExMTAxMDAgMDEwMTEwMDAgMDAxMTAwMTAgMDExMDAxMTEgMDAxMTAwMTEgMDEwMDExMTAgMDAxMTAwMTEgMDEwMDAwMTAgMDExMDAxMTAgMDExMDAwMTEgMDExMDEwMTAgMDEwMDExMTAgMDExMTEwMDAgMDExMDAxMDAgMDEwMTAxMDAgMDEwMDExMDEgMDAxMTAwMDEgMDExMDAxMDAgMDEwMDEwMDAgMDEwMDExMTAgMDAxMTEwMDE). If you use [CyberChef's Magic](https://gchq.github.io/CyberChef/#recipe=Magic(3,false,false,'')&input=MDEwMTEwMTAgMDExMDExMDEgMDExMTEwMDAgMDExMDEwMDAgMDEwMTEwMTAgMDAxMTAwMTEgMDExMTAxMDAgMDExMTAxMDEgMDEwMTAxMDAgMDAxMTAwMDEgMDEwMTAwMTAgMDExMDAxMTAgMDEwMTAxMDEgMDAxMTAwMTAgMDAxMTEwMDEgMDExMDAxMTAgMDExMDAwMTEgMDExMDEwMTAgMDEwMTAwMTAgMDExMTAxMDEgMDEwMTEwMTAgMDEwMDAxMTEgMDAxMTEwMDEgMDExMTAxMDAgMDEwMTEwMDAgMDAxMTAwMTAgMDExMDAxMTEgMDAxMTAwMTEgMDEwMDExMTAgMDAxMTAwMTEgMDEwMDAwMTAgMDExMDAxMTAgMDExMDAwMTEgMDExMDEwMTAgMDEwMDExMTAgMDExMTEwMDAgMDExMDAxMDAgMDEwMTAxMDAgMDEwMDExMDEgMDAxMTAwMDEgMDExMDAxMDAgMDEwMDEwMDAgMDEwMDExMTAgMDAxMTEwMDE) roughly it's base64 , so if you add it a flag will appear. From Binary & From Base64, `ZmxhZ3tuT1RfU29fcjRuZG9tX2g3N3BfcjNxdTM1dHN9`

```bash
$ echo 'ZmxhZ3tuT1RfU29fcjRuZG9tX2g3N3BfcjNxdTM1dHN9' | base64 -d
$ flag{nOT_So_r4ndom_h77p_r3qu35ts}
```

<details>
  <summary>FLAG :</summary>
  
  > `flag{nOT_So_r4ndom_h77p_r3qu35ts}`
  
</details>
<br>
