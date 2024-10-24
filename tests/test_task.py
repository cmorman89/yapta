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


def test_task_construction():
    '''Tests the `Tasks` constructor and attributes'''
    task = Task(id=TASK_ID, title=TASK_TITLE, description=TASK_DESC,
                due_date=TASK_DUE_DATE, priority=TASK_PRIORITY)
    assert task.id == TASK_ID
    assert task.title == TASK_TITLE
    assert task.description == TASK_DESC
    assert task.due_date == TASK_DUE_DATE
    assert task.priority == TASK_PRIORITY
