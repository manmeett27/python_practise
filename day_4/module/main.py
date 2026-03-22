'''3. The "Math Toolbox" (Creating your own module)
Goal: Practice multi-file organization.

Step 1: Create a file named physics.py. Inside it, define a constant GRAVITY = 9.8 and a function calculate_force(mass) that returns mass * GRAVITY.

Step 2: Create a file named main.py in the same folder.

Step 3: In main.py, import your module and use it to find the force of a 10kg object.

Hint: Use import physics or from physics import calculate_force.'''

import physics

print(physics.calculate_force(10))