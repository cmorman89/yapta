

from app.task import Task
from app.task_list import TaskList


if __name__ == "__main__":
    task_1 = Task(task_name="Item 1")
    task_2 = Task(task_name="Item 2")
    task_3 = Task(task_name="Item 3")

    task_list = TaskList()

    task_list.add_task(task_1).add_task(task_2).add_task(task_3)

    task_list.print_todo()
