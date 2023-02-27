## Thinker

<details>
  <summary>Deskripsi</summary>

  > I always overthink about finding other part of myself, can you help me? <br>
  > [Attachments](./confused.png) <br>
  > Author: Zangetsu#2398

</details>

Diberikan sebuah file gambar [confused.png](./confused.png) <br>

Setelah kami cek isi stringnya ternyata setelah diakhir segment `IEND` ada beberapa file berekstensi `.zip` `.txt` dan `.png`

```bash
$ strings confused.png
IEND
        _GV
didyou/UT
=GFV
didyou/e.txtUT
QVJBMjAyM3s=
didyou/find.zipUT
find/UT
HFV/C
find/a.txtUT
35216D706C335F
find/something.zipUT
something/UT
something/s.txtUT
p^GV
something/suspicious.zipUT
4^GV
suspicious/UT
suspicious/y.pngUT
```

Maka dari itu kami mencoba meng-extract menggunakan `binwalk` berikut command ketika meng-extractnya

```bash
$ binwalk -e confused.png

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 720 x 881, 8-bit/color RGB, non-interlaced
6170          0x181A          Zlib compressed data, best compression
321663        0x4E87F         TIFF image data, big-endian, offset of first image directory: 8
321693        0x4E89D         Zip archive data, at least v1.0 to extract, name: didyou/
321758        0x4E8DE         Zip archive data, at least v1.0 to extract, compressed size: 13, uncompressed size: 13, name: didyou/e.txt
321841        0x4E931         Zip archive data, at least v1.0 to extract, compressed size: 10568, uncompressed size: 10568, name: didyou/find.zip
332460        0x512AC         End of Zip archive, footer length: 22
332726        0x513B6         End of Zip archive, footer length: 22
```

Terdapat zipfile `4E89D.zip` berisi folder `didyou` didalamnya, langsung saja di extract lagi

Setelah di extract terdapat zipfile `find.zip` dan juga ada file `e.txt` berisi string base64, jika di decode hasil outputnya `ARA2023{`
```bash
$ echo 'QVJBMjAyM3s=' | base64 -d
ARA2023{
```

Kemudian ada zipfile lagi 🙃 `something.zip` dan juga ada file `a.txt` berisi hexstring jika didecode `5!mpl3_`
```bash
$ python3
>>> bytes.fromhex('35216D706C335F').decode('utf-8')
'5!mpl3_'
>>>
```

lagi-lagi... ada zipfile `suspicious.zip` dan file `s.txt` berisi 8 bits binary didecode hasil didecodenya `C0rrupt3d_`
```bash
$ python3
>>> bin = '01000011 00110000 01110010 01110010 01110101 01110000 01110100 00110011 01100100 01011111'
>>> ascii_str = ''
>>> for i in bin.split():
...     decimal = int(i, 2)
...     ascii_char = chr(decimal)
...     ascii_str += ascii_char
...
>>> print(ascii_str)
C0rrupt3d_
>>>
```

Dan pada zipfile terakhir `suspicious.zip` berisi file gambar `y.png` yang ternyata gambarnya corrupted

Setelah kami cek menggunakan hex editor, berikut hex value segment header yang corrupted
```bash
$ xxd y.png
00000000: 215a 7852 0d0a 1a0a 0000 000d 5252 485c  !ZxR........RRH\
```

File signature dan segment headernya ternyata `!ZxR` yang dimana seharunya `%PNG` dan `RRH\` seharusnya `IHDR`

Berikut perbandingan dengan header png yang normal
```bash
00000000: 8950 4e47 0d0a 1a0a 0000 000d 4948 4452  .PNG........IHDR
```

Kita bisa mengubah file signature 1 bit hex value `21 5a 78 52` menjadi `89 50 5e 52` <br>
Lalu ubah segment header 1 bit hex value `52 52 48 5c` menjadi `49 48 44 52` seperti berikut
```bash
$ hexedit y.png
00000000   89 50 4E 47  0D 0A 1A 0A  00 00 00 0D  49 48 44 52  00 00 02 BD  00 00 00 90  .PNG........IHDR........
```

Setelah diubah file signature dan header gambar kemudian file png dapat di display, pada gambar berisi angka decimal `49 109 52 103 101 53 125` jika di decode hasilnya `_1m4ge5}`

```bash
$ python3
>>> dec = '49 109 52 103 101 53 125'
>>> dec_list = dec.split()
>>> ascii_list = [chr(int(i)) for i in dec_list]
>>> ascii_str = ''.join(ascii_list)
>>> print(ascii_str)
1m4ge5}
>>>
```

<details>
  <summary>Flag</summary>
  
  > `ARA2023{5!mpl3_C0rrupt3d_1m4ge5}`
  
</details>
