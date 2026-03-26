'''Goal: Creating and inspecting arrays.
1. The "Range" Array: Create a NumPy array of all even integers from 10 to 50.
2. The "Identity" Matrix: Create a $3 \times 3$ identity matrix (a square of zeros with a diagonal of ones).
3. The "Randomizer": Generate an array of 25 random numbers sampled from a standard normal distribution.
4. The "Inspecter": Create a $5 \times 5$ matrix of zeros. Print its shape, size, and data type.'''

import numpy as np

# To get Even number from 10 to 50
even = np.arange(10,50,2)

matrix = np.eye(3,3)

randomizer = np.random.randn(25)

inspector = np.zeros((5,5))
print(f"shape of zeroes: {inspector.shape} size of zeroes: {inspector.size} and data type of zeroes: {inspector.dtype}")