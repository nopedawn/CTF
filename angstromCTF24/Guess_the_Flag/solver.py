secret_code = '`bugzbnllhuude^un^uid^md`ru^rhfohghb`ou^chu|'
original_input = ''.join(chr(ord(c) ^ 1) for c in secret_code)
print(original_input)
