'''
Module:     task.py
Descrp:     Defines the `Task` class that holds task data
Author:     Charles Morman

'''


from dataclasses import dataclass


@dataclass
class Task:
    '''
    Responsibility: `Task` class primarily holds task-related data and
        other identifiers
    '''
    def __init__(self, id=None, title="Untitled Task", description=None,
                 due_date=None, priority=None, complete=False):
        self.id = id                    # placeholder
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.complete = complete

  
    def update_title(self, title):
        self.title = title
        return self


    def update_description(self, description):
        self.description = description
        return self


    def update_due_date(self, due_date):
        self.due_date = due_date
        return self


    def update_priority(self, priority):
        self.priority = priority
        return self

    def toggle_complete(self):
        self.complete = not self.complete
        return self
