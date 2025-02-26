from fastapi import FastAPI
from routes import router  # Import the router from routes.py
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# Initialize the FastAPI app
app = FastAPI(title="Stock Market Monitor API")

origins = [
    "http://localhost:3000",
    "http://localhost",
    "http://localhost:8080",
]

# Add CORS middleware to allow requests from a specific origin (e.g., localhost:3000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allow the frontend on localhost:3000
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Include the router with all your endpoints (from routes.py)
app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Stock Market Monitor API"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)