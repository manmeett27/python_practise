'''2. The "Time to Next Year" (datetime)
Goal: Practice date math and specific imports.

Task: Calculate exactly how many days are left until January 1st, 2027.

Modules to use: from datetime import datetime.

Logic: 
1. Create a variable now = datetime.now().
2. Create a variable new_year = datetime(2027, 1, 1).
3. Subtract now from new_year and print the .days attribute of the result.'''


from datetime import datetime

now = datetime.now()
new_year = datetime(27,1,1)
left = new_year - now
print(f"Time to Next Year : {left.days}")