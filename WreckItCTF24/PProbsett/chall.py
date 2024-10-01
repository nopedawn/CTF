from secret import FLAG
from PProbsett import PProbsett
from Crypto.Util.number import *
import random

secretCode = random.randbytes(40).hex()
i_have_secret_contd = f'Im READY for SECURITY code: {secretCode[:40]} buzzing MAKE me code: {secretCode[40:]}'.encode()
secretInt = bytes_to_long(i_have_secret_contd)
RSAfuzzingP = getPrime(1024)
RSAfuzzingQ = getPrime(1024)
RSAfuzzingN = RSAfuzzingP*RSAfuzzingQ
RSAfuzzinge = (secretInt*2020202202020220)*getPrime(1024) | 1
while True:
    try:
        RSAfuzzingd = pow(RSAfuzzinge, -1, (RSAfuzzingP-1)*(RSAfuzzingQ-1))
        break
    except:
        RSAfuzzinge += 2

assert pow(secretInt, RSAfuzzinge*RSAfuzzingd, RSAfuzzingN) == secretInt
print('cipher_number:', pow(secretInt, RSAfuzzinge, RSAfuzzingN))
print(f'pub_value: ({RSAfuzzinge}, {RSAfuzzingN})')

iv = i_have_secret_contd[:40]
cipher = PProbsett(RSAfuzzingd)
while True:
    inp = input("]: ")
    if(inp=='1'):
        answer = input("answer: ")
        if(answer==i_have_secret_contd.decode()):
            print(f"Successfully, and this is your flag: {FLAG}")
        else:
            print(f"You are not our team, access denied.")
            exit(1)
    elif(inp=='2'):
        message = input("message: ")
        hasil = cipher.process(iv + message.encode())
        print(f"ciphertext: {hasil[0]}\nsignature: {hasil[1]}")
    elif(inp=='3'):
        pubs = cipher.public()
        print(f"publickey:\np: {pubs[0]}\nn: {pubs[1]}\ne: {pubs[2]}")
    elif(inp=='4'):
        print("I need some access code for authenticate you")
        inp = input("10 first secretCode: ")
        inp2 = input("10 first selfKey: ")
        if(inp==secretCode[:10] and inp2==cipher.selfKey()[:10]):
            print(f"your enc_nonce: {pow(cipher.getNonce(), 5, RSAfuzzingN)}")
    elif(inp=='exit'):
        exit(1)
    else:
        print("Invalid menu!!")