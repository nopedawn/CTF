from pwn import *

def exploit(io):
    io.recvuntil(b"how can i help?")
    
    payload = b"please" * 39 
    payload += b"pretty" * 15 
    payload += b"flag"
    io.sendline(payload)
    
    # output = io.recvall()
    # print(output)
    io.interactive()

if __name__ == "__main__":
    context.update(log_level='debug')
    try:
        io = remote('chall.lac.tf', 31321)
        exploit(io)
    except:
        io = process('./aplet321')
        exploit(io)
