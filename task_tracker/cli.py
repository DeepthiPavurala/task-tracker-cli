from task_tracker.storage import TaskStorage
from task_tracker.service import TaskService
import sys

VALID_STATUSES = {"todo", "in-progress", "done"}

def print_task(task):
    print(
        f"[{task.id}] {task.description} | "
        f"status={task.status} | "
        f"createdAt={task.createdAt} | updatedAt={task.updatedAt}"
    )

def parse_task_id(value):
    try:
        return int(value)
    except ValueError:
        return None

def run():
    storage = TaskStorage()
    service = TaskService(storage)

    args = sys.argv[1:]
    if not args:
        print("Usage: task-cli <command> [arguments]")
        return 
    
    command = args[0]

    if command == "add":
        if len(args) < 2:
            print("Missing required arguments")
            return
        
        description = " ".join(args[1:])
        task = service.add_task(description)

        if task == "empty_description":
            print("Description cannot be empty")
        else:
            print(f"Task added successfully (ID: {task.id})")
    
    elif command == "list":
        status = args[1] if len(args) > 1 else None
        if status and status not in VALID_STATUSES:
            print("Invalid status. Use: todo, in-progress, or done")
            return

        tasks = service.list_tasks(status)
        
        if not tasks:
            print("No tasks found")
        else:
            for task in tasks:
                print_task(task)

    elif command == "update":
        if len(args) < 3:
            print("Missing required arguments")
            return
        
        task_id = parse_task_id(args[1])
        if task_id is None:
            print("Task ID must be a number")
            return

        description = " ".join(args[2:])
        task = service.update_task(task_id, description)
        if task == "empty_description":
            print("Description cannot be empty")
        elif task == "not_found":
            print("Task not found")
        else:
            print("Task updated successfully")
    
    elif command == "delete":
        if len(args) < 2:
            print("Missing required arguments")
            return
        
        task_id = parse_task_id(args[1])
        if task_id is None:
            print("Task ID must be a number")
            return
        
        deleted = service.delete_task(task_id)
        if deleted:
            print("Task deleted successfully")
        else:
            print("Task not found")

    elif command == "mark-in-progress":
        if len(args) < 2:
            print("Missing required arguments")
            return
        
        task_id = parse_task_id(args[1])
        if task_id is None:
            print("Task ID must be a number")
            return

        task = service.mark_in_progress(task_id)
        if task:
            print("Task marked as in-progress")
        else:
            print("Task not found")

    elif command == "mark-done":
        if len(args) < 2:
            print("Missing required arguments")
            return
        
        task_id = parse_task_id(args[1])
        if task_id is None:
            print("Task ID must be a number")
            return

        task = service.mark_done(task_id)
        if task:
            print("Task marked as done")
        else:
            print("Task not found")
    
    else:
        print("Unknown command")
        

