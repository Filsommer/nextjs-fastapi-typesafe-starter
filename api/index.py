from fastapi import FastAPI
from fastapi.routing import APIRoute
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
import json
from anyio.streams.file import FileWriteStream
import datetime

def custom_generate_unique_id(route: APIRoute):
    return f"{route.tags[0] if len(route.tags) > 0 else ''}-{route.name}"

app = FastAPI(generate_unique_id_function=custom_generate_unique_id)

# TODO handle CORS, see: https://fastapi.tiangolo.com/tutorial/cors/
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Item(BaseModel):
    name: str
    price: int
    created_at: Optional[datetime.date]

class ResponseMessage(BaseModel):
    message: str

# TODO move this to a DB in production ;)
itemList: list[Item] = [Item(name="Stapler", price=3), Item(name="World's Best Boss mug", price=201)]

@app.on_event("startup")
async def startup():
    # write openapi objects to file on startup
    async with await FileWriteStream.from_path("./openapi.json") as stream:
        jsonData = jsonable_encoder(app.openapi())
        for path_data in jsonData["paths"].values():
            for operation in path_data.values():
                operation_id = operation["operationId"]
                new_operation_id = operation_id.split("-")[1]
                operation["operationId"] = new_operation_id
        await stream.send(json.dumps(jsonData).encode("utf-8"))


@app.post("/api/items", response_model=ResponseMessage, tags=["items"])
async def create_item(item: Item):
    itemList.append(item)
    return {"message": "item received"}


@app.get("/api/items", response_model=list[Item], tags=["items"])
async def get_items():
    return itemList

@app.get("/api/python", response_model=str)
async def get_hello():
    return "Hello, I'm a Python server!"