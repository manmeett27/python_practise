'''1. The "VIP Guest" Filter
Goal: Practice if-else inside a for loop.

Data: guests = ["Alice", "Bob", "Charlie", "David", "Eve"]

Task: Loop through the list. If the name is "Alice" or "Eve", print "[Name] is a VIP!". For everyone else, print "[Name] is a regular guest."

Hint: Use if name == "Alice" or name == "Eve":.'''


guests = ["Alice", "Bob", "Charlie", "David", "Eve"]

for name in guests:
    if name=='Alice' or name=='Eve':
        print(f"{name} is a VIP!")
    else:
        print(f"{name} is a regular guest.")