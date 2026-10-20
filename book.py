
book_type = input("Enter book type (standard/reference): ")
overdue_days = int(input("Enter overdue days: "))
premium_member = input("Are you a premium member? (yes/no): ")

if book_type == "standard":
    if overdue_days <= 5:
        fine = overdue_days * 5
    else:
        fine = (5 * 5) + ((overdue_days - 5) * 10)

elif book_type == "reference":
    fine = overdue_days * 20

else:
    fine = 0
    print("Invalid book type!")# Calculate fine


if book_type in ["standard", "reference"]:
    if premium_member == "yes":
        fine = fine * 0.80

    print(f"Total library fine: Rs {fine:.2f}")
