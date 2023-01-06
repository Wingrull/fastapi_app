from fastapi import FastAPI
from app.handlers import router
import uvicorn


def get_app() -> FastAPI:
    application = FastAPI()
    application.include_router(router)
    return application


app = get_app()

if __name__ == "__main__":
    uvicorn.run("main:app", port=8080, host='0.0.0.0', reload=True)