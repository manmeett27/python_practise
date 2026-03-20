# The "Daily Budget" Calculator

monthly_allowance = float(input("Enter monthly allowance: "))
days_in_month = int(input("Enter no of days in month? "))
daily_budget = monthly_allowance/days_in_month

print(f"You have to spend ${daily_budget} per day.")

if daily_budget<10:
    print("Better save up!")
    
# The "Cool Name" Formatter

first_name = input("Enter your first name:" )
second_name = input("Enter your second name: ")
color = input("Enter your favorite color: ")

print(f"---USER PROFILE: {second_name.upper()}, {first_name.upper()}.\nFAVORITE COLOR: {color.upper()}")

# The "Party Guest" List

guests = []

for i in range(3):
    name = input("Enter your name: ")
    guests.append(name)
    
print(f"You have {len(guests)} people coming to your party!")


# The "Pet Translator"

animals = {
    "dog":"woof",
    "cat": "meow",
    "cow": "moo"}

animal_name = input("Enter animal name: ").lower()

print(f"{animal_name} sounds {animals[animal_name]}")


# The "Logic Boss" (Final Challenge)

hero = {
    "name": "",
    "health": 100,
    "inventory": ["Bread", "torch"]
}

name = input("Enter your name: ")
hero["name"] = name

inventory = input("Enter your weapon: ")
hero["inventory"].append(inventory)

hero["health"] = hero["health"] - 15

print(hero)