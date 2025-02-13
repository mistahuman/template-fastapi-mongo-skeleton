from fastapi import FastAPI
from app.routers import exampleitem
from fastapi.middleware.cors import CORSMiddleware
import logging 
import uvicorn
from app.conf.config import setup_advanced_logging, Config

# Logging
conf_logger = setup_advanced_logging()
logger = logging.getLogger("main")

# FastAPI
logger.info(f"Starting FastAPI: {Config.title}-{Config.version}")
app = FastAPI(redirect_slashes=False)

# Add CORS middleware to allow all origins, headers, and methods
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)

# Routing
app.include_router(exampleitem.router, tags=["exampleitems"])

# Main route
@app.get("/")
def root():
    return {"msg": f"Hello {Config.title or 'World'}!"}

# Main for debugging
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)