'''
Module:     task.py
Descrp:     Defines the `Task` class that holds task data
Author:     Charles Morman

'''


from dataclasses import dataclass


@dataclass
class Task:
    '''
    Responsibility: `Task` class primarily holds task-related data and identifiers
    '''
    def __init__(self, id=None, title="Untitled Task", description=None,
                 due_date=None, priority=None):
        self.id = id                    # placeholder
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
