from request import account
from request import repo

import asyncio
from flask import Blueprint

user = account.User()

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route("/<repo_list>", methods=['GET', 'POST'])
def repository_info(repo_list):
    """

    :param repo_list: list of repository name
    :return: list of repository information
    """
    username = user.get_username()

    # split repository names
    repositories = repo_list.split(',')

    # get repository information asynchronously
    results = asyncio.run(repo.get_repositories_info(username, repositories))

    return results
