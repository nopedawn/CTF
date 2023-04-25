message = "43 4F 44 45 01000010 01011001 01111011 167 60 167 137 167 150 60 154 63 137 102 97 109 49 108 121 95 116 48 95 U+67 U+61 U+74 U+68 U+33 U+72 U+7D"
message_list = message.split()

decoded_hex = "".join([chr(int(x, 16)) for x in message_list[0:4]])
decoded_binary = "".join([chr(int(x, 2)) for x in message_list[4:7]])
decoded_octal = "".join([chr(int(x, 8)) for x in message_list[7:17]])
decoded_decimal = "".join([chr(int(x)) for x in message_list[17:27]])
decoded_unicode = "".join([chr(int(x[2:], 16)) for x in message_list[27:]])

flag = decoded_hex + decoded_binary + decoded_octal + decoded_decimal + decoded_unicode
print(flag)