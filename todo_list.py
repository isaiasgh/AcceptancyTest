# todo_list.py

class Task:
    def __init__(self, title, description="", due_date=None, priority="Normal"):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"[{status}] {self.title} - {self.description} (Due: {self.due_date}, Priority: {self.priority})"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description="", due_date=None, priority="Normal"):
        task = Task(title, description, due_date, priority)
        self.tasks.append(task)

    def list_tasks(self):
        return self.tasks

    def mark_task_completed(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_completed()
                return True
        return False

    def clear_tasks(self):
        self.tasks.clear()

    def remove_task(self, title):
        self.tasks = [task for task in self.tasks if task.title != title]

    def list_tasks_by_status(self, completed=False):
        return [task for task in self.tasks if task.completed == completed]
