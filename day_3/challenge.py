'''The Scenario
You are cleaning up a messy database of flight bookings. Some people booked twice by mistake, and some data is incomplete. You need to create a "Master List" of unique, valid trips.

The Data
Copy this list of "Raw Bookings" into your code:

# Each booking is a Tuple: (Passenger_Name, Destination, Price)
raw_bookings = [
    ("Alice", "Paris", 800),
    ("Bob", "Tokyo", 1200),
    ("Alice", "Paris", 800),   # Duplicate!
    ("Charlie", "London", 500),
    ("Alice", "London", 450),  # Different trip, same person
    ("Bob", "Tokyo", 1200)     # Duplicate!
]
The Challenge Tasks
The "Uniqueness" Filter: * Use a Set to automatically remove the duplicate bookings.

Hint: Since the bookings are Tuples, Python allows them to be put into a Set because they are "hashable" (immutable).

The "Data Extraction" (Tricky):

Create a new empty Set called unique_destinations.

Loop through your unique bookings and add only the Destination name to this new set.

The "Price Update" (The Most Tricky Part):

You want to create a final List of all unique bookings, but there's a catch: All "Paris" flights just got a $50 discount.

Remember: You cannot change a Tuple. To "update" the price, you must unpack the old tuple and create a new one with the discounted price.

The Final Output:

Print the total number of Unique Destinations found.

Print your final List of updated bookings.'''


raw_bookings = [
    ("Alice", "Paris", 800),
    ("Bob", "Tokyo", 1200),
    ("Alice", "Paris", 800),   # Duplicate!
    ("Charlie", "London", 500),
    ("Alice", "London", 450),  # Different trip, same person
    ("Bob", "Tokyo", 1200)     # Duplicate!
]

clean_bookings_data = set(raw_bookings)

unique_destinations = set()
for name, destination, price in clean_bookings_data:
    unique_destinations.add(destination)
    
final_list = []
for name, destination, price in clean_bookings_data:
    if destination == 'Paris':
        new_price = price - 50
        updated=(name,destination,new_price)
        final_list.append(updated)
    else:
        final_list.append((name,destination,price))
    
# print(final_list)
# print(unique_destinations)