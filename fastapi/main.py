from os import environ as env
from fastapi import FastAPI
import requests


app = FastAPI()


@app.get("/")
def index():
    DB_URL = env["DB_URL"]
    print(DB_URL)
    output = f"Hot reloading works! 👏 DB_URL = {DB_URL} 🚀"
    return {"details": output, "success": True, "error": None}


@app.get("/users")
def get_users():

    response = requests.get("https://api.github.com/users/python-test-engineer")

    output = response.json()
    if response.status_code != 200:
        output = {"details": output, "success": False, "error": "API Error"}
    else:
        output = {"details": output["login"], "success": True, "error": None}
    return output
