import aiohttp
import json

import common

headers = common.github_graphql_header


async def get_repository_info(username, repo):
    async with aiohttp.ClientSession() as session:
        data = {
            "query": f"""
                query {{
                    repository(owner: "{username}", name: "{repo}") {{
                        name
                    }}
                }}
            """
        }
        async with session.post('https://api.github.com/graphql', headers=headers, data=json.dumps(data)) as response:
            print("Status:", response.status)
            html = await response.text()
            data = json.loads(html).get('data', {})
            print('data: ', data)

            return data
