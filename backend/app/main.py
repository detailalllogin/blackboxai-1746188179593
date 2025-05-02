from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Bilingual Astrology API")

# Allow CORS for frontend development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from .api_routes import router as api_router

@app.get("/")
async def root():
    return {"message": "Welcome to the Bilingual Astrology API"}

app.include_router(api_router, prefix="/api")
