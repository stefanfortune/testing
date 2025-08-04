from fastapi import FastAPI, responses, requests
from fastapi.middleware.cors import CORSMiddleware
from src.routes import content_router

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(content_router.router, prefix="/api")



