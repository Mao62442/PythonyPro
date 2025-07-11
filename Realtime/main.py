from fastapi import FastAPI, WebSocket, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import pandas as pd
import asyncio

from starlette.websockets import WebSocketDisconnect

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def get_page(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            df = pd.read_csv("data.csv")
            data = {
                "columns": df.columns.tolist(),
                "rows": df.tail(10).values.tolist(),
            }
            await websocket.send_json(data)
            await asyncio.sleep(1)
    except WebSocketDisconnect:
        (
            print("WebSocket disconnected"))
    except Exception as e:
        print(f"WebSocket error: {e}")
    finally:
        await websocket.close()
