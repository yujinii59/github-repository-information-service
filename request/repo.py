import aiohttp
import json
import asyncio

import common

headers = common.github_graphql_header


async def get_repository_info(session, username, repo):
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
        print("Status:", response.status)
        html = await response.text()
        json_data = json.loads(html)
        data = json_data.get('data', {}).get('repository', {})
        print('data: ', data)
        if data:
            result = {
                'Repository name': data['name'],
                'Repository description': data['description'],
                'Number of open issues': data['issueCount']['totalCount'],
                'A list of the 5 most recent issue titles': data['last5Issues']['nodes']
            }
        else:
            result = json_data
            return {"error":"repository not found",
                    "Repository name": repo}
        return result


async def get_repositories_info(username, names):
    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(
            *[get_repository_info(session, username, name) for name in names]
        )

        return results
