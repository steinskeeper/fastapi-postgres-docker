from fastapi import FastAPI

from app.auth.auth_routes import auth
from app.users.users_routes import users

from fastapi.middleware.cors import CORSMiddleware


import os


app = FastAPI()
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth)
app.include_router(users)


@app.get("/")
async def root():
    type = os.environ['TYPE']
    return {"message": "Server Ready",
            "type": type}
