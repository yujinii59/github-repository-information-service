from request import account
from request import repo

import asyncio

user = account.User()
username = user.get_username()
print(username)

data = asyncio.run(repo.get_repository_info(username, "github-repository-information-service"))
print(data)