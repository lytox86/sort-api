#!/usr/bin/env python3


import uvicorn
from fastapi import FastAPI

from src.api.root_router import root_router
from src.api.sort_router import sort_router

app = FastAPI()

app.include_router(sort_router, prefix="/api/v1")
app.include_router(root_router)

if __name__ == "__main__":
    uvicorn.run("src.app:app", port=8000, reload=True)
