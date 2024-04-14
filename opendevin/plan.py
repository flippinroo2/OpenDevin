from typing import List

from opendevin.task import Task

OPEN_STATE = "open"
COMPLETED_STATE = "completed"
ABANDONED_STATE = "abandoned"
IN_PROGRESS_STATE = "in_progress"
VERIFIED_STATE = "verified"
STATES = [
    OPEN_STATE,
    COMPLETED_STATE,
    ABANDONED_STATE,
    IN_PROGRESS_STATE,
    VERIFIED_STATE,
]


class Plan:
    """Represents a plan consisting of tasks.

    Attributes:
        main_goal: The main goal of the plan.
        task: The root task of the plan.
    """

    main_goal: str
    task: Task

    def __init__(self, task: str):
        """Initializes a new instance of the Plan class.

        Args:
            task: The main goal of the plan.
        """
        self.main_goal = task
        self.task = Task(parent=None, goal=task, subtasks=[])

    def __str__(self):
        """Returns a string representation of the plan.

        Returns:
            A string representation of the plan.
        """
        return self.task.to_string()

    def get_task_by_id(self, id: str) -> Task:
        """Retrieves a task by its ID.

        Args:
            id: The ID of the task.

        Returns:
            The task with the specified ID.

        Raises:
            ValueError: If the provided task ID is invalid or does not exist.
        """
        try:
            parts = [int(p) for p in id.split(".")]
        except ValueError:
            raise ValueError("Invalid task id, non-integer:" + id)
        if parts[0] != 0:
            raise ValueError("Invalid task id, must start with 0:" + id)
        parts = parts[1:]
        task = self.task
        for part in parts:
            if part >= len(task.subtasks):
                raise ValueError("Task does not exist:" + id)
            task = task.subtasks[part]
        return task

    def add_subtask(self, parent_id: str, goal: str, subtasks: List = []):
        """Adds a subtask to a parent task.

        Args:
            parent_id: The ID of the parent task.
            goal: The goal of the subtask.
            subtasks: A list of subtasks associated with the new subtask.
        """
        parent = self.get_task_by_id(parent_id)
        child = Task(parent=parent, goal=goal, subtasks=subtasks)
        parent.subtasks.append(child)

    def set_subtask_state(self, id: str, state: str):
        """Sets the state of a subtask.

        Args:
            id: The ID of the subtask.
            state: The new state of the subtask.
        """
        task = self.get_task_by_id(id)
        task.set_state(state)

    def get_current_task(self):
        """Retrieves the current task in progress.

        Returns:
            The current task in progress, or None if no task is in progress.
        """
        return self.task.get_current_task()
