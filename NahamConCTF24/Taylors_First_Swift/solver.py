import base64

# Hardcoded string in ASCII values
hardcoded_string = [115, 119, 105, 102, 116, 105, 101, 115, 33]  # "swifties!"

# Hardcoded base64 string
hardcoded_base64 = "FRsIAQ8PVBUVEREIVERbBkURFkUIBxVQVkAYFxJfV0FYVkIVQgo="

# Decode the base64 string
decoded_base64 = base64.b64decode(hardcoded_base64)

# Perform the reverse of the xorEncrypt operation
result = ''.join(chr(decoded_base64[i] ^ hardcoded_string[i % len(hardcoded_string)]) for i in range(len(decoded_base64)))
print(result)
