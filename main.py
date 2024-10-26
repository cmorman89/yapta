"""
Note:   This is primarily a live test of functionality
        It is designed to be quick and easy to write
        and use.
"""

import time
from app.task import Task
from app.task_list import TaskList
from app.utils.task_printer import TaskPrinter


if __name__ == "__main__":

    task_list = TaskList()
    make_another = True
    while make_another:
        # Basic functionality:
        print("\n\n\n")
        print("============================")
        print("YET ANOTHER PYTHON TO-DO APP")
        print("============================\n")
        time.sleep(0.4)
        print("Let's build your first task!\n")
        task = Task()

        LINE_PAUSE = 0.1
        time.sleep(0.2)
        task.update_name(input("What is the name of your task?\n"))
        time.sleep(LINE_PAUSE)
        task.update_due_date(input("When is your task due?\n"))
        time.sleep(LINE_PAUSE)
        task.update_priority(input("What is your task priority?\n"))
        time.sleep(LINE_PAUSE)
        task.update_description(input("Add a description, or leave blank:\n"))
        time.sleep(LINE_PAUSE)
        print("Type 'c' to mark complete, or leave blank for incomplete")
        if input("") == "c":
            task.toggle_complete()
        for x in range(1, 6):
            print(". " * x)
            time.sleep(0.2)

        print("\nYour task has been created!")
        TaskPrinter.print_task(task)
        task_list.add_task(task)
        print("\nYour task list is:")
        task_list.print_todo()
        print("Would you like to make another task? (Y/n)")
        if input() == "n":
            make_another = False
