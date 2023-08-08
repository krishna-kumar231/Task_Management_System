# task.py

class Task:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.completed = False

    def __str__(self):
        status = "Completed" if self.completed else "Not Completed"
        return f"{self.name}: {self.description} ({status})"
