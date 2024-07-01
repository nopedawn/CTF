import hashlib
from Crypto.Cipher import AES 
from Crypto.Util.Padding import unpad
from ecpy.curves import * # Assuming you have the same library
from base64 import b64decode

# Given parameters
curve = Curve.get_curve(13, 245, 335135809459196851603485825030548860907)
point = Point(14592775108451646097, 237729200841118959448447480561827799984, curve)

# Recover the shared secret
shared_secret = (point * 1337).x

# Generate the AES key from the shared secret
sha1 = hashlib.sha1()
sha1.update(str(shared_secret).encode('ascii'))
key = sha1.digest()[:16]

# Given ciphertext and IV
ciphertext = b64decode('SllGMo5gxalFG9g8j4KO0cIbXeub0CM2VAWzXo3nbIxMqy1Hl4f+dGwhM9sm793NikYA0EjxvFyRMcU2tKj54Q==')
iv = b64decode('MWkMvRmhFy2vAO9Be9Depw==')

# Decrypt the flag
cipher = AES.new(key, AES.MODE_CBC, iv)
plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)

print("Flag: ", plaintext.decode('ascii'))
