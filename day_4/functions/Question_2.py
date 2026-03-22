'''2. The "Username Cleaner" (Default Parameters)
Goal: Practice string manipulation and default arguments.

Task: 
Write a function called make_handle that takes a name and a suffix.
Requirement: Set the default value of suffix to "99".
Logic: The function should return the name in lowercase plus the suffix.

Test: 
1. Call it with just "Alex". (Result: "alex99")
2. Call it with "Alex" and "2026". (Result: "alex2026")'''


def make_handle(name, suffix = 99):
    return print(f"{name.lower()}{suffix}")

make_handle("Alex")
make_handle("Alex", 2026)