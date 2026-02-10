"""FastAPI main application module."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router as api_router
from app.core.config import settings

app = FastAPI(
    title="${{ values.name }}",
    description="FastAPI application created via Backstage",
    version="1.0.0",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(api_router, prefix="/api")


@app.get("/health")
async def health_check():
    """Health check endpoint for Kubernetes probes."""
    return {
        "status": "healthy",
        "service": "${{ values.name }}",
        "version": "1.0.0"
    }


@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "message": "Welcome to ${{ values.name }}",
        "docs": "/docs",
        "health": "/health"
    }
