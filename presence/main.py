import os
import uvicorn

from dotenv import load_dotenv
from fastapi import FastAPI
from presence.utils.connect_scylla import connect_scylla
from presence.utils.socket_manager import socket_manager

load_dotenv()

app = FastAPI()
port = int(os.environ.get("PORT"))

connect_scylla()
socket_manager(app=app)

def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("presence.main:app", host="0.0.0.0", port=port, reload=True)