
import json
import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError(
        "GROQ_API_KEY missing hai. Apni .env file check karein."
    )

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0,
)


def extract_tasks(user_input: str) -> list:
    """User ke message se individual tasks extract karein."""

    prompt = f"""
You are a task extraction assistant.

Extract every individual task from the user's message.
Do not invent tasks.
Return ONLY a valid JSON array of strings.

Example:
Input: I need to study Python and buy groceries.
Output: ["Study Python", "Buy groceries"]

User message:
{user_input}
"""

    response = llm.invoke(prompt)
    content = response.content

    if isinstance(content, list):
        content = "".join(
            item.get("text", "") if isinstance(item, dict)
            else str(item)
            for item in content
        )

    content = str(content).strip()
    content = content.removeprefix("```json").removeprefix("```")
    content = content.removesuffix("```").strip()

    tasks = json.loads(content)

    if not isinstance(tasks, list):
        raise ValueError("AI ne valid task list return nahi ki.")

    return [str(task) for task in tasks if str(task).strip()]


def prioritize_tasks(tasks: list) -> list:
    """Har task ko High, Medium ya Low priority dein."""

    if not tasks:
        return []

    prompt = f"""
You are a task prioritization assistant.

Assign each task one priority:
- High: urgent, deadline is near, or very important
- Medium: important but not immediately urgent
- Low: optional or less urgent

Use deadlines mentioned by the user when available.
Do not invent deadlines.

Return ONLY a valid JSON array in this format:
[
  {{"task": "Complete assignment", "priority": "High",
    "reason": "Due tomorrow"}}
]

Tasks:
{json.dumps(tasks, ensure_ascii=False)}
"""

    response = llm.invoke(prompt)
    content = response.content

    if isinstance(content, list):
        content = "".join(
            item.get("text", "") if isinstance(item, dict)
            else str(item)
            for item in content
        )

    content = str(content).strip()
    content = content.removeprefix("```json").removeprefix("```")
    content = content.removesuffix("```").strip()

    result = json.loads(content)

    if not isinstance(result, list):
        raise ValueError("AI ne valid priority list return nahi ki.")

    valid_priorities = {"High", "Medium", "Low"}
    task_map = {task: task for task in tasks}
    cleaned = []

    for item in result:
        if not isinstance(item, dict):
            continue

        task = str(item.get("task", "")).strip()
        priority = str(item.get("priority", "Medium")).title()

        if task not in task_map:
            continue

        if priority not in valid_priorities:
            priority = "Medium"

        cleaned.append({
            "task": task,
            "priority": priority,
            "reason": str(item.get("reason", ""))
        })

    # Agar AI koi task miss kare, use bhi list mein rakhein.
    included = {item["task"] for item in cleaned}

    for task in tasks:
        if task not in included:
            cleaned.append({
                "task": task,
                "priority": "Medium",
                "reason": "Default priority; review suggested"
            })

    return cleaned
