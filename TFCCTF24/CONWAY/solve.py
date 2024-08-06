import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad, pad
from binascii import unhexlify

def generate_next_key(s):
    result = []
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            i += 1
            count += 1
        result.append(f"{count}{s[i]}")
        i += 1
    return ''.join(result)

def main():
    initial = "11131221131211131231121113112221121321132132211331222113112211"
    
    initial = generate_next_key(initial)
    print("First transformation: ", initial)
    
    initial = generate_next_key(initial)
    print("Second transformation: ", initial)
    
    h = hashlib.sha256()
    h.update(str(initial).encode())
    key = h.digest()
    
    cipher_text = "f143845f3c4d9ad024ac8f76592352127651ff4d8c35e48ca9337422a0d7f20ec0c2baf530695c150efff20bbc17ca4c"
    cipher_text_bytes = unhexlify(cipher_text)
    
    cipher = AES.new(key, AES.MODE_ECB)
    flag = unpad(cipher.decrypt(cipher_text_bytes), 16)
    print("Decrypted flag: ", flag.decode())

if __name__ == "__main__":
    main()
