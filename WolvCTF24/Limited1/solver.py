import random

correct = [189, 24, 103, 164, 36, 233, 227, 172, 244, 213, 61, 62, 84, 124, 242, 100, 22, 94, 108, 230, 24, 190, 23, 228, 24]

# Since the time_cycle is unknown, we need to try all possible values (0-255)
for time_cycle in range(256):
    flag = ""
    for i in range(len(correct)):
        random.seed(i+time_cycle)
        # Reverse the XOR operation to get the original character
        char = correct[i] ^ random.getrandbits(8)
        flag += chr(char)
    # Print only flags with printable characters
    if all(' ' <= c <= '~' for c in flag):
        print(f"time_cycle: {time_cycle}\nflag: {flag} ")
