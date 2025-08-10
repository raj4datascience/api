from fastapi import FastAPI

app = FastAPI()

@app.get("/mukesh/api/add/")
def add(a:int,b:int):
    return a+b
