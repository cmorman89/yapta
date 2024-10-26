"""
Module:         task.py
Description:    Defines the `Task` class that holds task data
Author:         Charles Morman
"""

from dataclasses import dataclass, field
from app.utils.unique_id import UniqueId


@dataclass
class Task:
    """
    Responsibility: `Task` class primarily holds task-related data and
        other identifiers, updates self values
    """

    task_id: UniqueId = field(default_factory=UniqueId)
    task_name: str = str(task_id)
    description: str = None
    due_date: str = None
    priority: str = None
    complete: bool = False

    def update_name(self, title):
        """Update task `title`"""
        self.task_name = title
        return self

    def update_description(self, description):
        """Update task `description`"""
        self.description = description
        return self

    def update_due_date(self, due_date):
        """Update task `due_date`"""
        self.due_date = due_date
        return self

    def update_priority(self, priority):
        """Update task `priority`"""
        self.priority = priority
        return self

    def toggle_complete(self):
        """Toggle task `complete` boolean"""
        self.complete = not self.complete
        return self
