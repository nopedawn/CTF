# FORENSICS
<br>

## Vastness of Space

<details>
  <summary>Description :</summary>
  
  > Is space really that empty? <br>
  > [Empty_Space.jpg](./vastness_of_space/Empty_Space.jpg)
  
</details>

Given the image file `Empty_Space.jpg` first You can get the password by checking the metadata by using `Exiftool`

```bash
$ exiftool Empty_Space.jpg
```

here's the password `xp_comment: The password is "BBCTF"`

Use [steghide](https://www.kali.org/tools/steghide/) to extract the embedded text file and enter passphrase as the password you got from exifdata 

```bash
$ steghide extract -sf Empty_Space.jpg
```

Got the [somedata.txt](./vastness_of_space/somedata.txt) then make a script to convert those numbers from `somedata.txt` into an image, here's the python3 script that I've coded

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

Got the result in qr code [output.png](./vastness_of_space/output.png) then scan it

<details>
  <summary>FLAG :</summary>
  
  > `flag{qUiCk_R3sP0nse_c0d3}`
  
</details>
<br>

## Random Requests

<details>
  <summary>Description :</summary>
  
  > I captured these very random http requests. Can you help me decode them? <br>
  > [random_requests.pcapng](./random_requests/random_requests.pcapng)
  
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
flag{nOT_So_r4ndom_h77p_r3qu35ts}
```

<details>
  <summary>FLAG :</summary>
  
  > `flag{nOT_So_r4ndom_h77p_r3qu35ts}`
  
</details>
<br>


## Memory Dump

<details>
  <summary>Description :</summary>
  
  > I was learning powershell when my pc suddenly crashed. Can you retrieve my bash history? <br>
  > [Download link](https://drive.google.com/drive/folders/1igAY42dIA-xrGMLH5_NVdq5nisVG4YLa?usp=share_link)
  
</details>

Given an memory image file named `Memdump.raw`, at the first i was using Volatility 2 but when I check the `imageinfo` to retrieve profile the suggested profile cannot appeared,

Then I switch to Volatility 3, this memory image file can be able to analyze using [Volatility 3](https://www.volatilityfoundation.org/releases-vol3)

Now check with `windows.info` to get an information of memory file

```bash
$ vol -f Memdump.raw windows.info
Volatility 3 Framework 2.4.1
Progress:  100.00               PDB scanning finished
Variable        Value

Kernel Base     0xf8025ea03000
DTB     0x1aa000
Symbols file:///home/nopedawn/.local/lib/python3.10/site-packages/volatility3/symbols/windows/ntkrnlmp.pdb/68A17FAF3012B7846079AEECDBE0A583-1.json.xz
Is64Bit True
IsPAE   False
layer_name      0 WindowsIntel32e
memory_layer    1 FileLayer
KdVersionBlock  0xf8025f612398
Major/Minor     15.19041
MachineType     34404
KeNumberProcessors      1
SystemTime      2022-12-16 10:41:11
NtSystemRoot    C:\Windows
NtProductType   NtProductWinNt
NtMajorVersion  10
NtMinorVersion  0
PE MajorOperatingSystemVersion  10
PE MinorOperatingSystemVersion  0
PE Machine      34404
PE TimeDateStamp        Wed Jun 28 04:14:26 1995
```

To get an information process tree of Powershell

```bash
$ vol -f Memdump.raw windows.pstree
*** 1324        2104    powershell.exe  0xc88f237da080  9       -       1       False   2022-12-16 10:36:27.000000      N/A
```

According to the description of the challenge to find commands executed in Powershell. After some googling, found that the powershell history is stored in a `.txt` file, which specifically in `ConsoleHost_history.txt`

```bash
$ vol -f Memdump.raw windows.filescan | grep "ConsoleHost_history.txt"
0xc88f21961af0.0\Users\bbctf\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt    216
```

After we get the Offset (virtaddr), we can retrieve the `ConsoleHost_history.txt` file with `windows.dumpfiles`

```bash
$ vol -f Memdump.raw windows.dumpfiles --pid 1324 --virtaddr 0xc88f21961af0
Volatility 3 Framework 2.4.1
Progress:  100.00               PDB scanning finished
Cache   FileObject      FileName        Result

DataSectionObject       0xc88f21961af0  ConsoleHost_history.txt file.0xc88f21961af0.0xc88f1e9b5570.DataSectionObject.ConsoleHost_history.txt.dat
```

After extracting, rename the file to make it easier to read, then cat the file

```bash
$ mv file.0xc88f21961af0.0xc88f1e9b5570.DataSectionObject.ConsoleHost_history.txt.dat ConsoleHost_history.txt
$ cat ConsoleHost_history.txt
> $xorkey = bbctf
> $xorkey = "bbctf"
> $aescipherkey = "ByteBandits-CTF Jan 2023"
> $encrypted_flag = "m74/XKCNkHmzJHEPAOHvegV96AOubRnSUQBpJnG4tHg="
```

We must decode the encrypted flag using base64 and then decrypt it using AES ECB mode with the AES cipher key. To obtain the flag we can use CyberChef, and here's the [result](https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true,false)AES_Decrypt(%7B'option':'UTF8','string':'ByteBandits-CTF%20Jan%202023'%7D,%7B'option':'UTF8','string':''%7D,'ECB','Raw','Raw',%7B'option':'Hex','string':''%7D,%7B'option':'Hex','string':''%7D)&input=bTc0L1hLQ05rSG16SkhFUEFPSHZlZ1Y5NkFPdWJSblNVUUJwSm5HNHRIZz0)

<details>
  <summary>FLAG :</summary>
  
  > `flag{V0L@tiLiTy_4_da_w1N}`
  
</details>
<br>


## ImageCeption

<details>
  <summary>Description :</summary>
  
  > "The painter has the universe in his mind and hands." <br>
  > -Leonardo Da Vinci <br>
  > [Download link](https://drive.google.com/drive/folders/1mkC2FP3NHUwANaz2f_ie-pha7L4PtACm?usp=share_link)
  
</details>

Given the memory image of named `imageception.raw`, and I will use Volatility 3 to analysis memory image,

We check the image info with `windows.info` first, it looks like a Windows 10 memory dump. 
```bash
$ vol -f imageception.raw windows.info
Volatility 3 Framework 2.4.1
Progress:  100.00               PDB scanning finished
Variable        Value

Kernel Base     0xf80778a18000
DTB     0x1aa000
Symbols file:///home/nopedawn/.local/lib/python3.10/site-packages/volatility3/symbols/windows/ntkrnlmp.pdb/68A17FAF3012B7846079AEECDBE0A583-1.json.xz
Is64Bit True
IsPAE   False
layer_name      0 WindowsIntel32e
memory_layer    1 FileLayer
KdVersionBlock  0xf80779627398
Major/Minor     15.19041
MachineType     34404
KeNumberProcessors      1
SystemTime      2022-12-16 08:28:29
NtSystemRoot    C:\Windows
NtProductType   NtProductWinNt
NtMajorVersion  10
NtMinorVersion  0
PE MajorOperatingSystemVersion  10
PE MinorOperatingSystemVersion  0
PE Machine      34404
PE TimeDateStamp        Wed Jun 28 04:14:26 1995
```

If we take a look `windows.pstree` there's a process `mspaint.exe` are running, by the challenge description let's just check that process

```bash
$ vol -f imageception.raw windows.pstree
Volatility 3 Framework 2.4.1
Progress:  100.00               PDB scanning finished
PID     PPID    ImageFileName   Offset(V)       Threads Handles SessionId       Wow64   CreateTime      ExitTime
*** 4448        3044    mspaint.exe     0xa08f6e45b080  8       -       1       False   2022-12-16 08:27:45.000000      N/A
```

Then I run `windows.cmdline` to check lists process command line arguments. And there's an `imageception.png` is opened with `mspaint.exe` process
```bash
$ vol -f imageception.raw windows.cmdline`, 
Volatility 3 Framework 2.4.1
Progress:  100.00               PDB scanning finished
PID     Process Args
4448 mspaint.exe "C:\Windows\system32\mspaint.exe" "C:\Users\bbctf\Desktop\imageception.png"
```

Catch the Offset (virtaddr) to retrive that `imageception.png` file with `windows.filescan` to scans for file objects present in a particular windows memory image.
```bash
$ vol -f imageception.raw windows.filescan | grep png
0xa08f6ca23200.0\Users\bbctf\Desktop\imageception.png   216
```

Got the Offset (virtaddr) `0xa08f6ca23200` of `imageception.png` now dump the file
```bash
$ vol -f imageception.raw windows.dumpfiles --pid 4448 --virtaddr 0xa08f6ca23200
Volatility 3 Framework 2.4.1
Progress:  100.00               PDB scanning finished
Cache   FileObject      FileName        Result

DataSectionObject       0xa08f6ca23200  imageception.png        Error dumping file
```

Got the dump result in `.dat` file just change into `.png` extension, and we got the flag [imageception.png](./imageception/imageception.png)
```bash
$ mv file.0xa08f6ca23200.0xa08f6c9d1350.DataSectionObject.imageception.png.dat imageception.png
```

<details>
  <summary>FLAG :</summary>
  
  > `flag{!m@g3_w1tHin_1M4ge}`
  
</details>
<br>
