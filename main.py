"""
Note:   This is primarily a live test of functionality
        It is designed to be quick and easy to write
        and use.
"""

import time
from app.task import Task
from app.task_list import TaskList


if __name__ == "__main__":

    # Basic functionality:
    print("\n\n\n")
    print("============================")
    print("YET ANOTHER PYTHON TO-DO APP")
    print("============================\n")
    time.sleep(0.4)
    print("Let's build your first task!\n")
    task_list = TaskList()
    task = Task()

    line_pause = 0.1
    time.sleep(0.2)
    task.update_name(input("What is the name of your task?\n"))
    time.sleep(line_pause)
    task.update_due_date(input("When is your task due?\n"))
    time.sleep(line_pause)
    task.update_priority(input("What is your task priority?\n"))
    time.sleep(line_pause)
    task.update_description(input("Add a description, or leave blank:\n"))
    time.sleep(line_pause)
    print("Type 'c' to mark complete, or leave blank for incomplete")
    if input("") == "c":
        task.toggle_complete()
    for x in range(1, 6):
        print(". " * x)
        time.sleep(0.2)

    print("\nYour task has been created!")
    print(
        f"""
        ====================================================
        Task Name: {task.task_name}
        ----------------------------------------------------
          - Priority:    {task.priority}
          - Description: {task.description}
          - Due Date:    {task.due_date}
          - Status:      {'Completed'  if task.complete else "Incomplete"}
        ====================================================
        """
    )
    task_list.add_task(task)
    print("\nYour task list is:")
    task_list.print_todo()
