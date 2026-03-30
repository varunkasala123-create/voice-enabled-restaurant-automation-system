from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
import json

app = FastAPI()

clients = []

@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()
    clients.append(ws)
    try:
        while True:
            await ws.receive_text()
    except:
        clients.remove(ws)

@app.post("/send")
async def send_to_kitchen(data: dict):
    for client in clients:
        await client.send_text(json.dumps(data))
    return {"status": "sent"}

@app.get("/kitchen")
def kitchen():
    return HTMLResponse(open("kitchen.html", encoding="utf-8").read())

