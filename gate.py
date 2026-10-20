
age = int(input("Enter passenger age: "))
gender = input("Enter gender (male/female): ").lower()
traveling_alone = input("Are you traveling alone? (yes/no): ").lower()
ticket_type = input("Enter ticket type (normal/tatkal): ").lower()
festival_holiday = input("Is it a blackout festival holiday? (yes/no): ").lower()

if (
    (age >= 60 or (gender == "female" and traveling_alone == "yes"))
    and ticket_type != "tatkal"
    and festival_holiday == "no"
):
    print("Eligible for lower-berth preference and ticket discount.")
else:
    print("Not eligible for special benefits.")
