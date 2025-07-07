# main.py

from todo_list import ToDoList

def main():
    todo = ToDoList()
    todo.add_task("Buy groceries", "Milk, eggs, bread", "2025-07-08", "High")
    todo.add_task("Pay bills", "Electricity and water", "2025-07-10", "Medium")

    print("Tasks:")
    for task in todo.list_tasks():
        print(task)

    print("\nMarking 'Buy groceries' as completed...\n")
    todo.mark_task_completed("Buy groceries")

    for task in todo.list_tasks():
        print(task)

    print("\nClearing tasks...")
    todo.clear_tasks()

    print(f"Total tasks after clearing: {len(todo.list_tasks())}")

if __name__ == "__main__":
    main()
