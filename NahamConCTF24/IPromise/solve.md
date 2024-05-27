gdb ./IPromise

b decryptIPromise
run

## Inspect the key at xmmword_4022B0
`x/16xb 0x4022B0`

## Inspect the encrypted data
`x/64xb &encrypted` or `x/64xb 0x404040`
