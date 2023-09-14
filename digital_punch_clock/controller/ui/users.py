from fastapi import APIRouter, Depends
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates

from dependecies import get_jinja_env

router = APIRouter(prefix='/usuarios')


@router.get('', response_class=HTMLResponse)
async def get_users(request: Request, jinja_env: Jinja2Templates = Depends(get_jinja_env)):
    return jinja_env.TemplateResponse('users/users.html', {'request': request})
