from typing import TypedDict


class TaskFlowState(TypedDict):
    user_input: str
    tasks: list
    prioritized_tasks: list
    formatted_result: str