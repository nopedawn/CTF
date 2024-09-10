import hashlib
from propietary import HORTEX

def find_collision():
    seen_hashes = {}
    
    for i in range(1, 0x1000000):  # You can adjust the range as needed
        # Generate hex value from integer
        hex_value = format(i, '06x')  # Generate a 6-digit hex value
        
        # Compute hash using HORTEX
        hash_value = HORTEX(hex_value)
        
        # Check if this hash has been seen before
        if hash_value in seen_hashes:
            X_hex = seen_hashes[hash_value]
            Y_hex = hex_value
            print(f"Collision found: X_hex = {X_hex}, Y_hex = {Y_hex}, Hash = {hash_value}")
            return X_hex, Y_hex
        else:
            seen_hashes[hash_value] = hex_value
            
    print("No collision found within the specified range.")

if __name__ == "__main__":
    find_collision()
