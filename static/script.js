
const form = document.getElementById("task-form");
const input = document.getElementById("task-input");
const submitButton = document.getElementById("submit-btn");
const buttonText = document.getElementById("button-text");
const loading = document.getElementById("loading");
const errorMessage = document.getElementById("error-message");
const taskList = document.getElementById("task-list");
const taskCount = document.getElementById("task-count");

document.querySelectorAll("[data-example]").forEach((button) => {
    button.addEventListener("click", () => {
        input.value = button.dataset.example;
        input.focus();
    });
});

function showError(message) {
    errorMessage.textContent = message;
    errorMessage.style.display = "block";
}

function createTaskCard(task, index) {
    const item = document.createElement("article");
    item.className = "task-item";

    const number = document.createElement("div");
    number.className = "task-number";
    number.textContent = String(index + 1);

    const content = document.createElement("div");
    content.className = "task-content";

    const title = document.createElement("div");
    title.className = "task-title";
    title.textContent = task.task;

    const level = ["High", "Medium", "Low"].includes(task.priority)
        ? task.priority
        : "Medium";

    const priority = document.createElement("span");
    priority.className = `priority ${level.toLowerCase()}`;
    priority.textContent = `${level} Priority`;

    content.append(title, priority);

    if (task.reason) {
        const reason = document.createElement("div");
        reason.className = "task-reason";
        reason.textContent = task.reason;
        content.append(reason);
    }

    item.append(number, content);
    return item;
}

form.addEventListener("submit", async (event) => {
    event.preventDefault();

    const message = input.value.trim();
    errorMessage.style.display = "none";

    if (!message) {
        showError("Please enter some tasks first.");
        return;
    }

    submitButton.disabled = true;
    buttonText.textContent = "Organizing...";
    loading.style.display = "block";

    try {
        const response = await fetch("/api/organize", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                user_input: message
            })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(
                data.detail || "Unable to organize tasks."
            );
        }

        const tasks = data.tasks || [];
        taskList.replaceChildren();

        if (tasks.length === 0) {
            const empty = document.createElement("div");
            empty.className = "empty-state";
            empty.textContent =
                "No tasks found. Try another message.";
            taskList.append(empty);
        } else {
            tasks.forEach((task, index) => {
                taskList.append(createTaskCard(task, index));
            });
        }

        taskCount.textContent =
            `${tasks.length} task${tasks.length === 1 ? "" : "s"} organized`;

    } catch (error) {
        showError(
            `${error.message} Check the backend and your Groq API key.`
        );
    } finally {
        submitButton.disabled = false;
        buttonText.textContent = "Organize my tasks";
        loading.style.display = "none";
    }
});
