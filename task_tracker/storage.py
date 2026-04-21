import os
import json
from task_tracker.models import Task

class TaskStorage:
    def __init__(self, file_name = "./tasks.json" ):
        self.file_name = file_name

    def load_tasks(self):
        if not os.path.exists(self.file_name):
            return []
        try:
            with open(self.file_name, "r") as file:
                data = json.load(file)
                return [Task.from_dict(task) for task in data]
        except (json.JSONDecodeError, EOFError):
                return []

    def save_tasks(self, tasks):
        with open(self.file_name, "w") as file:
            json.dump([task.to_dict() for task in tasks], file, indent=2)

