from fastapi import FastAPI
from fastapi.routing import APIRoute
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from typing import Optional, Union, Any, List
from fastapi.middleware.cors import CORSMiddleware
import json
from anyio.streams.file import FileWriteStream
import datetime
from supabase.client import create_client, Client
from dotenv import dotenv_values
from prisma_client import Prisma
from prisma_client.models import Items
from prisma_client.types import ItemsCreateInput

secrets = dotenv_values(".env")
prisma = Prisma()

url: Union[str, None] = secrets.get("SUPABASE_URL")
key: Union[str, None] = secrets.get("SUPABASE_KEY")
if not url or not key:
    raise ValueError("Please create a .env file with your SUPABASE_URL and SUPABASE_KEY")

supabase: Client = create_client(url, key)

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

class ResponseMessage(BaseModel):
    message: str

@app.on_event("startup")
async def startup():
    await prisma.connect()
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
async def create_item(item: Items):
    json_compatible_data = jsonable_encoder(item, exclude_none=True)
    await prisma.items.create(json_compatible_data)
    supabase.from_("items").select().execute()
    return {"message": "item inserted"}


@app.get("/api/items", response_model=list[Items], tags=["items"])
async def get_items():
    # write your queries here
    items: List[Items] = await prisma.items.find_many(where={"name": {"contains": "it"}})
    return items

@app.get("/api/python", response_model=str)
async def get_hello():
    return "Hello, I'm a Python server!"