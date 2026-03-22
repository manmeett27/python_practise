'''4. The "System Info" (os & platform)
Goal: Interact with the operating system.

Task: Write a script that tells the user about their computer.

Modules to use: import os and import platform.

Logic: 
1. Print the current working directory using os.getcwd().
2. Print the Operating System name using platform.system().
3. Print the Python version using platform.python_version().'''


import os
import platform

print(os.getcwd())
print(platform.system())
print(platform.python_version())