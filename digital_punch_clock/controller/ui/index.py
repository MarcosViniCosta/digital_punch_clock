from fastapi import APIRouter, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from dependecies import get_jinja_env

router = APIRouter(prefix='')


@router.get('/', response_class=HTMLResponse)
async def get_index(
        request: Request,
        jinja_env: Jinja2Templates = Depends(get_jinja_env)
):
    return jinja_env.TemplateResponse('index.html', {'request': request, 'user_name': 'Marcos Vinicius'})


@router.get('/favicon.ico')
async def get_favicon():
    return 'Ola mundo!!!!'
