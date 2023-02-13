## crypto/one-more-time-pad

<details>
  <summary>Description</summary>
  
  > I heard the onetime pad is perfectly secure so I used it to send an important message to a friend, but now a UCLA competition is asking for the key? I threw that out a long time ago! Can you help me recover it? <br> [chall.py](./chall.py)
  
</details>

This cryptographic challenge is to encrypt a plain text `Long ago, the four nations lived together in harmony ...`

Then XOR it with hexadecimal key `200e0d13461a055b4e592b0054543902462d1000042b045f1c407f18581b56194c150c13030f0a5110593606111c3e1f5e305e174571431e`

Here's a solver script

```python
plaintext = b"Long ago, the four nations lived together in harmony ..."
ciphertext = bytes.fromhex("200e0d13461a055b4e592b0054543902462d1000042b045f1c407f18581b56194c150c13030f0a5110593606111c3e1f5e305e174571431e")

assert len(plaintext) == len(ciphertext)

for (x,z) in zip(ciphertext,plaintext):
    if chr(x^z) == "}" :
        print(chr(x^z))
        break
    else:
        print(chr(x^z), end="")
```

And this another solver using [CyberChef](https://gchq.github.io/CyberChef/#recipe=XOR(%7B'option':'Hex','string':'200e0d13461a055b4e592b0054543902462d1000042b045f1c407f18581b56194c150c13030f0a5110593606111c3e1f5e305e174571431e'%7D,'Standard',false)&input=TG9uZyBhZ28sIHRoZSBmb3VyIG5hdGlvbnMgbGl2ZWQgdG9nZXRoZXIgaW4gaGFybW9ueSAuLi4)

<details>
  <summary>FLAG</summary>
  
  > `lactf{b4by_h1t_m3_0ne_m0r3_t1m3}`
  
</details>
