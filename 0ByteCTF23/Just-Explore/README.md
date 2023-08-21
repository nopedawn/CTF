## Just Explore

<details>
  <summary>Deskripsi</summary>
  
  > Just explore and find a vulnerability innit :)
  >
  > http://0x7e7ctf.zerobyte.me:49723/
  >
  > Author: novran
  
</details>

<br/>

![1](img/1.png)

Diberikan sebuah challenge web yang disuruh menuju ke halaman (endpoint) explorer

![2](img/2.png)

![3](img/3.png)

![4](img/4.png)

<br/>

Saya menemukan pada Tech Stack terdapat nginx. Kemudian saya mencoba mengutak-atik pada url-nya, dan ditemukan bahwa web ini vulnerable dengan Directory Traversal / Path Traversal setelah saya coba akses

http://0x7e7ctf.zerobyte.me:49723/explore../

![5](img/5.png)

<br/>

Ini terjadi ketika kesalahan konfigurasi pada nginx (alias) apabila mengakses directory yang di sisipkan `../` pada directory `/exprore../`

https://labs.hakaioffsec.com/nginx-alias-traversal/

<br/>

Tinggal kita cari flagnya saja, ada di http://0x7e7ctf.zerobyte.me:49723/explore../usr/share/

![6](img/6.png)

```bash
curl http://0x7e7ctf.zerobyte.me:49723/explore../usr/share/flag.txt
```

![7](img/7.png)

<br/>

<details>
  <summary>Flag</summary>
  
  > `0byteCTF{P4th_Tr4v3rS4L_ThRu_Ng1nX_M1sC0nf1g_4l14s}`
  
</details>
