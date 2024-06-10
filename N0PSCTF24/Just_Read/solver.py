ascii_values = [78, 48, 80, 83, 123, 99, 72, 52, 114, 95, 49, 115, 95, 56, 98, 105, 116, 115, 95, 49, 78, 116, 125]

characters = [chr(value) for value in ascii_values]

flag = ''.join(characters[::-1])

print(flag[::-1])
