
from langgraph.graph import StateGraph, START, END

from src.state import TaskFlowState
from src.agents import extract_tasks, prioritize_tasks


def task_extraction_node(state: TaskFlowState) -> dict:
    """Node 1: User message se tasks extract karein."""
    tasks = extract_tasks(state["user_input"])
    return {"tasks": tasks}


def task_prioritization_node(state: TaskFlowState) -> dict:
    """Node 2: Har task ko priority assign karein."""
    prioritized_tasks = prioritize_tasks(state["tasks"])
    return {"prioritized_tasks": prioritized_tasks}


def format_results_node(state: TaskFlowState) -> dict:
    """Node 3: Tasks ko readable to-do list mein format karein."""
    tasks = state["prioritized_tasks"]

    priority_order = {"High": 0, "Medium": 1, "Low": 2}
    tasks = sorted(
        tasks,
        key=lambda item: priority_order.get(item["priority"], 1)
    )

    lines = ["# Your Organized To-Do List", ""]

    if not tasks:
        lines.append("No tasks found. Please enter some tasks.")
    else:
        for index, task in enumerate(tasks, start=1):
            lines.append(
                f"{index}. **[{task['priority']}]** {task['task']}"
            )

            reason = task.get("reason", "").strip()
            if reason:
                lines.append(f"   - Reason: {reason}")

    return {"formatted_result": "\n".join(lines)}


def build_graph():
    """Create and compile the TaskFlow AI workflow."""
    workflow = StateGraph(TaskFlowState)

    workflow.add_node("task_extraction", task_extraction_node)
    workflow.add_node("task_prioritization", task_prioritization_node)
    workflow.add_node("format_results", format_results_node)

    workflow.add_edge(START, "task_extraction")
    workflow.add_edge("task_extraction", "task_prioritization")
    workflow.add_edge("task_prioritization", "format_results")
    workflow.add_edge("format_results", END)

    return workflow.compile()
