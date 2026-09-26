from fastapi import FastAPI

app = FastAPI(
    title="TajikGuide AI",
    description="AI Travel Platform for Tajikistan",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to TajikGuide AI",
        "status": "running"
    }

@app.get("/health")
def health():
    return {
        "status": "ok"
    }
