from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Receipt Processor ")

app.include_router(router)

@app.get("/")
async def root():
    return {"message": "Receipt Processor API"}