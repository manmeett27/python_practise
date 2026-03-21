'''4. The "Stock Market" Alert (Complex)
Goal: Combine everything (Lists, Dictionaries, Loops, and Conditions).

Data: A list of dictionaries representing stock prices:

stocks = [
    {"name": "Apple", "price": 150},
    {"name": "Tesla", "price": 800},
    {"name": "Amazon", "price": 3200},
    {"name": "Nokia", "price": 5}
]
Task: Loop through the stocks list.

Task: If the price is above 500, print "SELL [Name]".

Task: If the price is below 10, print "BUY [Name]".

Task: Otherwise, print "HOLD [Name]".'''


stocks = [
    {"name": "Apple", "price": 150},
    {"name": "Tesla", "price": 800},
    {"name": "Amazon", "price": 3200},
    {"name": "Nokia", "price": 5}
]

for item in stocks:
    if item["price"] >500:
        print(f"SELL {item["name"]}")
    elif item["price"]<10:
        print(f"BUY {item["name"]}")
    else:
        print (f"HOLD {item["name"]}")