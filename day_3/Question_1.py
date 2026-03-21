'''1. The "Duplicate Destroyer" (Sets)
Goal: Practice removing duplicates and checking for items.

The Data: raw_emails = ["abc@gmail.com", "xyz@yahoo.com", "abc@gmail.com", "hello@me.com", "xyz@yahoo.com"]

The Task: 
1.  Convert the list into a Set to remove the duplicates.
2.  Check if "admin@company.com" is in your new set. If not, add it.
3.  Print the final count of unique emails using len().'''


raw_emails = ["abc@gmail.com", "xyz@yahoo.com", "abc@gmail.com", "hello@me.com", "xyz@yahoo.com"]

for email in raw_emails:
    if email != "admin@company.com":
        raw_emails.append("admin@company.com")
        
clean_emails = list(set(raw_emails))

print(f"Total number of emails {len(clean_emails)}")