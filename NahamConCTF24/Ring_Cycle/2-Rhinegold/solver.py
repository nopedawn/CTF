import random

# The string from the check function
check_string = "cioerosgaenessT   ns k urelh oLdTie heri nfdfR"

# The seed for the random number generator is always 0
seed = 0

# The maximum value that the rand function can return
RAND_MAX = 32767

# Seed the random number generator
random.seed(seed)

# Create a list of indices
indices = list(range(46))

# Shuffle the indices
for i in range(45, 0, -1):
    j = random.randint(0, RAND_MAX) % (i+1)
    indices[i], indices[j] = indices[j], indices[i]

# Use the shuffled indices to rearrange the check string
passphrase = "".join(check_string[indices[i]] for i in range(46))

print("The passphrase is:", passphrase)
