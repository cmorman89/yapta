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
    task_list: list[Task] = field(default_factory=list)
    list_name: str = None
