## SH4-32

<details>
  <summary>Deskripsi</summary>
  
  > Sze received an ecnrypted file and a message containing the clue of the file password from her friend. <br>
  > The clue was a hash value : 9be9f4182c157b8d77f97d3b20f68ed6b8533175831837c761e759c44f6feeb8 <br>
  > Decrypt the file password! <br>
  > [Attachments](./Dictionary.txt) <br>
  > Author: L e n s#1048
  
</details>

Kita diminta untuk men decrypt encrypted text sebuah hash value dengan file text berisi list `Dictionary.txt`

```python3
import hashlib
import codecs

target_hash = '9be9f4182c157b8d77f97d3b20f68ed6b8533175831837c761e759c44f6feeb8'

with open('Dictionary.txt', 'r', encoding='utf-8', errors='ignore') as f:
    passwords = f.readlines()

for password in passwords:
    password = password.strip()
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    if hashed_password == target_hash:
        print(f"Password found: {password}")
        output = password
        break

decoded = codecs.decode(output, 'hex').decode()

print(decoded)
```

Atau kita bisa saja langsung men decode hex value yang ada pada file `Dictionary.txt` maka akan di decode menjadi flag langsung

```python3
$ python3
>>> bytes.fromhex('415241323032337b6834736833645f30525f6e4f545f6834736833647d').decode('utf-8')
'ARA2023{h4sh3d_0R_nOT_h4sh3d}'
>>>
```

<details>
  <summary>Flag</summary>
  
  > `ARA2023{h4sh3d_0R_nOT_h4sh3d}`
  
</details>
