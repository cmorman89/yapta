"""
Module:         task_printer.py
Description:    Prints a formatted Task card to console
Author:         Charles Morman
"""


import textwrap
from dataclasses import dataclass


@dataclass
class TaskPrinter:
    """
    A class used to print the details of a task in a formatted manner.

    Attributes
    ----------
    task : Task
        An instance of the `Task` class containing task details.

    Methods
    -------
    __init__(task)
        Initializes the `TaskPrinter` with a task and prints its details.
    """
    @staticmethod
    def task_card_string(task):
        """
        Return a formatted card string
        """
        output = textwrap.dedent(f"""
            ====================================================
            Task Name: {task.task_name}
            ----------------------------------------------------
            - Priority:    {task.priority}
            - Description: {task.description}
            - Due Date:    {task.due_date}
            - Status:      {'Completed' if task.complete else "Incomplete"}
            ====================================================
        """).strip(" ")

        return output

    @staticmethod
    def print_task(task):
        """
        Get and the print the formatted card string
        """
        print(TaskPrinter.task_card_string(task))
