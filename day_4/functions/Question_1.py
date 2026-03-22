'''1. The "Currency Converter" (Basic Return)
Goal: Practice def, return, and basic math.

Task: 
Write a function called to_dollars that takes one parameter (pesos).

Logic: Assume 1 dollar = 20 pesos. The function should return the pesos divided by 20.

Test: Call the function with 400 and print the result. (It should show 20.0).'''


def to_dollars(pesos):
    dollar = 20
    return pesos/dollar

print(f"${to_dollars(400)}")