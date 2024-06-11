constants = [
    0xB21E71BA177BBAA7, 0xF2F2DAD7F679BA96, 0xBA32C30AB77BBAF2, 0xCBD3D5C3D1DBD14A,
    0xC9C4C481D848BAC3, 0xBA22B77BBA84C0EF, 0xC0EFC94ABA2AA77B, 0xEF48BAD483DBD384,
    0xBACDC9C284DE81D2, 0x3516A77BBA2EB77B, 0xEA19F2F2F2F23EB7, 0x22F7B644FD3EB779,
    0x3EB779307BB00271, 0xF33EB77122F7A67A, 0xBA621084E93E8F71, 0xD7F6D9BA960AB779,
    0x86F2F2F2DAD7F6D9, 0x313BF2F2F2F21AF7
]

reversed_bytes = bytearray()
for constant in constants:
    bytes_ = constant.to_bytes(8, byteorder='little')
    for b in bytes_:
        reversed_bytes.append(b ^ 0xF2)

print(reversed_bytes)

with open("reversed.bin", "wb") as f:
    f.write(reversed_bytes)
    print("Saved in :", f.name)
