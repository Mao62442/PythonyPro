from fastapi import FastAPI, WebSocket, Request, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import asyncio, csv

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

def read_latest_data():
    try:
        with open("data/data.csv", newline='', encoding='utf-8') as f:
            rows = list(csv.DictReader(f))
            return rows[-1] if rows else {"formaldehyde": "N/A", "temperature": "N/A", "humidity": "N/A"}
    except Exception as e:
        print(f"読み取り失敗: {e}")
        return {"formaldehyde": "ERR", "temperature": "--", "humidity": "--"}

@app.get("/", response_class=HTMLResponse)
async def get_home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.websocket("/ws/data")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = read_latest_data()
            await websocket.send_json(data)
            await asyncio.sleep(5)
    except WebSocketDisconnect:
        print("🔌 WebSocket切断されました")
