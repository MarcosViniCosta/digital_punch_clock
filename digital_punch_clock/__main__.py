
from fastapi import FastAPI
from uvicorn import run
from controller.ui.index import router
from controller.ui.users import router as router_users

if __name__ == '__main__':
    app = FastAPI()
    app.include_router(router)
    app.include_router(router_users)
    run(app=app, host='0.0.0.0', port=8081)

