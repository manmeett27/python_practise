'''4. The "Tax Calculator" (Functions + Lists)
Goal: Use a function inside a loop to process multiple items.

Task: 1. Write a function get_tax(price) that returns price * 0.10.
2. Create a list: prices = [100, 250, 50, 900].
3. Loop through the list, call your function for each price, and print: "Price: [price], Tax: [result]".'''


def get_tax(price):
    return price * 0.10

prices = [100, 250, 50, 900]

for price in prices:
    print(f"Price: {price}, Tax: {get_tax(price)}")