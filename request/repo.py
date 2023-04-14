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
                        description
                        issueCount: issues(states:OPEN) {{
                            totalCount
                        }}
                        last5Issues: issues(last:5) {{
                            nodes {{
                                    title
                            }}
                        }}
                    }}
                }}
            """
        }
        async with session.post('https://api.github.com/graphql', headers=headers, data=json.dumps(data)) as response:

            html = await response.text()
            data = json.loads(html).get('data', {}).get('repository', {})
            if data:
                result = {
                    'Repository name': data['name'],
                    'Repository description': data['description'],
                    'Number of open issues': data['issueCount']['totalCount'],
                    'A list of the 5 most recent issue titles': data['last5Issues']['nodes']
                }
            else:
                result = {
                    'Repository name': repo,
                    'Error description': "This name is not a correct name."
                }
            return result
