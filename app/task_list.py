'''
Module:         task_list.py
Description:    Defines the `TaskList` class that holds `Tasks` and is
                responsible for task CRUD
Author:         Charles Morman

'''

from dataclasses import dataclass, field
from app.task import Task


@dataclass
class TaskList:
    '''
    The `TaskList` class is responsible for holding and performing CRUD
    operations on `Tasks`
    '''
    task_queue: list[Task] = field(default_factory=list)
    list_name: str = None

    # CRUD: Create
    def add_task(self, task):
        '''Responsible for adding a task to the list'''
        self.task_queue.append(task)
        return self

    # CRUD: Read
    def get_task(self, task_id):
        '''Responsible for fetching task from list'''
        return self

    # CRUD: Update
    def update_task_position(self, task_id, i):
        '''Responsible for updating task position in list'''
        return self

    # CRUD: Delete
    def delete_task(self, task_id):
        '''Responsible for removing a task from the list'''
        return self
