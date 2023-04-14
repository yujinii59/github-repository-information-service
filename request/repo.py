import aiohttp
import json
import asyncio
from typing import List

import common

headers = common.github_graphql_header


async def get_repository_info(session, username: str, repo: str):
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
        json_data = json.loads(html)
        data = json_data.get('data', {}).get('repository', {})

        if data:
            result = {
                'Repository name': data['name'],
                'Repository description': data['description'],
                'Number of open issues': data['issueCount']['totalCount'],
                'A list of the 5 most recent issue titles': data['last5Issues']['nodes']
            }
        else:
            result = json_data
            return {"error": "repository not found",
                    "Repository name": repo}
        return result


async def get_repositories_info(username: str, names: List[str]):
    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(
            *[get_repository_info(session, username, name) for name in names]
        )

        return results
