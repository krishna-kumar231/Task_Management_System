# task_manager.py
from task import Task

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, description):
        task = Task(name, description)
        self.tasks.append(task)

    def list_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            for idx, task in enumerate(self.tasks, 1):
                print(f"{idx}. {task}")

    def mark_completed(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            task = self.tasks[task_index - 1]
            task.completed = True
        else:
            print("Invalid task index.")

    def save_tasks_to_file(self, filename):
        with open(filename, 'w') as file:
            for task in self.tasks:
                file.write(f"{task.name}::{task.description}::{task.completed}\n")

    def load_tasks_from_file(self, filename):
        self.tasks.clear()
        try:
            with open(filename, 'r') as file:
                for line in file:
                    name, description, completed = line.strip().split("::")
                    task = Task(name, description)
                    task.completed = (completed.lower() == "true")
                    self.tasks.append(task)
        except FileNotFoundError:
            print("Task data file not found.")
        except Exception as e:
            print("Error loading tasks:", e)
