## Secret Behind a Letter

<details>
  <summary>Deskripsi</summary>

  > Melon and Edith went to an labyrinth and they should break the code written on a letter in a box in order to escape the labyrinth. <br>
  > Open the letter and break the code <br>
  > [Attachments](./Letter.txt) <br>
  > Author: L e n s#1048
  
</details>

Challenge basic RSA yang diberikan <b><i>(p, q, c)</i></b> key yg sudah ada implementasi dari dekripsi RSA untuk mendekripsi encrypted text <b><i>c</i></b> dengan menggunakan private key yang terdiri dari nilai <b><i>(p, q, dan d)</i></b> serta nilai <b><i>(e)</i></b> sebagai private keynya.

```python
from Crypto.Util.number import inverse

p = 12575333694121267690521971855691638144136810331188248236770880338905811883485064104865649834927819725617695554472100341361896162022311653301532810101344273 
q = 12497483426175072465852167936960526232284891876787981080671162783561411521675809112204573617358389742732546293502709585129205885726078492417109867512398747 
c = 36062934495731792908639535062833180651022813589535592851802572264328299027406413927346852454217627793315144892942026886980823622240157405717499787959943040540734122142838898482767541272677837091303824669912963572714656139422011853028133556111405072526509839846701570133437746102727644982344712571844332280218
e = 65537

n = p*q
phi_n = (p-1)*(q-1)
d = inverse(e, phi_n)

m = pow(c, d, n)
print(m.to_bytes((m.bit_length() + 7) // 8, 'big').decode())
```

<details>
  <summary>Flag</summary>
  
  > `ARA2023{1t_turn5_0ut_to_b3_an_rsa}`
  
</details>
