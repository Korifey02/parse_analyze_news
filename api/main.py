from fastapi import FastAPI, APIRouter
import asyncio
import api
# from db import DBConnection

app = FastAPI()
# db = DBConnection()
app.include_router(api.router)


