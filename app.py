from flask import Flask
from request import account
from request import repo

import asyncio

# get username by token
user = account.User()
username = user.get_username()
print(username)
# generate flask api
app = Flask(__name__)


@app.route('/<repository_names>', methods=['POST', 'GET'])
def repository_info(repository_names):
    # split repository names
    repositories = repository_names.split(',')

    # get repository information asynchronously
    result = asyncio.run(repo.get_repositories_info(username, repositories))
    print(result)
    return result


if __name__ == '__main__':
    app.run(debug=True)
