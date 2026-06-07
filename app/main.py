from fastapi import FastAPI, Depends

from app.config import get_settings, Settings
app = FastAPI()

# Depends(get_settings). Dependency
# Depends variable depends on the result of get_settings. The value returned is then assigned to the settings parameter
@app.get("/ping")
async def pong(settings: Settings = Depends(get_settings)):
    return {
        "ping": "pong!",
        "environment": settings.environment,
        "testing": settings.testing
    }

