from fastapi import FastAPI
import json

app = FastAPI()

def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)
    
    return data


@app.get("/")
def read_root():
    return {"message": "Patient management System API!"}

@app.get("/about")
def about():
    return {"message": "A Fully Functional API To Manage Your Patient Record!"}

@app.get("/view")
def view():
    data = load_data()
    
    return data