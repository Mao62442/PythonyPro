from datetime import datetime

from fastapi import FastAPI, WebSocket, Request, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import asyncio, csv

from starlette.responses import JSONResponse

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


def read_latest_data():
    try:
        with open("data/now_data.csv", newline='', encoding='utf-8') as f:
            rows = list(csv.DictReader(f))
            if not rows:
                return None
            last = rows[-1]
            return {
                "timestamp": last["timestamp"],  # ← 追加！
                "formaldehyde": last["formaldehyde"],
                "temperature": last["temperature"],
                "humidity": last["humidity"]
            }
    except Exception as e:
        print(f"読み取り失敗: {e}")
        return None


@app.get("/", response_class=HTMLResponse)
async def get_home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.websocket("/ws/last_data")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    prev_data = None  # 前回のデータを保存
    try:
        while True:
            data = read_latest_data()

            # 前回と違う場合のみ送信
            if data != prev_data:
                await websocket.send_json(data)
                prev_data = data

            await asyncio.sleep(1)  # チェック間隔（例：1秒）
    except WebSocketDisconnect:
        print("🔌 WebSocket切断されました")


@app.websocket("/ws/history")
async def get_history(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            with open("data/data.csv", newline="", encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile)
                data = [row for row in reader]
            await websocket.send_json({"data": data})
            await asyncio.sleep(2)
    except Exception as e:
        print("WebSocket connection closed:", e)
        await websocket.close()