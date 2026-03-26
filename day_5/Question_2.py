'''Goal: Moving data around without loops.
1. The "Slicer": Create a $4 \times 4$ matrix with values ranging from 1 to 16.     
    - Extract the middle $2 \times 2$ square.
    - Extract the last column only.
    
2. The "Reshaper": Create a 1D array of 12 elements. Reshape it into a $3 \times 4$ matrix, and then transpose it (swap rows and columns).

3. The "Border" Challenge: Create a $5 \times 5$ matrix of ones. Change the values so that the "border" (edges) are 0 and the inside remains 1.'''

import numpy as np

mat = np.arange(1,17).reshape(4,4)
slicer = mat[1:3, 1:3]
last_col = mat[:,-1]

reshaper = np.arange(12).reshape(3,4)
transpose = reshaper.T

border = np.ones((5,5))
border[1:-1,1:-1] = 0
print(border)