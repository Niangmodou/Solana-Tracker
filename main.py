from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
import uvicorn
import pymongo 
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

PASSWORD = os.getenv("PASSWORD")
USERNAME = os.getenv("USERNAME")

app = FastAPI()

# app.mount("/", WSGIMiddleware())

CLUSTER = MongoClient("mongodb+srv://{}:{}@cluster0.rlimv.mongodb.net/Solana-Tracker?retryWrites=true&w=majority".format(USERNAME, PASSWORD))
DATABASE = CLUSTER["Quotes"]

@app.get("/")
def index():

    return "hello"


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
