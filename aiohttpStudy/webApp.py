# coding='utf-8'
from aiohttp import web


async def home(request: web.Request) -> web.Response:
    return web.Response(text="Hi")


async def init_app() -> web.Application:
    app = web.Application()
    app.add_routes([web.get("/", home)])
    return app


web.run_app(init_app(), port=5000, host="127.0.0.1")
