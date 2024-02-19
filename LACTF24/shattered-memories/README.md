## shattered-memories

<details>
  <summary>Description</summary>
  
  > Author: aplet123 <br>
  > I swear I knew what the flag was but I can't seem to remember it anymore... can you dig it out from my inner psyche?
  
  [shattered-memories](shattered-memories) <br>
</details>

Provided executable binary file  `./shattered-memories`

And here's the decompiled of the main function

```c
undefined8 main(void)

{
  int iVar1;
  size_t sVar2;
  undefined8 uVar3;
  char local_98 [8];
  char acStack_90 [8];
  char acStack_88 [8];
  char acStack_80 [8];
  char acStack_78 [108];
  int local_c;
  
  puts("What was the flag again?");
  fgets(local_98,0x80,stdin);
  strip_newline(local_98);
  sVar2 = strlen(local_98);
  if (sVar2 == 0x28) {
    local_c = 0;
    iVar1 = strncmp(acStack_90,"t_what_f",8);
    local_c = local_c + (uint)(iVar1 == 0);
    iVar1 = strncmp(acStack_78,"t_means}",8);
    local_c = local_c + (uint)(iVar1 == 0);
    iVar1 = strncmp(acStack_80,"nd_forge",8);
    local_c = local_c + (uint)(iVar1 == 0);
    iVar1 = strncmp(local_98,"lactf{no",8);
    local_c = local_c + (uint)(iVar1 == 0);
    iVar1 = strncmp(acStack_88,"orgive_a",8);
    local_c = local_c + (uint)(iVar1 == 0);
    switch(local_c) {
    case 0:
      puts("No, that definitely isn\'t it.");
      uVar3 = 1;
      break;
    case 1:
      puts("I\'m pretty sure that isn\'t it.");
      uVar3 = 1;
      break;
    case 2:
      puts("I don\'t think that\'s it...");
      uVar3 = 1;
      break;
    case 3:
      puts("I think it\'s something like that but not quite...");
      uVar3 = 1;
      break;
    case 4:
      puts("There\'s something so slightly off but I can\'t quite put my finger on it...");
      uVar3 = 1;
      break;
    case 5:
      puts("Yes! That\'s it! That\'s the flag! I remember now!");
      uVar3 = 0;
      break;
    default:
      uVar3 = 0;
    }
  }
  else {
    puts("No, I definitely remember it being a different length...");
    uVar3 = 1;
  }
  return uVar3;
}
```

The function first prompts the user for input. It then checks if the length of the input is 40 characters (0x28 in hexadecimal). If the length is correct, it compares segments of the input with predefined strings. If the length is not correct will returns 1. 
The function seems to be checking if the input matches a specific format or pattern. The correct input would likely result in the function returning 0.

Base on `strcmp` they start with the strings `t_what_f`, `t_means}`, `nd_forge`, `lactf{no`, and `orgive_a`.

```bash
$ ./shattered-memories
What was the flag again?
lactf{not_what_forgive_and_forget_means}
Yes! That's it! That's the flag! I remember now!
```


<details>
  <summary>FLAG</summary>
  
  > `lactf{not_what_forgive_and_forget_means}`
    
</details>
