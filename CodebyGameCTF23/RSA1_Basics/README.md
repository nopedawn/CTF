## RSA 1 Basics

<details>
  <summary>Description</summary>
  
  > [null]
  
  > Flag Format: CODEBY{}
  
</details>

Given a cryptography challenge with a zip file containing [data.txt](./data.txt) and [flag.txt](./flag.txt), where we have to decrypt the message in `flag.txt` using the given exponent key `n`, `e`, and `p`.

To implement of RSA decryption algorithm that reads in the modulus `n`, the public exponent `e`, and the prime factor `p` of `n` from the given values. Also imports a function inverse from an external library that calculates the modular multiplicative inverse of two numbers.

Calculates the other prime factor `q` of `n` by dividing `n` by `p`, then computes the private key `d` using the modular multiplicative inverse function by passing `e` and `(p-1)*(q-1)` as inputs.

```python3
from Crypto.Util.number import inverse, long_to_bytes

# nilai yang diberikan
n = 17821369821197224755204170576717386974772583796320656477539620911939396151906969461959183978640937853223745304126597764393313271455282077396239424618606794404260667285392141808188728083834584927026023081706807877287176411455869333099599758756680824930296103562451364106123092367375221182676628604366038187928496804145884268753169728377208516981412594946003622745692274230506436281885419071635199138875290167920431573351256816462603222296067133230212113705435433321977478320363027010331451497317278086877300977556100259644050343025778299297465892385900238472919994896492369105460841980012051688350169675505544039420123
e = 65537
p = 1972000550284100445870121306958622830045225641252954033009593459446242613031033375213304073309426202713792319087153903001608198707751563017341316136191257392659269749490809852144061763170826581018719515204465050487987949598939979468867872704976528393610305938567746277939323612907052468216732931923001246346805966071415508727723

# menghitung q
q = n // p

# menghitung d
d = inverse(e, (p-1)*(q-1))

# membaca pesan dari file
with open('flag.txt', 'rb') as f:
    ciphertext = f.read()

# mendekripsi pesan
plaintext = pow(int.from_bytes(ciphertext, 'big'), d, n)

# mencari string yang dimaksud dan hanya mencetak string tersebut dan seterusnya
decoded_text = long_to_bytes(plaintext).decode('latin-1')
flag_start = decoded_text.find("CODEBY")
print(decoded_text[flag_start:])
```

<details>
  <summary>Flag</summary>
  
  > `CODEBY{1_know_th4T_I5_The_HARD3sT_t4SK_YOu'wE_ev3R_SeeN}`
  
</details>
