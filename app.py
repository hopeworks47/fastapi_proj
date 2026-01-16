from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import router as api_router
# from pydantic import BaseModel, BaseSettings
# from typing import List
# import logging

# Setting
class Settings():
    app_name: str = "FastAPI Application"
    debug: bool = True

    class Config:
        env_file = ".env"

settings = Settings()

# Logging
# logging.baseConfig(
#     level=logging.INFO,
#     formart="%(asctime)s | %(levelname)s | %(name)s - %(message)s",
# )
# logger = logging.getLogger(__name__)

app = FastAPI(title=settings.app_name, debug=settings.debug)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api", tags=["api"])
