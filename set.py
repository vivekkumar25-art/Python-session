
students = {"vikky", "aman", "himanshu", "sushil"}

student = input("Enter student name: ")

if student in students:
    print(" exists in set")
else:
    students.add(student)
    print(student, "added to set")

print("All students:", students)
