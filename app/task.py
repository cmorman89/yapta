'''
Module:         task.py
Description:    Defines the `Task` class that holds task data
Author:         Charles Morman

'''


from dataclasses import dataclass


@dataclass
class Task:
    '''
    Responsibility: `Task` class primarily holds task-related data and
        other identifiers, updates self values
    '''
    def __init__(self, task_id=None, title="Untitled Task", description=None,
                 due_date=None, priority=None, complete=False):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.complete = complete
