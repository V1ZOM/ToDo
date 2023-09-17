tasks = []

while True:
  print("\nOptions:")
  print("1. Add a task")
  print("2. Remove a task")
  print("3. Mark a task as done")
  print("4. Show tasks")
  print("5. Quit")

  choice = input("Enter your choice (1/2/3/4/5): ")

  if choice == '1':
    task = input("Enter the task: ")
    tasks.append({"task": task, "done": False})
    print(f"Task '{task}' added successfully!")
  elif choice == '2':
    task = input("Enter the task to remove: ")
    for t in tasks:
      if t["task"] == task:
        tasks.remove(t)
        print(f"Task '{task}' removed successfully!")
    print(f"Task '{task}' not found in the list.")
  elif choice == '3':
    if tasks:
      print("To-Do List:")
      for i, task in enumerate(tasks, start=1):
        status = "Done" if task["done"] else "Not Done"
        print(f"{i}. [{status}] {task['task']}")
    else:
      print("Your to-do list is empty.")

    task = input("Enter the task to mark as done: ")
    for t in tasks:
      if t["task"] == task:
        t["done"] = True
        print(f"Task '{task}' marked as done!")
      else:
        print(f"Task '{task}' not found in the list.")
  elif choice == '4':
    if tasks:
      print("To-Do List:")
      for i, task in enumerate(tasks, start=1):
        status = "Done" if task["done"] else "Not Done"
        print(f"{i}. [{status}] {task['task']}")
    else:
      print("Your to-do list is empty.")
  elif choice == '5':
    print("Goodbye!")
    break
  else:
    print("Invalid choice. Please select a valid option.")
