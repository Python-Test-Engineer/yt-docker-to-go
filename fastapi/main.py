from os import environ as env
from fastapi import FastAPI
import requests
from datetime import datetime

app = FastAPI()


@app.get("/")
def index():
    DB_URL = env["DB_URL"]
    print(DB_URL)
    output = f"Hot reloading works! 👏 DB_URL = {DB_URL} 🚀"
    now = datetime.now()  # current date and time
    date_time = f'Date and Time now: { now.strftime("%d/%m/%Y, %H:%M:%S") }'
    return {"details": output, "success": True, "error": None, "timestamp": date_time}


@app.get("/users")
def get_users():

    response = requests.get("https://api.github.com/users/python-test-engineer")

    output = response.json()
    if response.status_code != 200:
        output = {"details": output, "success": False, "error": "API Error"}
    else:
        output = {"details": output["login"], "success": True, "error": None}
    return output
