'''
Module:     task_builder.py
Descr.:     Defines the `TaskBuilder` class that extensibly constructs tasks
            and will serve as a future web API hook
Author:     Charles Morman

'''


# from app.task import Task


class TaskBuilder:
    '''
    The `TaskBuilder` class will be responsible for creating tasks, can will be
    the target for new features without changing `Task`, and might have
    application as an API for the web front end
    '''

    def __init__(self, task_id=None, title="Untitled Task", description=None,
                 due_date=None, priority=None, complete=False):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.complete = complete
