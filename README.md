# Task Tracker CLI

## Overview

Task Tracker CLI is a command-line application built in Python that allows users to manage tasks efficiently. It supports creating, updating, deleting, and tracking tasks with persistent storage using a JSON file.

---

## Features

- Add tasks
- List all tasks
- Filter tasks by status (`todo`, `in-progress`, `done`)
- Update task descriptions
- Delete tasks
- Mark tasks as in-progress
- Mark tasks as done
- Persistent storage using `tasks.json`

---

## Project structure
```bash
Task Tracker CLI/
│
├── task_tracker/
│   ├── task_cli.py → entry point
│   ├── cli.py → command parsing and output
│   ├── service.py → business logic
│   ├── storage.py → JSON read/write
│   ├── models.py → Task data model
│   ├── utils.py → helper functions like timestamp generation
│   ├──__init__.py
├──tasks.json → persisted task data
└── README.md
```

---

## Getting Started

### Prerequisites
- Python 3.x

### Run the Application

Execute commands from the project root:

```bash
python3 -m task_tracker.task_cli <command> [arguments]
```

#### Examples:

* add a task
* list tasks
* update task
* delete task
* mark in progress
* mark done

```
python3 -m task_tracker.task_cli add "Buy groceries"
python3 -m task_tracker.task_cli list
python3 -m task_tracker.task_cli list todo
python3 -m task_tracker.task_cli update 1 "Buy groceries and vegetables"
python3 -m task_tracker.task_cli mark-in-progress 1
python3 -m task_tracker.task_cli mark-done 1
python3 -m task_tracker.task_cli delete 1
```

## Data format

Each task contains the following fields:

* id → Unique identifier
* description → Task description
* status → (todo, in-progress, done)
* createdAt → Creation timestamp
* updatedAt → Last updated timestamp

## Design explanation

The project follows a layered design:

* CLI layer → Handles command-line input and output
* Service layer → Contains task-related business logic
* Storage layer → Manages JSON persistence
* Model layer → Defines the Task object

This separation improves:
- Readability
- Maintainability
- Scalability.

## Error handling

The application handles:

* Missing arguments
* Invalid task IDs
* Invalid status filters
* File not found / empty / corrupted JSON
* Task not found scenarios
* Empty descriptions

## Future improvements

* Use argparse for cleaner CLI parsing
* Add unit and integration tests
* Support task priorities or due dates
* Improve CLI output formatting(tables, colors)
* Add custom exceptions
* Add logging support

## Project URL
https://github.com/DeepthiPavurala/task-tracker-cli
