## rev/string-cheese

<details>
  <summary>Description</summary>
  
  > I'm something of a cheese connoisseur myself. If you can guess my favorite flavor of string cheese, I'll even give you a flag. Of course, since I'm lazy and socially inept, I slapped together a program to do the verification for me.
  
  > Connect to my service at `nc lac.tf 31131`
  
  > Note: The attached binary is the exact same as the one executing on the remote server. <br> [string_cheese](./string_cheese)
  
</details>

When the program is run it will ask for a password, by the challenge name it's `string` then we can check that there is a string stored in the program

I'm using IDA Disassembler to analyze the given binary-elf file, and get the string value `blueberry` to answering that's input statement, or you can just use `strings` command

```bash
$ nc lac.tf 31131
What's my favorite flavor of string cheese? blueberry
...how did you know? That isn't even a real flavor...
Well I guess I should give you the flag now...
lactf{d0n7_m4k3_fun_0f_my_t4st3_1n_ch33s3}
```

<details>
  <summary>FLAG</summary>
  
  > `lactf{d0n7_m4k3_fun_0f_my_t4st3_1n_ch33s3}`
  
</details>
