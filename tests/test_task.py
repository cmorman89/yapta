'''Tests the app/task.py module'''


from datetime import datetime
from app.task import Task


# Global/common inputs
TASK_ID = 1
TASK_TITLE = "Get Milk"
TASK_DESC = "Remember to get milk from the store."
TASK_DUE_DATE = datetime(2024, 9, 30)
TASK_DUE_DATE_STR = "9/30/2024"
TASK_PRIORITY = "High"
Template_Task = Task(task_id=TASK_ID,
                     title=TASK_TITLE,
                     description=TASK_DESC,
                     due_date=TASK_DUE_DATE,
                     priority=TASK_PRIORITY,
                     complete=True
                     )


def test_task_construction():
    '''Tests the `Tasks` constructor and attributes'''
    task = Task(task_id=TASK_ID, title=TASK_TITLE, description=TASK_DESC,
                due_date=TASK_DUE_DATE, priority=TASK_PRIORITY, complete=True
                )
    assert task.task_id == TASK_ID
    assert task.title == TASK_TITLE
    assert task.description == TASK_DESC
    assert task.due_date == TASK_DUE_DATE
    assert task.priority == TASK_PRIORITY
    assert task.complete is True


def test_task_setters():
    '''Tests the various setters in `Task`'''
    task = Task(task_id=TASK_ID)
    (task.update_title(TASK_TITLE).update_description(TASK_DESC)
        .update_due_date(TASK_DUE_DATE).update_priority(TASK_PRIORITY)
        .toggle_complete())
    assert task.task_id == TASK_ID
    assert task.title == TASK_TITLE
    assert task.description == TASK_DESC
    assert task.due_date == TASK_DUE_DATE
    assert task.priority == TASK_PRIORITY
    assert task.complete is True


def test_task_complete_toggle():
    '''Toggle boolean back and forth'''
    task = Task()
    assert not task.complete
    task.toggle_complete()
    assert task.complete
    task.toggle_complete()
    assert not task.complete
