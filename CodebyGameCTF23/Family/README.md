## Family

<details>
  <summary>Description</summary>
  
  > [null]
  
  > Flag Format: CODEBY{}
  
</details>

Given a challenge [file](./family.txt) containing a message that has been encoded in 5 types of encoding

> hex = `43 4F 44 45` <br>
> 
> binary = `01000010 01011001 01111011` <br>
> 
> octal = `167 60 167 137 167 150 60 154 63 137` <br>
> 
> decimal = `102 97 109 49 108 121 95 116 48 95` <br>
> 
> unicode = `U+67 U+61 U+74 U+68 U+33 U+72 U+7D` <br>

Here's the solver

```python3
message = "43 4F 44 45 01000010 01011001 01111011 167 60 167 137 167 150 60 154 63 137 102 97 109 49 108 121 95 116 48 95 U+67 U+61 U+74 U+68 U+33 U+72 U+7D"
message_list = message.split()

decoded_hex = "".join([chr(int(x, 16)) for x in message_list[0:4]])
decoded_binary = "".join([chr(int(x, 2)) for x in message_list[4:7]])
decoded_octal = "".join([chr(int(x, 8)) for x in message_list[7:17]])
decoded_decimal = "".join([chr(int(x)) for x in message_list[17:27]])
decoded_unicode = "".join([chr(int(x[2:], 16)) for x in message_list[27:]])

flag = decoded_hex + decoded_binary + decoded_octal + decoded_decimal + decoded_unicode
print(flag)
```

<details>
  <summary>Flag</summary>
  
  > `CODEBY{w0w_wh0l3_fam1ly_t0_gath3r}`
  
</details>
