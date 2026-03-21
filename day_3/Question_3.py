'''3. The "Common Friends" (Set Operations)
Goal: Practice comparing two groups of data.

The Data: * my_favorites = {"Pizza", "Pasta", "Burgers", "Sushi"}

friend_favorites = {"Sushi", "Salad", "Pizza", "Tacos"}

The Task: 
1.  Find the Intersection (What you both like).
2.  Find the Difference (What you like that your friend doesn't).
3.  Find the Union (A master list of every food mentioned between you two).'''


my_favorites = {"Pizza", "Pasta", "Burgers", "Sushi"}

friend_favorites = {"Sushi", "Salad", "Pizza", "Tacos"}

print(my_favorites&friend_favorites)  # Intersection (What you both like)
print(my_favorites-friend_favorites)  # Difference (What you like that your friend doesn't)
print(my_favorites|friend_favorites)  # Union (A master list of every food mentioned between you two)