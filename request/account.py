import json
import requests

import common
from exception.custom_exception import TokenException


class User(object):
    def __init__(self):
        self.header = common.github_graphql_header
        self.username = ''

    def get_username(self):
        if self.username != '':
            return self.username
        data = {'query': """
                        query {
                            viewer {
                                login
                            }
                        } 
                    """
                }
        request = requests.post(url='https://api.github.com/graphql',
                                headers=self.header,
                                data=json.dumps(data))

        username = request.json().get('data', {}).get('viewer', {}).get('login', '')

        if username == '':
            raise TokenException()
        return username
