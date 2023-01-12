import uvicorn
from fastapi import FastAPI, APIRouter
import api
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api.router)

if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000)
