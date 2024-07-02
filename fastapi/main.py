from os import environ as env
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    DB_URL = env["DB_URL"]
    print(DB_URL)
    output = f"Hot reloading works! 👏 DB_URL = {DB_URL} 🚀"
    return {"details": output}
