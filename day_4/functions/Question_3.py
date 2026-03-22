'''3. The "Unique Counter" (Functions + Sets)
Goal: Practice using a function to process a collection.

Task: 
Write a function called count_unique that takes a List as an argument.
Logic: Inside the function, convert the list to a Set and return the len() of that set.
Data to test: [1, 2, 2, 3, 3, 3, 4]

Expected Result: 4'''


def count_unique(list = []):
    list_to_set = set(list)
    return len(list_to_set)

Data_to_test= [1, 2, 2, 3, 3, 3, 4, 5]
print(count_unique(Data_to_test))