import hashlib
import codecs

# Assign nilai hash langsung ke dalam variable
target_hash = '9be9f4182c157b8d77f97d3b20f68ed6b8533175831837c761e759c44f6feeb8'

# Baca daftar kata sandi dari file
with open('Dictionary.txt', 'r', encoding='utf-8', errors='ignore') as f:
    passwords = f.readlines()

# Coba semua kata sandi
for password in passwords:
    password = password.strip()
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    if hashed_password == target_hash:
        print(f"Password found: {password}")
        output = password
        break

# Decode dari hex ke string
decoded = codecs.decode(output, 'hex').decode()

# Print hasil decode
print(decoded)
