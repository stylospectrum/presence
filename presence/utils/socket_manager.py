import socketio
from fastapi import FastAPI


def socket_manager(app: FastAPI):
    _sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins='*')
    _app = socketio.ASGIApp(
        socketio_server=_sio, socketio_path='socket.io'
    )

    app.mount('/ws', _app)
    app.sio = _sio
