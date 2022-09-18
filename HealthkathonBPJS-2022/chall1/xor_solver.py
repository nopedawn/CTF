def decrypt(encrypted: bytes, key: bytes):
    result = []
    
    for i in range(len(encrypted)):
        result.append(encrypted[i] ^ key[i % len(key)])

    return bytes(result)
