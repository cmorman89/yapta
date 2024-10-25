# TaskList Module

## Overview
The `TaskList` class is responsible for managing a collection of `Task` instances. It enables operations on tasks, such as adding, retrieving, updating, and deleting. `TaskList` interacts with `UniqueId` to ensure each list is uniquely identifiable, supporting features like multiple task lists in the future.

## Attributes
- **list_id** (`UniqueId`): Unique identifier for each task list.
- **list_name** (`str`): Name of the task list.
- **task_queue** (`list[Task]`): List that stores `Task` objects.

## Methods
### CRUD Operations
- **add_task(task)**: Adds a `Task` instance to `task_queue`.
- **get_task(task_id)**: Retrieves a `Task` by its ID or by position in the queue if an integer is passed.
- **get_task_position(task_id)**: Returns the index of a `Task` based on `task_id`.
- **update_task_position(task_id, i)**: Moves a task to a new position in `task_queue`.
- **remove_task(task_id)**: Removes a `Task` from `task_queue` by `task_id`.

### Design Choices
`TaskList` is built to support flexibility in accessing tasks by either `task_id` or queue position. This design choice enables efficient retrieval and management of tasks. Encapsulating `task_id` management with `UniqueId` ensures each list and task is traceable across different sessions and databases.
