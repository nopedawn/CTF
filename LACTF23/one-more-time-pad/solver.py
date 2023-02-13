plaintext = b"Long ago, the four nations lived together in harmony ..."
ciphertext = bytes.fromhex("200e0d13461a055b4e592b0054543902462d1000042b045f1c407f18581b56194c150c13030f0a5110593606111c3e1f5e305e174571431e")

assert len(plaintext) == len(ciphertext)

for (x,z) in zip(ciphertext,plaintext):
    if chr(x^z) == "}" :
        print(chr(x^z))
        break
    else:
        print(chr(x^z), end="")