from aiohttp import web
import socketio

rooms: list[dict] = []

sio = socketio.AsyncServer()
app = web.Application()
sio.attach(app)

@sio.event
def connect(sid, environ):
    print("connect ", sid)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

@sio.event
async def create_room(sid, data):
    print(sid,"joining", data)
    rooms.append(data)
    sio.enter_room(sid, data["name"])

if __name__ == '__main__':
    web.run_app(app)
    