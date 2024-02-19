## shattered-memories

<details>
  <summary>Description</summary>
  
  > Author: kaiphait <br>
  > Unlike Aplet123, Aplet321 might give you the flag if you beg him enough.
  
  [Dockerfile](Dockerfile) <br>
  [aplet321](aplet321)
</details>

Provided executable binary file `./aplet321`

And here's the decompiled of the main function

```c
undefined8 main(void)

{
  int iVar1;
  size_t sVar2;
  char *pcVar3;
  int iVar4;
  int iVar5;
  char local_238;
  char acStack_237 [519];
  
  setbuf(stdout,(char *)0x0);
  puts("hi, i\'m aplet321. how can i help?");
  fgets(&local_238,0x200,stdin);
  sVar2 = strlen(&local_238);
  if (5 < sVar2) {
    iVar4 = 0;
    iVar5 = 0;
    pcVar3 = &local_238;
    do {
      iVar1 = strncmp(pcVar3,"pretty",6);
      iVar5 = iVar5 + (uint)(iVar1 == 0);
      iVar1 = strncmp(pcVar3,"please",6);
      iVar4 = iVar4 + (uint)(iVar1 == 0);
      pcVar3 = pcVar3 + 1;
    } while (pcVar3 != acStack_237 + ((int)sVar2 - 6));
    if (iVar4 != 0) {
      pcVar3 = strstr(&local_238,"flag");
      if (pcVar3 == (char *)0x0) {
        puts("sorry, i didn\'t understand what you mean");
        return 0;
      }
      if ((iVar5 + iVar4 == 0x36) && (iVar5 - iVar4 == -0x18)) {
        puts("ok here\'s your flag");
        system("cat flag.txt");
        return 0;
      }
      puts("sorry, i\'m not allowed to do that");
      return 0;
    }
  }
  puts("so rude");
  return 0;
}
```

It first prints a greeting message, then reads a line of input from the user. If the input length is more than 5 characters, it checks for the occurrence of the words `pretty` and `please` in the input. If the word `please` is found, it further checks for the word `flag`. If `flag` is also found and the sum of the occurrences of `pretty` and `please` equals 54 (`0x36` in hexadecimal) and the difference between the occurrences of `pretty` and `please` equals -24 (`-0x18` in hexadecimal), it prints a message and executes the command `cat flag.txt`. If these conditions are not met, it prints a refusal message. If the input length is 5 characters or less, it prints a message indicating that the user is being rude. The function returns 0 before it ends.


`solver.py` <br>
```py
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
```


In order to exploit. The payload consists of the word `please` repeated 39 times, `pretty` repeated 15 times, and `flag`. This payload is designed to satisfy the conditions in the C program for printing the flag: the sum of the occurrences of `pretty` and `please` equals 54 (0x36 in hexadecimal) and the difference between the occurrences of `pretty` and `please` equals -24 (-0x18 in hexadecimal). After sending the payload

```bash
$ python3 solver.py
[+] Opening connection to chall.lac.tf on port 31321: Done
[DEBUG] Received 0x22 bytes:
    b"hi, i'm aplet321. how can i help?\n"
[DEBUG] Sent 0x149 bytes:
    b'pleasepleasepleasepleasepleasepleasepleasepleasepleasepleasepleasepleasepleasepleasepleasepleasepleasepleasepleasepleasepleasepleasepleasepleasepleasepleasepleasepleasepleasepleasepleasepleasepleasepleasepleasepleasepleasepleasepleaseprettyprettyprettyprettyprettyprettyprettyprettyprettyprettyprettyprettyprettyprettyprettyflag\n'
[*] Switching to interactive mode

[DEBUG] Received 0x14 bytes:
    b"ok here's your flag\n"
ok here's your flag
[DEBUG] Received 0x35 bytes:
    b"lactf{next_year_i'll_make_aplet456_hqp3c1a7bip5bmnc}\n"
lactf{next_year_i'll_make_aplet456_hqp3c1a7bip5bmnc}
[*] Got EOF while reading in interactive
$
[*] Interrupted
[*] Closed connection to chall.lac.tf port 31321
```



<details>
  <summary>FLAG</summary>
  
  > `lactf{not_what_forgive_and_forget_means}`
    
</details>
