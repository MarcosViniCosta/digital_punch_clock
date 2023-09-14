from os.path import join, dirname, realpath

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from uvicorn import run
from controller.ui.index import router
from controller.ui.users import router as router_users

if __name__ == '__main__':
    dir_static = join(dirname(realpath(__file__)), 'templates','images')
    app = FastAPI()
    app.include_router(router)
    app.include_router(router_users)
    app.mount(
        f'/assets',
        StaticFiles(directory=dir_static),
        'assets'
    )
run(app=app, host='0.0.0.0', port=8081)
