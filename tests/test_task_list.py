"""Tests the app/task_list.py module"""

from app.task import Task
from app.task_list import TaskList


def test_task_list_construction():
    """Tests if `TaskList` can be constructed"""
    task = Task()
    task_list = TaskList()
    assert isinstance(task_list, TaskList)
    print(task_list)
    task_list = TaskList(task_queue=[task])
    assert task_list.task_queue[0] == task


def test_add_task_to_list():
    """Test if `Task` can be added to `TaskList`"""
    task = Task()
    task_list = TaskList()
    task_list.add_task(task)

    assert task_list.task_queue[0] == task


def test_get_task_from_list():
    """Retreive a task by ID"""
    task = Task()
    task_id = task.task_id
    task_list = TaskList()
    task_list.add_task(task)

    assert task_list.get_task(task_id)
    assert task_list.get_task(0)


def test_remove_task_from_list():
    """Remove a task based on `task_id`"""
    task = Task()
    task_id = task.task_id
    task_list = TaskList()
    task_list.add_task(task)
    task = Task()
    task_list.add_task(task)

    task_list.remove_task(task_id)

    assert task_list.task_queue[0] == task


def test_update_task_position():
    """Find a task and move it to a new position"""
    task_list = TaskList()
    task_list.add_task(Task()).add_task(Task()).add_task(Task())

    # Get the task_id of the first task
    task_id = task_list.get_task(0).task_id

    # Move that task to i = 1
    task_list.update_task_position(task_id, 1)

    # Get element 1 and check if it matches saved task_id
    assert task_list.get_task(1).task_id == task_id


def test_update_task_list_name():
    """Update the task list's name"""
    task_list = TaskList()

    task_list.update_task_list_name("New Name")
    assert task_list.list_name == "New Name"

    task_list.update_task_list_name("")
    assert not task_list.list_name
    task_list.update_task_list_name(None)
    assert not task_list.list_name
