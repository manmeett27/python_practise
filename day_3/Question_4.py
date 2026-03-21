'''4. The "Security Audit" (Complex/Double Topic)
Goal: Combine Lists, Tuples, and Sets. This is a very common task in real programming!

The Scenario: You have a list of "Logins" where each login is a Tuple of (Username, IP_Address).

logins = [
    ("user1", "192.168.1.1"),
    ("user2", "10.0.0.5"),
    ("user1", "192.168.1.1"),
    ("admin", "127.0.0.1"),
    ("user2", "10.0.0.5")
]
The Task: 
1.  Create a Set called unique_logins from the logins list. (Python allows sets of tuples because tuples cannot change!).
2.  Loop through the unique_logins set.
3.  For each one, unpack the tuple and print: "User [Name] logged in from [IP]".
4.  Print the total number of unique login events.'''


logins = [
    ("user1", "192.168.1.1"),
    ("user2", "10.0.0.5"),
    ("user1", "192.168.1.1"),
    ("admin", "127.0.0.1"),
    ("user2", "10.0.0.5")
]

unique_logins = sorted(set(logins))

for each_login in unique_logins:
    user, logged_in_from = each_login
    print(f"User '{user}' logged in from '{logged_in_from}'")
print(len(unique_logins))