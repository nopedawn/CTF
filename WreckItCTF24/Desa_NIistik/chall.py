from secp256k1 import PrivateKey, PublicKey
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
import random
from secret import FLAG

VILLAGE_NAME = b'NIST_VILL'
BASE = len(VILLAGE_NAME)

class villageAuth:
    def __init__(self,):
        self.pubkeys = self.keygen(BASE)

    def serialize(self, pub):
        return pub.public_bytes(serialization.Encoding.X962,serialization.PublicFormat.CompressedPoint)

    def keygen(self, base):
        secret = [random.getrandbits(base*i) for i in range(1,base)]
        secret = [random.getrandbits(base) for i in range(1,base)]
        privs = [ec.derive_private_key(i, ec.SECP256K1()) for i in secret]
        pubs = [self.serialize(i.public_key()).hex() for i in privs]
        return pubs
    
    def verify(self, pub, signature, message):
        pubkey = PublicKey(pub, raw=True)
        sign = PrivateKey().ecdsa_deserialize(signature)
        ver = pubkey.ecdsa_verify(message, sign) & (pubkey.serialize().hex() in self.pubkeys)
        return ver
    
    def getPub(self,):
        return self.pubkeys

def verifySign(village):
    signs = []
    pubs = []
    try:
        for _ in range(2*BASE//3):
            signature = bytes.fromhex(input("Your signature: "))
            pub = bytes.fromhex(input("Your publickey: "))
            valid = village.verify(pub,signature,b'look-at-base')
            if(valid and pub not in pubs and signature not in signs):
                signs.append(signature)
                pubs.append(pub)
            else:
                print("You are not our village members")
                return
        print(FLAG)
    except:
        print("Something error is happen")
        return
    return

def printPubs(village):
    print(village.getPub())
    return

if __name__ == "__main__":
    print("-------------------------------------------")
    print("-                                         -")
    print("-               WELCOME TO                -")
    print("-                   OUR                   -")
    print("-            "+VILLAGE_NAME.decode()+" VILLAGE             -")
    print("-             --------------              -")
    print("-           feel free to use it           -")
    print("-                                         -")
    print("-------------------------------------------")
    inc = 0
    ROvillage = villageAuth()
    while True:
        print("\nDash: ")
        print("1. Verify")
        print("2. Getpub")
        print("3. Exit")
        choosen = input("Your choosen: ").strip()
        if(choosen=='3' or inc==3): break
        elif(choosen=='2'): printPubs(ROvillage)
        elif(choosen=='1'): verifySign(ROvillage)
        else: print("invalid keys")
        inc += 1
    if(inc>2): print("You are a robot!!")
