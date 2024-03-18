HEADER_SIZE = 55  # Size of the BMP header

with open('eWolverine.bmp', 'rb') as f:
    eWolverine = f.read()
with open('eFlag.bmp', 'rb') as f:
    eFlag = f.read()

header = eWolverine[:HEADER_SIZE]

xor = header + bytes(a^b for a, b in zip(eWolverine[HEADER_SIZE:], eFlag[HEADER_SIZE:]))

with open('out.bmp', 'wb') as f:
    f.write(xor)
