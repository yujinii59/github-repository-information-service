from aiohttp import web

from request import account
from request import repo

user = account.User()


async def repository_info(request):
    username = user.get_username()
    repo_list = request.match_info.get('repo_names', "")
    repositories = repo_list.split(',')
    text = await repo.get_repositories_info(username=username, names=repositories)

    return web.json_response(data=text)
