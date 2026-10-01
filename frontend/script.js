const API_BASE = "http://127.0.0.1:8000";

const addForm = document.getElementById("addForm");
const taskInput = document.getElementById("taskInput");
const taskListEl = document.getElementById("taskList");
const emptyStateEl = document.getElementById("emptyState");
const progressCountEl = document.getElementById("progressCount");
const progressPercentEl = document.getElementById("progressPercent");
const progressFillEl = document.getElementById("progressFill");
const errorMsgEl = document.getElementById("errorMsg");
const fileWarningEl = document.getElementById("fileWarning");

// If this file was opened directly (file://) instead of via the server,
// fetch() below will always fail — tell the user exactly why.
if (location.protocol === "file:") {
  fileWarningEl.hidden = false;
  addForm.querySelector("button").disabled = true;
}

function showError(show) {
  errorMsgEl.hidden = !show;
}

function renderTasks(tasks) {
  taskListEl.innerHTML = "";
  emptyStateEl.hidden = tasks.length > 0;

  tasks.forEach((task, index) => {
    const li = document.createElement("li");
    li.className = "task-item" + (task.done ? " done" : "");

    const name = document.createElement("span");
    name.className = "task-name";
    name.textContent = task.name;

    const check = document.createElement("button");
    check.className = "task-check";
    check.type = "button";
    check.setAttribute("aria-label", task.done ? "Mark as not done" : "Mark as done");
    check.addEventListener("click", () => completeTask(index));

    const del = document.createElement("button");
    del.className = "task-delete";
    del.type = "button";
    del.setAttribute("aria-label", `Remove "${task.name}"`);
    del.innerHTML = '<svg width="15" height="15" viewBox="0 0 15 15" fill="none"><path d="M2.5 4h10M6 4V2.5h3V4M3.5 4l.6 8.5a1 1 0 001 .9h4l1-.9L11 4" stroke="currentColor" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round"/></svg>';
    del.addEventListener("click", () => deleteTask(index));

    li.appendChild(name);
    li.appendChild(check);
    li.appendChild(del);
    taskListEl.appendChild(li);
  });
}

function renderProgress(progress) {
  const { completed, total, percentage } = progress;
  progressCountEl.textContent = `${completed}/${total} done`;
  progressPercentEl.textContent = `${Math.round(percentage)}%`;
  progressFillEl.style.width = `${percentage}%`;
}

async function loadTasks() {
  if (location.protocol === "file:") return;
  try {
    const res = await fetch(`${API_BASE}/tasks`);
    if (!res.ok) throw new Error("Failed to load tasks");
    const data = await res.json();
    showError(false);
    renderTasks(data.tasks);
    renderProgress(data.progress);
  } catch (err) {
    showError(true);
  }
}

async function addTask(name) {
  try {
    const res = await fetch(`${API_BASE}/tasks`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name }),
    });
    if (!res.ok) throw new Error("Failed to add task");
    await loadTasks();
  } catch (err) {
    showError(true);
  }
}

async function completeTask(index) {
  try {
    const res = await fetch(`${API_BASE}/tasks/${index}/complete`, { method: "POST" });
    if (!res.ok) throw new Error("Failed to complete task");
    await loadTasks();
  } catch (err) {
    showError(true);
  }
}

async function deleteTask(index) {
  try {
    const res = await fetch(`${API_BASE}/tasks/${index}`, { method: "DELETE" });
    if (!res.ok) throw new Error("Failed to delete task");
    await loadTasks();
  } catch (err) {
    showError(true);
  }
}

addForm.addEventListener("submit", (e) => {
  e.preventDefault();
  const name = taskInput.value.trim();
  if (!name) return;
  taskInput.value = "";
  addTask(name);
});

loadTasks();