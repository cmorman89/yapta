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
    list_id: UniqueId = field(default_factory=UniqueId)
    list_name: str = None
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
        return self.task_queue[self.get_task_position(task_id)]

    def get_task_position(self, task_id):
        '''Returns the index number of task if found'''
        # Iterate task_queue
        if self.task_queue:
            for i, task_item in enumerate(self.task_queue):
                # Look for task_id match
                if task_item.task_id == task_id:
                    return i
        return None

    # CRUD: Update
    def update_task_list_name(self, list_name):
        '''Update the list name with a `string`'''
        # Use list_name if it is non
        if isinstance(list_name, str) and list_name != "":
            self.list_name = list_name
        else:
            self.list_name = None
    
    def update_task_position(self, task_id, i):
        '''Responsible for updating task position in list'''
        # Check if there is a task queue
        if self.task_queue:
            # Make sure new position within bounds
            # -1 for list[0], -1 for moved task (list.pop())
            max_index = len(self.task_queue) - 2
            i = max_index if i > max_index else i
            # Find and remove task from `task_queue` before inserting
            # it at index position i
            self.task_queue.insert(
                i, self.task_queue.pop(self.get_task_position(task_id))
                )
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

    def print_todo(self):
        '''Print the to-do list to the terminal'''
        if self.list_name:
            print(f'{self.list_name}:')
        if self.task_queue:
            for i, task_item in enumerate(self.task_queue):
                print(f'{i + 1}:\t{task_item.task_name}')
