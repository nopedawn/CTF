target = "lfqc~opvqZdkjqm`wZcidbZfm`fn`wZd6130a0`0``761gdx"
correct_input = ""

for char in target:
    correct_input += chr(ord(char) ^ 5)

print(correct_input)
