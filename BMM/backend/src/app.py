from fastapi import FastAPI, responses, requests
from fastapi.middleware.cors import CORSMiddleware
from .routes import content_router

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:5174"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(content_router.router, prefix="/api")