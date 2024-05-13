import re

ciphertext = 'T0n40g5BG03cmk0D1hr}T{dFe_3g_3buL_5_n0'

def rail_fence_decrypt(ciphertext, rails):
    matrix = [['' for _ in range(len(ciphertext))] for _ in range(rails)]
    idx = 0
    for rail in range(rails):
        p = (rail != 0 and rail != (rails - 1))
        r = rail
        while r < len(ciphertext):
            matrix[rail][r] = '*'
            if p:
                r += 2 * (rails - rail - 1)
            else:
                r += 2 * rail
            p = not p
    r = 0
    for i in range(rails):
        for j in range(len(ciphertext)):
            if matrix[i][j] == '*':
                matrix[i][j] = ciphertext[r]
                r += 1
    plaintext = ''
    for i in range(len(ciphertext)):
        for j in range(rails):
            if matrix[j][i] != '':
                plaintext += matrix[j][i]
    return plaintext

def find_string(plaintext):
    pattern = r'TBTL{.*}'
    match = re.search(pattern, plaintext)
    if match:
        return match.group()
    return None

for rails in range(2, len(ciphertext)):
    plaintext = rail_fence_decrypt(ciphertext, rails)
    found_string = find_string(plaintext)
    if found_string:
        print(f'Key: {rails} \nFlag: {found_string}')
        break
