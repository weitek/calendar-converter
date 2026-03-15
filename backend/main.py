import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from routers import convert, widgets
from config import settings

# Загрузка переменных окружения
load_dotenv()

app = FastAPI(
    title="Calendar Converter API",
    description="API для конвертации дат между различными календарями",
    version="1.0.0"
)

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключение роутеров
app.include_router(widgets.router, prefix="/api", tags=["widgets"])
app.include_router(convert.router, prefix="/api", tags=["convert"])

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "ok", "service": "backend"}

@app.get("/")
async def root():
    return {"message": "Calendar Converter API"}
