'''The Scenario
You are a manager auditing a delivery truck. The truck has multiple crates. Each crate is a dictionary containing a category and a list of items. Each item is a dictionary with a name and a price.

The Data
Copy this exactly into your code:

truck_delivery = [
    {
        "category": "Fruits",
        "items": [
            {"name": "Apple", "price": 1.5},
            {"name": "Mango", "price": 12.0},
            {"name": "Banana", "price": 0.5}
        ]
    },
    {
        "category": "Electronics",
        "items": [
            {"name": "Battery", "price": 5.0},
            {"name": "Luxury Headphones", "price": 550.0},
            {"name": "Cable", "price": 15.0}
        ]
    }
]
The Challenge Task
Write a script that does the following:

Double Loop: Use a for loop to go through each crate in truck_delivery. Then, inside that loop, use another for loop to go through the items in that crate.

The "Luxury" Filter: * If an item costs more than $500, print: [ITEM NAME] is a LUXURY item!

If an item costs between $10 and $500, print: [ITEM NAME] is standard.

If it costs less than $10, don't print anything.

The Math (Tricky Part): * Calculate the Total Value of all items in the truck.

Count how many items in total are under $5 (The "Budget" items).

The Output:

Print the Grand Total Price.

Print the Total Count of Budget Items.'''


truck_delivery = [
    {
        "category": "Fruits",
        "items": [
            {"name": "Apple", "price": 1.5},
            {"name": "Mango", "price": 12.0},
            {"name": "Banana", "price": 0.5}
        ]
    },
    {
        "category": "Electronics",
        "items": [
            {"name": "Battery", "price": 5.0},
            {"name": "Luxury Headphones", "price": 550.0},
            {"name": "Cable", "price": 15.0}
        ]
    }
]
total_value = 0
count_item = 0
for each_crate in truck_delivery:
    for items_in_crate in each_crate["items"]:
        if items_in_crate["price"]>500:
            print(f"{items_in_crate["name"]} is a LUXURY item!")
        elif items_in_crate["price"]>10 and items_in_crate["price"]<500:
            print(f"{items_in_crate["name"]} is standard.")
        if items_in_crate["price"]<5:
            count_item += 1
        total_value += items_in_crate["price"]
        
print(f"The Grand Total Price {total_value} And The Total Count of Budget Items {count_item}")