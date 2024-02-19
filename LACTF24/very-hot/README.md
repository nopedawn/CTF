## very-hot

<details>
  <summary>Description</summary>

  > Author: Red Guy
  > I didn't think that using two primes for my RSA was sexy enough, so I used three. <br> 
  
  [src.py](src.py)
  [out.txt](out.txt)
</details>

Provided chall source `src.py` <br>
```py
from Crypto.Util.number import getPrime, isPrime, bytes_to_long
from flag import FLAG

FLAG = bytes_to_long(FLAG.encode())

p = getPrime(384)
while(not isPrime(p + 6) or not isPrime(p + 12)):
    p = getPrime(384)
q = p + 6
r = p + 12

n = p * q * r
e = 2**16 + 1
ct = pow(FLAG, e, n)

print(f'n: {n}')
print(f'e: {e}')
print(f'ct: {ct}')
```


`out.txt` <br>
```
n: 10565111742779621369865244442986012561396692673454910362609046015925986143478477636135123823568238799221073736640238782018226118947815621060733362956285282617024125831451239252829020159808921127494956720795643829784184023834660903398677823590748068165468077222708643934113813031996923649853965683973247210221430589980477793099978524923475037870799
e: 65537
ct: 9953835612864168958493881125012168733523409382351354854632430461608351532481509658102591265243759698363517384998445400450605072899351246319609602750009384658165461577933077010367041079697256427873608015844538854795998933587082438951814536702595878846142644494615211280580559681850168231137824062612646010487818329823551577905707110039178482377985
```

The provided Python script is implementing a basic RSA encryption scheme with a twist. It generates a prime number `p` and ensures that `p+6` and `p+12` are also prime, assigning these to `q` and `r` respectively. The product of `p`, `q`, and `r` forms the RSA modulus `n`. The public exponent `e` is set to `2^16 + 1`, a common choice in RSA systems. The script then converts a secret flag into a long integer and encrypts it using RSA, resulting in the ciphertext `ct`. The output file contains the values of `n`, `e`, and `ct`, which are part of the public key and the encrypted message in the RSA encryption scheme.


`solver.py` <br>
```
from sympy import nextprime, root
from Crypto.Util.number import long_to_bytes

def factorize(n):
    p = nextprime(int(root(n, 3)))
    while n % p != 0:
        p = nextprime(p)
    n //= p
    q = nextprime(p)
    while n % q != 0:
        q = nextprime(q)
    r = n // q
    return p, q, r

def decrypt(ct, p, q, r, e):
    phi = (p - 1) * (q - 1) * (r - 1)
    d = pow(e, -1, phi)
    return pow(ct, d, n)

n = 10565111742779621369865244442986012561396692673454910362609046015925986143478477636135123823568238799221073736640238782018226118947815621060733362956285282617024125831451239252829020159808921127494956720795643829784184023834660903398677823590748068165468077222708643934113813031996923649853965683973247210221430589980477793099978524923475037870799
e = 65537
ct = 9953835612864168958493881125012168733523409382351354854632430461608351532481509658102591265243759698363517384998445400450605072899351246319609602750009384658165461577933077010367041079697256427873608015844538854795998933587082438951814536702595878846142644494615211280580559681850168231137824062612646010487818329823551577905707110039178482377985

p, q, r = factorize(n)
flag = decrypt(ct, p, q, r, e)
print(long_to_bytes(flag))
```

To decrypt an RSA-encrypted message. It first factorizes the RSA modulus `n` into its prime factors `p`, `q`, and `r` using a function called `factorize`. This function exploits the fact that `p`, `q`, and `r` are close together, which allows for efficient factorization. Then uses these factors to compute the RSA private key and decrypt the ciphertext `ct` using a function called `decrypt`. The decrypted message is converted back to bytes and printed out, revealing the original message.

```bash
$ python3 solver.py
b'lactf{th4t_w45_n0t_so_53xY}'
```

<details>
  <summary>FLAG</summary>
  
  > `lactf{th4t_w45_n0t_so_53xY}`
    
</details>
