import itertools

# Define a list of emoticons
emoticons = [":)", ":(", ":D", ":P", ";)", ":|", ":O", "XD"]

# Define alphanumeric characters
alphanumeric = [chr(i) for i in range(ord('a'), ord('z') + 1)] + [str(i) for i in range(10)]

# Set the maximum length for the password
max_length = 4  # Adjust this value for the desired maximum length

# Generate passwords
valid_passwords = []
for length in range(2, max_length + 1):  # Start from length 2
    # Ensure even length to maintain the alternating pattern
    if length % 2 == 0:
        for emoticon_combo in itertools.product(emoticons, repeat=length // 2):
            for alphanum_combo in itertools.product(alphanumeric, repeat=length // 2):
                # Combine emoticons and alphanumeric in alternating order
                password = ''.join(itertools.chain(*zip(emoticon_combo, alphanum_combo)))
                valid_passwords.append(password)

# Save to a wordlist file
with open("wordlist.txt", "w") as f:
    for password in valid_passwords:
        f.write(password + "\n")

print("Wordlist generated: wordlist.txt")
