from fastapi import FastAPI 
from pydantic import BaseModel


app = FastAPI()


@app.get("/") # just for the homepage
def read_root():
    return {"Hello" : "Server"}   # when you run the page you will see this message on the homepage

