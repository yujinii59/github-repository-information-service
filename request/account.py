import json
import requests

import common


class User(object):
    def __init__(self):
        self.header = common.github_graphql_header

    def get_username(self):
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

        username = request.json()['data']['viewer']['login']

        return username
