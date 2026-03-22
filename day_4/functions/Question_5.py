'''5. The "Inventory Manager" (The Booster Challenge)
Goal: Combine Functions, Dictionaries, and Logic.

The Data: ```python
player_stats = {"name": "Hero", "health": 100}

The Task: Write a function called take_damage that takes two parameters: stats_dict and amount.

Logic: 
1. Subtract the amount from the "health" value inside the dictionary.
2. If health drops below 0, set it to 0.
3. Return the updated dictionary.

Test: Call take_damage(player_stats, 30) and print the new stats.'''


player_stats = {"name": "Hero", "health": 100}

def take_damage(stats_dict, amount):
    stats_dict["health"] = stats_dict["health"]-amount
    if stats_dict["health"]<0:
        stats_dict["health"] =0
    return stats_dict

print(take_damage(player_stats, 30))
    