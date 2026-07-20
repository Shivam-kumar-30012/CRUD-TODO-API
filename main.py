from fastapi import FastAPI 
from pydantic import BaseModel


app = FastAPI()


@app.get("/") # just for the homepage
def read_root():
    return { "name": "Task API", "version": "1.0", "endpoints": ["/tasks"] }    # when you run the page you will see this message on the homepage

@app.get("/health")
def health_check():
    return {"status": "ok"}
