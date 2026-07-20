from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class CreateTask(BaseModel):
    title : str

tasks = [
    {
        "id" : 1,
        "title" : "Task 1",
        "done" : False
    },
    {
        "id" : 2,
        "title" : "Task 2",
        "done" : False
    },
    {
        "id" : 3,
        "title" : "Task 3",
        "done" : False
    }
]

@app.get("/")
def read_root():
    return { "name": "Task API", "version": "1.1", "endpoints": ["/tasks"] }

@app.get("/health")
def read_health():
    return {"status": "ok"}

@app.get("/tasks")
def get_task():
    return tasks

@app.get("/tasks/{task_id}")
def get_task_by_id(task_id : int):
    for task in tasks:
        if task["id"] == task_id: 
            return task
    raise HTTPException(status_code = 404, detail = f"Task {task_id} not found")

@app.post("/tasks", status_code = 201)
def create_task(create_title : CreateTask):
    if not create_title.title.strip():
        raise HTTPException(status_code = 400, detail = "Title cannot be empty")
    next_id = -1
    if len(tasks) != 0:
        for task in tasks:
            next_id = max(task["id"], next_id)
        next_id += 1
    else:
        next_id = 1
    newtask = {"id"  : next_id, "title" : create_title.title, "done" : False}
    tasks.append(newtask)
    return newtask