## One Time Password

<details>
  <summary>Deskripsi</summary>

  > bwoah, some innovative challenges <br>
  > [Attachments](./one_time_password.txt) <br>
  > Author: circlebytes#5520
  
</details>

Diberikan sebuah chall crypto xor dengan A, B key dan xor key ber-value hexadecimal
yang mana bisa gunakan untuk mendapatkan flagnya

Sebenarnya jika kita decode XOR key, maka kita langsung dapat flagnya

```bash
$ python3
>>> bytes.fromhex('415241323032337b7468335f705f3574346e64355f6630725f7034647a7a7d').decode('ascii')
'ARA2023{th3_p_5t4nd5_f0r_p4dzz}'
>>>
```


<details>
  <summary>Flag</summary>
  
  > `ARA2023{th3_p_5t4nd5_f0r_p4dzz}`
  
</details>
