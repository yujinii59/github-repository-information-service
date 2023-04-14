from request import account
from request import repo

import asyncio
from flask import Blueprint

user = account.User()
username = user.get_username()

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route("/api/v1/<repo_list>", methods=['GET','POST'])
def repository_info(repo_list):
    # split repository names
    repositories = repo_list.split(',')

    # get repository information asynchronously
    results = asyncio.run(repo.get_repositories_infos(username, repositories))
    return results
