from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import service
import webbrowser
import threading

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# In-memory task list, shared across all requests
tasks = []

# Serve frontend files
app.mount("/static", StaticFiles(directory="frontend"), name="static")


class TaskCreate(BaseModel):
    name: str


@app.get("/")
def home():
    return FileResponse("frontend/index.html")


@app.get("/tasks")
def list_tasks():
    completed, total, percentage = service.get_progress(tasks)
    return {
        "tasks": tasks,
        "progress": {
            "completed": completed,
            "total": total,
            "percentage": percentage,
        },
    }


@app.post("/tasks")
def create_task(payload: TaskCreate):
    name = payload.name.strip()
    if not name:
        raise HTTPException(status_code=400, detail="Task name cannot be empty")
    service.add_task(tasks, name)
    return {"tasks": tasks}


@app.post("/tasks/{index}/complete")
def complete_task(index: int):
    success = service.mark_done(tasks, index)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"tasks": tasks}


@app.delete("/tasks/{index}")
def delete_task(index: int):
    success = service.remove_task(tasks, index)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"tasks": tasks}


@app.get("/progress")
def progress():
    completed, total, percentage = service.get_progress(tasks)
    return {"completed": completed, "total": total, "percentage": percentage}


def open_browser():
    webbrowser.open("http://127.0.0.1:8000")


threading.Timer(1.5, open_browser).start()