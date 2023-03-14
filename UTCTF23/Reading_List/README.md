## Reading List

<details>
  <summary>Description</summary>
  
  > I created this binary to keep track of some strings that I want to read. I thought I put a CTF flag in it so I'll remember to make a problem for UTCTF, but I can't seem to find it... 
  
  > By Caleb (@eden.caleb.a#6541 on Discord)
  
</details>

The command `strings readingList | grep "utflag"` is used to extract strings from the file `readingList`, then search for strings that contain the keyword `"utflag"` in the resulting string output.

```bash
$ strings readingList | grep "utflag"
utflag{string_theory_is_a_cosmological_theory_based_on_the_existence_of_cosmic_strings}
```

`strings` is a command used to extract and print sequences of characters that are readable as strings from a given file input. In this case, `readingList` is the file from which the strings will be extracted.

<details>
  <summary>Flag</summary>
  
  > `utflag{string_theory_is_a_cosmological_theory_based_on_the_existence_of_cosmic_strings}`
  
</details>