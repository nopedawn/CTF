## "Easy" Volatility

<details>
  <summary>Description</summary>
  
  > I've included the flag in as shell command. Can you retrieve it? <br>
  > I recommend using the [volatility3](https://github.com/volatilityfoundation/volatility3) software for this challenge. <br>
  > Here is the memory dump: [debian11.core.zst](https://utexas.box.com/s/fehluzyox4bbgfjlz061r2k7k2sek3cw) <br>
  > This problem also comes with a free profile! [debian11_5.10.0-21.json.zst](https://utexas.box.com/s/g64kezqvkqhm6nw79oovcekn9z1w66q0) <br>
  > Both of these files are compressed using zstd. <br>
  > This challenge's flag looks like a UUID. <br>
  
  > Note: the volatility challenges do not have a flag format to discourage grepping. They all should be possible without guessing. If you have trouble, remember that you can ask for help. <br>
  
  > By Daniel Parks (@danielp on discord)
  
</details>

We need the symbol table for the corresponding kernel.

```bash
$ ls
debian11.core  debian11.core.zst  debian11_5.10.0-21.json  debian11_5.10.0-21.json.zst
```

As the symbol table in the form of a JSON file is already provided in this challenge, we can simply move it to the directory `/volatility3/symbols`.

```bash
$ mv debian11_5.10.0-21.json /home/nopedawn/.local/lib/python3.10/site-packages/volatility3/symbols
```

Then, we can continue recover the bash command history from memory.

```bash
$ vol -f debian11.core linux.bash
Volatility 3 Framework 2.4.1
Progress:  100.00               Stacking attempts finished
PID     Process CommandTime     Command

467     bash    2023-03-05 18:21:23.000000      # 08ffea76-b232-4768-a815-3cc1c467e813
```

<details>
  <summary>Flag</summary>
  
  > `08ffea76-b232-4768-a815-3cc1c467e813`
  
</details>
