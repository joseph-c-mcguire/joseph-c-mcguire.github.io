from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI(
    title="Joseph McGuire Backend",
    description="Backend services for personal website",
    version="0.1.0",
)

# Enable CORS for frontend requests
origins = [
    "http://localhost:3000",
    "http://localhost:4321",
    os.getenv("FRONTEND_URL", "https://www.example.com"),
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Backend is running"}

@app.get("/api/health")
async def health():
    return {"status": "healthy"}

# Example endpoint for background tasks
@app.post("/api/tasks")
async def create_task(task: dict):
    """Create and queue a background task"""
    return {"id": "task-123", "status": "queued", "task": task}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
