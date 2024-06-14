from pwn import *

def xor_decrypt(encrypted_flag, key):
    decrypted_flag = ""
    key_len = len(key)
    for i in range(0, len(encrypted_flag), 2):
        decrypted_char = chr(int(encrypted_flag[i:i+2], 16) ^ ord(key[i//2 % key_len]))
        decrypted_flag += decrypted_char
    return decrypted_flag

conn = remote('challs.bcactf.com', 30119)

# Encrypted flag: 21 0F 0A 15 3F 29 29 6B 13 1C 2C 74 7D 30 5E 50 6E 29 2B 24 19 0C 67 7D 05 54 7C 34 5C 13 32 42 29 62 7B 0F 4E
encrypted_flag_line = conn.recvline().decode()
encrypted_flag = encrypted_flag_line.strip().split(": ")[1].replace(" ", "")

key = "ClkvKOR8JQA1JB731LeGkU7J4d2khDvrOPI63mM7"
flag = xor_decrypt(encrypted_flag, key)

print(flag)
