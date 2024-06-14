from pwn import *

p = process('./chall')

gdb.attach(p, '''
    break main
    run
    call (int) win()
''')

flag = p.recv()
print(flag)
