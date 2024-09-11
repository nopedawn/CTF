# challenge CRYPTO/Desa NIistik

from pwn import *
import json
from secp256k1 import PrivateKey, PublicKey
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from coincurve import PrivateKey as PrK, PublicKey as PbK, verify_signature
from coincurve.utils import int_to_bytes_padded

io = remote('188.166.247.108', '7043')

def getpub():
    io.recvuntil(b'choosen: ')
    io.sendline(b'2')
    return json.loads(io.recvline().decode().strip().replace('\'','"'))
    
def verify(arr):
    io.recvuntil(b'choosen: ')
    io.sendline(b'1')
    for i,j in arr:
        io.recvuntil(b'signature: ')
        io.sendline(j.hex().encode())
        io.recvuntil(b'publickey: ')
        io.sendline(i.hex().encode())
    flag = io.recvline()
    print(flag)

def verif(pub, sign, message):
    pubkey = PublicKey(pub, raw=True)
    sign = PrivateKey().ecdsa_deserialize(sign)
    ver = pubkey.ecdsa_verify(message, sign)
    return ver

def generatePb(pk, pb_byte):
    pb0 = PbK(pb_byte)
    x,y = pb0.point()
    message = b'look-at-base'
    pbks_byte0 = pb_byte
    cors = int_to_bytes_padded(x)+int_to_bytes_padded(y)
    pbks_byte1 = b'\x04'+cors
    pad = b''
    if(pb_byte[0]==b'\x02'[0]): pad=b'\x06'
    else: pad = b'\x07'
    pbks_byte2 = pad+cors
    p = [pbks_byte0, pbks_byte1, pbks_byte2]
    assert p[0].hex() != p[1].hex() != p[2].hex()
    ret = []
    inc = 0
    while True:
        s = pk.sign(message,ec.ECDSA(hashes.SHA256()),)
        if(verif(p[inc], s, message)):
            ret.append([p[inc], s])
            inc += 1
        if(inc==3): break
        if(inc==100): 
            print("long loop")
            break
    return ret

listPk = []

pubs = getpub()[:3]
for i in range(1, 2**18):
    if(i%10000==1): print(i*100/(2**18))
    pk = ec.derive_private_key(i, ec.SECP256K1())
    pubk = pk.public_key().public_bytes(serialization.Encoding.X962,serialization.PublicFormat.CompressedPoint).hex()
    if(pubk in pubs):
        print("Found")
        print(i)
        print(pubk)
        hasil = generatePb(pk, bytes.fromhex(pubk))
        listPk += hasil
        if(len(listPk)==6): 
            print("Getting the flag")
            break
        
verify(listPk)