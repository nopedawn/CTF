from Crypto.Cipher import AES

key = bytes([0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c])
enc = bytes([0x0f, 0x5f, 0xa3, 0xb9, 0x09, 0x23, 0x71, 0x50, 0xbb, 0x4f, 0x6f, 0x6b, 0x88, 0x1d, 0x96, 0xc2, 0x80, 0x29, 0x5f, 0xe0, 0x71, 0x90, 0x64, 0xa6, 0xe5, 0x35, 0x86, 0x64, 0xb4, 0x0c, 0xcb, 0xb4, 0xd8, 0x23, 0x6f, 0x12, 0x02, 0x54, 0xe2, 0x0b, 0x94, 0x83, 0xde, 0x09, 0xf4, 0x3e, 0x6d, 0x24])

# Initialize AES cipher in ECB mode with the key
cipher = AES.new(key, AES.MODE_ECB)

dec = cipher.decrypt(enc)
print(dec.strip())