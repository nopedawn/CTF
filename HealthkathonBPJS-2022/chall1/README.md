# CHALL 1
## http://pentest.student.1337hackathon.id:81/

![logo](https://raw.githubusercontent.com/nopedawn/CTF/main/HealthkathonBPJS-2022/chall1/images/chall1_webpage.png)

Diberikan sebuah soal nomor 1 berupa webpage berikut, setelah itu kami cari tahu view page sourcenya seperti berikut

<img src="images/image1.png" width="800">

Kemudian kami menemukan clue pada saat kami meng-inspect halamannya, yaitu berupa strings base64
```
RGVjb2RlIHBhcnQ1IGJ5IHVzaW5nIHRoZSBYT1IgZnVuY3Rpb24gd2l0aCBjdXN0b20gY3NzIG51bWJlci4=
```
<img src="images/image2.png" width="800">

Setelah kami decode hasilnya seperti berikut
```bash
$ echo 'RGVjb2RlIHBhcnQ1IGJ5IHVzaW5nIHRoZSBYT1IgZnVuY3Rpb24gd2l0aCBjdXN0b20gY3NzIG51bWJlci4=' | base64 --decode
```

<img src="images/image3.png" width="1000">

Singkat cerita kami coba menggunakan ```curl``` dengan parameter ```-v``` untuk mencari informasi dari URL-nya, dan kami menemukan potongan flag berupa Hexadecimal
```bash
$ curl -v http://pentest.student.1337hackathon.id:81/
```

<img src="images/image4.png" width="1000">

Setelah itu kami coba decode dari format Hexadecimal to ASCII dengan tools <i>https://www.rapidtables.com/convert/number/hex-to-ascii.html</i>
Didapatkanlah Flag <b>Part1</b> s/d <b>Part4</b> nya yaitu, ```BPJS{Mel4y4ni_s3penuh_h4t!_m3l4mp4u1```
dan tinggal sisa <b>Part5</b> dari flagnya yaitu ```%y?y=,#}```

Sesuai dengan cluenya yaitu <b><i>“Decode part5 by using the XOR function with custom css number.”</i></b>
maka dari itu kami mencari script untuk memecahkan XOR function dengan custom css number dan menemukan script dari web berikut <i>https://crypto.stackexchange.com/questions/98727/how-can-i-decode-a-xor-cipher-with-a-string-key-i-know</i>

Berikut script Python-nya
```python
def decrypt(encrypted: bytes, key: bytes):
    result = []
    
    for i in range(len(encrypted)):
        result.append(encrypted[i] ^ key[i % len(key)])

    return bytes(result)
```

Lalu kami jalankan dengan command ```python3 -i xor_solver.py``` dan didapatkanlah <b>Part5</b> dari Flagnya yaitu ```h4r4pan```
```bash
$ python3 -i xor_solver.py
>>> encrypted = b"%y?y=,#"
>>> key = bytes([77])
>>> decrypt(encrypted, key)
```

<img src="images/image5.png" width="300">

## FLAG
```FLAG : BPJS{Mel4y4ni_s3penuh_h4t!_m3l4mp4u1_h4r4pan}```
