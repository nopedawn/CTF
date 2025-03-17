import matplotlib.pyplot as plt
import numpy as np

bitstring = open("bitstring.txt", "r").read().strip()

length = len(bitstring)
size = int(length ** 0.5)
grid = 1 - np.array([int(b) for b in bitstring[:size*size]]).reshape((size, size))

plt.imshow(grid, cmap="gray", interpolation="nearest")
plt.axis("off")
plt.savefig("output.png", dpi=300, bbox_inches="tight")