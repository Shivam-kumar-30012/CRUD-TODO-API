from fastapi import FastAPI, HTTPException

app = FastAPI()


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
