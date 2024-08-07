import base64

# Garbled text
garbled_text = "楣瑦筴栴瑟楳渷彣桩渳獥"

# Convert the garbled text to bytes
bytes_text = garbled_text.encode('utf-8')

# Decode the bytes as Base64
try:
    decoded_bytes = base64.b64decode(bytes_text)
    decoded_text = decoded_bytes.decode('utf-8')
    print(decoded_text)
except Exception as e:
    print(f"Error decoding Base64: {e}")
