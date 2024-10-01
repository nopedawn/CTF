from sage.all import Integer, GF, gcd
import random
from Crypto.Util.number import getPrime, bytes_to_long, long_to_bytes
from secret import tets
import hashlib

class PProbsett:
    def __init__(self, secret):
        self.p = getPrime(512)
        self.k = secret % self.p
        self.nonce = secret // self.p
        self.R = GF(self.p)['x']
        p1 = self.R.irreducible_element(Integer(random.randint(5,8)), algorithm="random")
        q1 = self.R.irreducible_element(Integer(random.randint(5,8)), algorithm="random")
        self.n = p1*q1
        self.teta = tets(self.k, self.p, p1, q1, self.n)
        self.e = random.randint(0, self.teta)
        while gcd(self.e, self.teta) != 1:
            self.e += 1

    def encrypt(self, message):
        mess = self.R('x + '+str(message))
        enc = pow(mess, self.e, self.n)
        return enc

    def sign(self, message, enc):
        k = random.getrandbits(500)
        digest = int(hashlib.sha256(message).hexdigest(), 16)
        buff = int(hashlib.sha256(enc).hexdigest(), 16)
        sign = -(k + (buff * digest * self.k) + (self.nonce%(2**256))) % self.p
        self.nonce += 1
        return sign
    
    def pad(self, message):
        return message + b'\x00'*(32 - (len(message)%32))

    def process(self, message):
        pad_message = self.pad(message)
        ciphertext = [self.encrypt(bytes_to_long(pad_message[i:i+32])) for i in range(0, len(pad_message), 32)]
        signature = self.sign(pad_message, str(ciphertext).encode())
        return [ciphertext, hex(signature)[2:]]
    
    def public(self,):
        return self.p, self.n, self.e

    def getNonce(self, ):
        return self.nonce

    def selfKey(self, ):
        return hashlib.sha256(long_to_bytes(self.k)).hexdigest()