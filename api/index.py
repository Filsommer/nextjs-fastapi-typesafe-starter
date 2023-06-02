from fastapi import FastAPI, Request
from fastapi.routing import APIRoute
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from typing import Union, List
from fastapi.middleware.cors import CORSMiddleware
import json
from anyio.streams.file import FileWriteStream
import os
from .prisma import Prisma
from .prisma.models import Item, ItemCreator

print("INITTING PRISMA")

# url: Union[str, None] = os.environ.get('SUPABASE_URL')
# key: Union[str, None] = os.environ.get('SUPABASE_KEY')
# if not url or not key:
#     raise ValueError("Please create a .env file with your SUPABASE_URL and SUPABASE_KEY")


def custom_generate_unique_id(route: APIRoute):
    return f"{route.tags[0] if len(route.tags) > 0 else ''}-{route.name}"

app = FastAPI(generate_unique_id_function=custom_generate_unique_id)
prisma = Prisma()
is_production = os.getenv("DEBUG") != "1"

# TODO handle CORS, see: https://fastapi.tiangolo.com/tutorial/cors/
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ResponseMessage(BaseModel):
    message: str


@app.on_event("startup")
async def startup():
    await prisma.connect()
    print("STARTUP FASTAPI")
    # write openapi objects to file on startup
    async with await FileWriteStream.from_path("./api/openapi.json") as stream:
        jsonData = jsonable_encoder(app.openapi())
        for path_data in jsonData["paths"].values():
            for operation in path_data.values():
                operation_id = operation["operationId"]
                new_operation_id = operation_id.split("-")[1]
                operation["operationId"] = new_operation_id
        await stream.send(json.dumps(jsonData).encode("utf-8"))


@app.on_event("shutdown")
async def shutdown():
    await prisma.disconnect()
    print("SHUTDOWN FASTAPI")


@app.middleware("https")
async def middleware_ep(request: Request, call_next):
    if not is_production:
        response = await call_next(request)
    else:  # endpoints are lambdas on vercel, so we need to instantiate prisma on every request :(
        await prisma.connect()
        response = await call_next(request)
        await prisma.disconnect()
        response = await call_next(request)
    return response


@app.post("/api/items", response_model=ResponseMessage, tags=["items"])
async def create_item(item: ItemCreator):
    json_compatible_data = jsonable_encoder(item, exclude_none=True)
    await prisma.item.create(json_compatible_data)
    return {"message": "item inserted"}


@app.get("/api/items", response_model=list[Item], tags=["items"])
async def get_items():
    items = []
    items: List[Item] = await prisma.item.find_many()
    # write your queries here
    return items

@app.get("/api/python", response_model=str)
async def get_hello():
    return "Hello, I'm a Python server!"