from fastapi import FastAPI
from backend.database import init_db

app = FastAPI(title="AI News Aggregator")

@app.on_event("startup")
async def startup():
    await init_db()

@app.get("/")
async def root():
    return {"message": "Here's the AI News Aggregator"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)