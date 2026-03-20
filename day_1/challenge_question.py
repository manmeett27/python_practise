'''The Challenge: "The Dragon's Shop"
    You are building a system for a shopkeeper in a fantasy game. The program needs to handle a player's profile, a shop's inventory, and a transaction.

The Requirements:

The Setup (Variables & Dictionary):
    Create a dictionary called player. It should have a name (String), gold (Float), and an inventory (List).
    Start the player with 100.0 gold and an empty inventory.

The Shop (List):
    Create a list called shop_items containing three items: "Health Potion", "Iron Sword", and "Shield".
    
The Input (I/O):
    Ask the user for their character's name and save it to the player dictionary.
    Show the user the shop_items list.
    Ask the user for the price of the item they want to buy (since it’s a magic shop, prices change!).

The Logic (Math & Updates):
    Ask the user which item they want from the list (by index 0, 1, or 2).
    Subtract the price from the player's gold.
    append the chosen item to the player's inventory list.

The Output:
    Print a final receipt using an f-string that shows the player's name, their new gold balance (rounded to 2 decimals), and what is currently in their inventory.'''
    
    
player = {
    "name": "",
    "gold": 100.0,
    "inventory": []
}

shop_items = ["Health Potion", "Iron Sword", "Shield"]

player["name"] = input("Enter your favorite character name: ") 
player_wanted_item_from_the_list = int(input(f"{shop_items}\nEnter [Health Potion] 0, [Iron Sword] 1, [Shield] 2: "))
price_of_item = float(input("Enter it's price: "))
player["gold"] = player["gold"] - price_of_item
player["inventory"].append(shop_items[player_wanted_item_from_the_list])

print(player)
