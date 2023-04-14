import json
import requests

import common
from exception.custom_exception import TokenException


class User(object):
    def __init__(self):
        self.header = common.github_graphql_header
        self.username = None

    def get_username(self) -> str:
        """
        get username using graphQL
        :return: github login user name
        """
        # already got username
        if self.username is not None:
            return self.username

        data = {'query': """
                        query {
                            viewer {
                                login
                            }
                        } 
                    """
                }
        request = requests.post(
            url='https://api.github.com/graphql',
            headers=self.header,
            data=json.dumps(data)
        )

        username = request.json().get('data', {}).get('viewer', {}).get('login', None)
        self.username = username

        # username can't be obtained
        if username is None:
            raise TokenException()

        return username
