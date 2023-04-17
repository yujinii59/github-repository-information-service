from aiohttp import web

import aiohttp_router

app = web.Application()
app.add_routes([web.get('/api/{repo_names}', aiohttp_router.repository_info)])

if __name__ == '__main__':
    web.run_app(
        app=app,
        host='0.0.0.0',
        port=8080
    )
