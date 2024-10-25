'''
Module:         task_list.py
Description:    Defines the `TaskList` class that holds `Tasks` and is
                responsible for task CRUD
Author:         Charles Morman

'''

from dataclasses import dataclass, field
from app.task import Task
from app.utils.unique_id import UniqueId


@dataclass
class TaskList:
    '''
    The `TaskList` class is responsible for holding and performing CRUD
    operations on `Tasks`
    '''
    list_id: UniqueId = UniqueId()
    list_name: str = str(list_id)
    task_queue: list[Task] = field(default_factory=list)

    # CRUD: Create
    def add_task(self, task):
        '''Responsible for adding a task to the list'''
        self.task_queue.append(task)
        return self

    # CRUD: Read
    def get_task(self, task_id):
        '''Responsible for fetching task from list'''
        # If it is an integer, use it as index
        if isinstance(task_id, int):
            return self.task_queue[task_id]
        # Otherwise lookup by task_id
        # Lookup logic is in `get_task_position`
        return self.task_queue[self.get_task_pos(task_id)]

    def get_task_pos(self, task_id):
        '''Returns the index number of task if found'''
        # Iterate task_queue
        for i, task_item in enumerate(self.task_queue):
            # Look for task_id match
            if task_item.task_id == task_id:
                return i

    # CRUD: Update
    def update_task_position(self, task_id, i):
        '''Responsible for updating task position in list'''
        return self

    # CRUD: Delete
    def remove_task(self, task_id):
        '''Responsible for removing a task from the list'''
        if self.task_queue:
            for i, task_item in enumerate(self.task_queue):
                if task_item.task_id == task_id:
                    self.task_queue.pop(i)
                    return self
                return self
