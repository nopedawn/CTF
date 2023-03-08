encrypted_text = "001300737173723a70321e3971331e352975351e247574387e3c"
encrypted_bytes = bytes.fromhex(encrypted_text)

for key in range(256):
    decrypted_bytes = bytes([b ^ key for b in encrypted_bytes])
    try:
        decrypted_text = decrypted_bytes.decode('utf-8')
    except UnicodeDecodeError:
        continue

    print(f"Key: {key}, Decrypted text: {decrypted_text}")
