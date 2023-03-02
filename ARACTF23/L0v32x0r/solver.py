ciphertext = "001300737173723a70321e3971331e352975351e247574387e3c"
key = 65

ciphertext_bytes = bytes.fromhex(ciphertext)

plaintext_bytes = bytes([b ^ key for b in ciphertext_bytes])

plaintext = plaintext_bytes.decode()

print(plaintext)