'''
Module:         task_manager.py
Description:    Defines the `TaskManager` class that holds `Tasks` and is
                responsible for task CRUD
Author:         Charles Morman

'''

from dataclasses import dataclass, field
from app.task import Task


@dataclass
class TaskManager:
    '''
    The `TaskManager` class is responsible for holding and performing CRUD
    operations on `Tasks`
    '''
    task_list: list[Task] = field(default_factory=list)
    list_name: str = None
