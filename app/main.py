from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="api de botones", description="esta es una api de control", version="1.0.0")

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Item(BaseModel):
    x: int
    y: int

@app.post("/")
async def suma(item: Item):
    print(item)
    salida = item.x + item.y
    return {"test": salida}
