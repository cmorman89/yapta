'''Tests the app/task_list.py module'''


from datetime import datetime
from app.task import Task
from app.task_list import TaskList


def test_task_list_construction():
    '''Tests if `TaskList` can be constructed'''
    task = Task()
    task_list = TaskList()
    assert isinstance(task_list, TaskList)

    task_list = TaskList([task])
    assert task_list.task_queue[0] == task


def test_add_task_to_list():
    '''Test if `Task` can be added to `TaskList`'''
    task = Task()
    task_list = TaskList()
    task_list.add_task(task)

    assert task_list.task_queue[0] == task
    

