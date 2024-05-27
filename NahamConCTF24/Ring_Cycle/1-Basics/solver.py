import subprocess

def reverse_check(s):
    s = list(s)
    for k in range(0, 47, 2):
        s[k], s[k + 1] = s[k + 1], s[k]
    s = ''.join(s)
    s = s[1:] + s[0]
    s = s[::-1]
    s = s[1:] + s[0]
    return s

passphrase = reverse_check("eyrnou jngkiaccre af suryot arsto  tdyea rre aouY")
print(passphrase)

subprocess.run(['./basics'], input=passphrase, text=True)
