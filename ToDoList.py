 tasks = []

while True:
    task = input("Enter a task (or 'exit' to stop): ")

    if task.lower() == "exit":
        break

    tasks.append(task)
    print("Task added successfully! ✅")

print("Your tasks:", tasks)