import json
import requests

from config import config


class User(object):
    def __init__(self):
        self.header = {'Authorization': 'bearer ' + config.TOKEN}

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
