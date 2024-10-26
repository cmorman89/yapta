"""Tests the app/utils/task_printer.py module"""


import textwrap
from datetime import datetime
from app.task import Task
from app.utils.task_printer import TaskPrinter


# Global/common inputs
TASK_TITLE = "Get Milk"
TASK_DESC = "Remember to get milk from the store."
TASK_DUE_DATE = datetime(2024, 9, 30)
TASK_DUE_DATE_STR = "9/30/2024"
TASK_PRIORITY = "High"
Template_Task = Task(
    task_name=TASK_TITLE,
    description=TASK_DESC,
    due_date=TASK_DUE_DATE,
    priority=TASK_PRIORITY,
    complete=True,
)


def test_task_printer():
    '''Test the formatted output of TaskPrinter'''
    task = Task(
        task_name=TASK_TITLE,
        description=TASK_DESC,
        due_date=TASK_DUE_DATE,
        priority=TASK_PRIORITY,
        complete=True,
        )
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

    assert TaskPrinter.task_card_string(task) == output
