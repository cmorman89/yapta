'''Tests the app/task.py module'''


from datetime import datetime
from app.task import Task
from app.task_list import TaskList


def test_task_list_construction():
    '''Tests if empty task list can be constructed'''
    task_list = TaskList()

    assert isinstance(task_list, TaskList)
