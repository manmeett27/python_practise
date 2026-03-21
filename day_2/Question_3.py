'''3. The "Odd/Even" Counter
Goal: Practice math operators (%) and updating variables in a loop.

Data: numbers = [12, 7, 9, 20, 15, 4, 33]

Task: Create two variables: even_count = 0 and odd_count = 0.

Task: Loop through the numbers. If a number is even, add 1 to even_count. If it's odd, add 1 to odd_count.

Output: Print both totals at the end.'''


numbers = [12, 7, 9, 20, 15, 4, 33]

even_counter = 0
odd_counter = 0

for num in numbers:
    if num%2 == 0:
        even_counter+=1
    else:
        odd_counter+=1
print(f"Total even number are {even_counter} and Total odd number are {odd_counter}")