from fastapi import FastAPI
from routes import router  # Import the router from routes.py
import uvicorn

app = FastAPI(title="Stock Market Monitor API")

# Include the router with all your endpoints (from routes.py)
app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Stock Market Monitor API"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)