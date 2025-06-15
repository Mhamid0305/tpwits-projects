import json
import os

FILENAME = "tasks.json"

# === File Handling ===
def read_tasks():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, 'r') as file:
        return json.load(file)

def write_tasks(task_data):
    with open(FILENAME, 'w') as file:
        json.dump(task_data, file, indent=4)

# === Core Functionalities ===

def create_task():
    task_text = input("🆕 Enter task description: ")
    task_list = read_tasks()
    task_list.append({"description": task_text, "is_done": False})
    write_tasks(task_list)
    print("✅ Task successfully created!\n")

def show_tasks():
    task_list = read_tasks()
    if not task_list:
        print("📭 No tasks found.\n")
        return
    print("\n📋 Task List:")
    for idx, item in enumerate(task_list, start=1):
        status = "✅" if item["is_done"] else "❌"
        print(f"{idx}. {item['description']} - {status}")
    print()

def complete_task():
    task_list = read_tasks()
    try:
        index = int(input("✔️ Enter task number to complete: ")) - 1
        if 0 <= index < len(task_list):
            task_list[index]["is_done"] = True
            write_tasks(task_list)
            print("🎉 Task marked as completed!\n")
        else:
            print("⚠️ Invalid task number.\n")
    except ValueError:
        print("⚠️ Please enter a valid number.\n")

def remove_task():
    task_list = read_tasks()
    try:
        index = int(input("🗑️ Enter task number to remove: ")) - 1
        if 0 <= index < len(task_list):
            removed = task_list.pop(index)
            write_tasks(task_list)
            print(f"🧹 Removed task: {removed['description']}\n")
        else:
            print("⚠️ Task number does not exist.\n")
    except ValueError:
        print("⚠️ Invalid input.\n")

# === Program Menu ===

def launch_app():
    while True:
        print("\n======== TO-DO MANAGER ========\n")
        print("1. Create a New Task")
        print("2. View All Tasks")
        print("3. Mark a Task as Completed")
        print("4. Delete a Task")
        print("5. Exit\n")

        option = input("👉 Choose an option (1-5): ")

        if option == '1':
            create_task()
        elif option == '2':
            show_tasks()
        elif option == '3':
            complete_task()
        elif option == '4':
            remove_task()
        elif option == '5':
            print("👋 Exiting the To-Do Manager. Have a productive day!\n")
            break
        else:
            print("❌ Invalid choice. Try again.\n")

# === Run App ===
if __name__ == "__main__":
    launch_app()
