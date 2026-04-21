from task_tracker.utils import current_timestamp
from task_tracker.models import Task

class TaskService:
    def __init__(self, storage):
        self.storage = storage

    def _get_next_id(self,tasks):
        if not tasks:
            return 1
        return max(task.id for task in tasks) + 1

    def _find_task_by_id(self,tasks, task_id):
        for task in tasks:
            if task.id == task_id:
                return task
        return None
     
    def _update_status(self, task_id, status):
        tasks = self.storage.load_tasks()
        task = self._find_task_by_id(tasks, task_id)

        if not task:
            return None
        task.status = status
        task.updatedAt = current_timestamp()
        self.storage.save_tasks(tasks)
        return task

    def add_task(self, description):
        tasks = self.storage.load_tasks()

        if not description or not description.strip():
            return "empty_description"
        cur_timestamp = current_timestamp()
        description = description.strip()
        task = Task(
            id = self._get_next_id(tasks),
            description = description,
            status =  "todo",
            createdAt = cur_timestamp,
            updatedAt = cur_timestamp
        )
        tasks.append(task)
        self.storage.save_tasks(tasks)
        return task
    
    def list_tasks(self, status=None):
        tasks = self.storage.load_tasks()
        if status:
            return [task for task in tasks if task.status==status]
        return tasks
    
    def update_task(self, task_id, description):
        tasks = self.storage.load_tasks()
        task = self._find_task_by_id(tasks, task_id)

        if not task:
            return "not_found"
        if not description or not description.strip():
            return "empty_description"
        task.description = description.strip()
        task.updatedAt = current_timestamp()
        self.storage.save_tasks(tasks)
        return task

    def delete_task(self, task_id):
        tasks = self.storage.load_tasks()
        task = self._find_task_by_id(tasks, task_id)

        if not task:
            return False
        
        tasks=[t for t in tasks if t.id!= task_id]
        self.storage.save_tasks(tasks)
        return True

    def mark_in_progress(self, task_id):
        return self._update_status(task_id, "in-progress")

    def mark_done(self, task_id):
        return self._update_status(task_id, "done")

            