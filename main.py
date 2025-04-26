from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from .db.database import create_db
from .routers import player


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up...")
    create_db()

    yield
    print("Shutting down...")
    

app = FastAPI(lifespan=lifespan)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(player.router)