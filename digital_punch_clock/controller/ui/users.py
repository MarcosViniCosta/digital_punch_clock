from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter(prefix='/usuarios')


@router.get('', response_class=HTMLResponse)
async def get_users():
    return 'Olá mundo!'
