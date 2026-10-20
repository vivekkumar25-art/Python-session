
import csv

contacts = [
    {"Name": "Sushil", "Phone": "9876543210"},
    {"Name": "Vivek", "Phone": "9876543211"},
    {"Name": "Samita", "Phone": "9876543212"},
    {"Name": "Rahul", "Phone": "9876543213"},
    {"Name": "Sneha", "Phone": "9876543214"}
]

with open("contacts.csv", "w", newline="") as file:
    fieldnames = ["Name", "Phone"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(contacts)

print("Contacts whose names start with S:")

with open("contacts.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for contact in reader:
        if contact["Name"].startswith("S"):
            print(contact["Name"], "-", contact["Phone"])
