## Secret Behind a Letter

<details>
  <summary>Deskripsi</summary>
  
  > Vonny and Zee were having a treasure hunt game until they realized that one of the clues was a not alike the other clues as it has a random text written on the clue. <br>
  > The clue was "001300737173723a70321e3971331e352975351e247574387e3c". <br>
  > Help them to find what the hidden clue means! <br>
  > Author: L e n s#1048
  
</details>

Penyelesaian, kita diminta untuk men decrypt encrypted text yang diberikan, tanpa XOR key nya, kita bisa saja mem brute-force kemungkinan range **0-256** key

```python3
encrypted_text = "001300737173723a70321e3971331e352975351e247574387e3c"
encrypted_bytes = bytes.fromhex(encrypted_text)

for key in range(256):
    decrypted_bytes = bytes([b ^ key for b in encrypted_bytes])
    decrypted_text = decrypted_bytes.decode('utf-8')
    print(f"Key: {key}, Decrypted text: {decrypted_text}")
```

Maka didapatlah key yang cocok yaitu **65**

<details>
  <summary>Flag</summary>
  
  > `ARA2023{1s_x0r_th4t_e45y?}`
  
</details>
