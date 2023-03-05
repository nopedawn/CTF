## Truth

<details>
  <summary>Deskripsi</summary>

  > Kuronushi traveled far away from his country to learn something about himself. He never sure about his identity. Untill One day, he met a sage who gave him a book of truth. The sage said " To understand about yourself,Erase the title and find the Bigger case" <br>
  > Submit the flag on this format ARA2023{} Separate the sentences with _ <br>
  > [Attachments](./Truth.pdf) <br>
  > Author: Zangetsu#2398

</details>

Diberikan sebuah file pdf berpassword, kita bisa saja membrute-force untuk mendapatkan passwordnya dengan menggunakan tools pdf2john atau John The Ripper

```bash
$ pdf2john Truth.pdf
Truth.pdf:$pdf$4*4*128*-1060*1*16*077e10eba516a741a6285385b42f5b27*32*df507156115f50098c3d8c6fdb1d662200000000000000000000000000000000*32*7a46addd4179a8ab90812ae8876369522d5facc72245be4f28b3559473767d57
```

Kita simpan hasil hash nya ke dalam sebuah file `.hash`

```bash
$ pdf2john Truth.pdf > pdf.hash
```

Lalu gunakan command `john nama_file` untuk crack hashnya menggunakan default wordlist dari library nya

```bash
$ john pdf.hash
Using default input encoding: UTF-8
Loaded 1 password hash (PDF [MD5 SHA2 RC4/AES 32/64])
No password hashes left to crack (see FAQ)
```

Sebelumnya kami sudah meng crack dan mendapatkan passwordnya, kita bisa langsung saja menggunakan parameter `–-show` untuk melihat password yg telah di crack tersimpan

```bash
$ john --show pdf.hash
Truth.pdf:subarukun

1 password hash cracked, 0 left
```

Password untuk membuka file pdfnya yaitu `subarukun`

Sesuai deskripsi soal yaitu kita diminta untuk mencari Letter yang Uppercase dan menghapus titlenya, didapatlah text yang Uppercase berikut `SOUNDSLIKEFANDAGO` kemudian pisahkan dengan `_`

<details>
  <summary>Flag</summary>
  
  > `ARA2023{SOUNDS_LIKE_FANDAGO}`
  
</details>
