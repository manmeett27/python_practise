'''1. The "Password Generator" (random & string)
Goal: Use two built-in modules together.

Task: Write a function generate_pass() that creates a random 8-character password.

Modules to use: import random and import string.

Logic: 
1. Combine string.ascii_letters and string.digits into one long string of characters.
2. Use random.choice() inside a loop (or a list comprehension) to pick 8 random characters from that string.
3. Join them into one string and return it.'''


import random
import string

def generate_pass():
    chars =  string.ascii_letters+string.digits
    password = ""
    for i in range(8):
        password += random.choice(chars)
    return password

print(f"This is your password: {generate_pass()}")