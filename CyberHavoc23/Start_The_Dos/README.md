## Start The Dos

<details>
  <summary>Description</summary>
  
  > Leon wants you to be a part of Agents of Havoc. He wants you to understand this software as old as hacking itself so as to fire a DoS Attack against whiterose's targets. Help him before he suspects your intentions.
  
  > Flag Format: CHCTF{}
  
</details>

Given a file named `dosser.s` we can compile it using the following commands:

```bash
$ nasm -f elf32 -o dosser.o dosser.s
$ ld -m elf_i386 -o dosser dosser.o
```

```bash
$ file dosser
dosser: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), statically linked, not stripped
```

After that, we can reverse the dosser ELF file using IDA Disassembler 32 bit. We will find a separate flag in the text segment stored in the `al` register.

<details>
  <summary>Flag</summary>
  
  > `CHCTF{L33T_CR4CK3R_5TR1K3S_4G41N}`
  
</details>
