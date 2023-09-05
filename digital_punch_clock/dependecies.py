from os.path import join, dirname, realpath
import asyncio
import asyncpg
from fastapi.templating import Jinja2Templates

_JINJA = None


async def get_jinja_env():
    global _JINJA
    if not _JINJA:
        dir_templates = join(dirname(realpath(__file__)), 'templates')
        _JINJA = Jinja2Templates(dir_templates)

    return _JINJA



async def run():
    print('conectando ...')

    conn = await asyncpg.connect(
        user='postgres',
        password='sWoiCMX3j30seiE5YhDy',
        database='punchclock3',
        #host='punchclock3.csix0yevpcqs.sa-east-1.rds.amazonaws.com',
        host='18.228.200.22',
        port=5432,
        timeout=30
    )

    print('CONECTADO')

    # values = await conn.fetch(
    #     'SELECT * FROM mytable WHERE id = $1',
    #     10,
    # )

    await conn.close()

#loop = asyncio.get_event_loop()
#loop.run_until_complete(run())