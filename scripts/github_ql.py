"""Helper to request GitHub GraphQL API."""
import os
from typing import Iterator, Optional

import requests


def _run_query(query: str) -> dict:
    """Run a GraphQL request on GitHub API
    
    A API token must be set as environment variable GITHUB_TOKEN
    """
    TOKEN = os.environ.get("GITHUB_TOKEN")
    if TOKEN is None:
        raise ValueError("GITHUB_TOKEN key API is undefined.")

    request = requests.post('https://api.github.com/graphql', json={'query': query}, headers={"Authorization": f"Bearer {TOKEN}"})

    if request.ok:
        return request.json()
    else:
        raise ValueError("Query failed to run by returning code of {}. {}".format(request.status_code, query))


def get_tags(owner: str, repo: str, n: int = 100, filter: Optional[str] = None) -> Iterator[str]:
    """Get the tags on a repository in descending commit tag date order."""

    ref_query = ""
    if filter is not None:
        ref_query = f', query: "{filter}"'

    # Use GraphQL to get tag by commit date and not by alphabetical order
    query = f"""
    {{
        repository(owner: "{owner}", name: "{repo}") {{
            refs(refPrefix: "refs/tags/"{ref_query}, first: {min(100, n)}, orderBy: {{field: TAG_COMMIT_DATE, direction: DESC}}) {{
                edges {{
                    node {{
                        name
                    }}
                }}
            }}
        }}
    }}
    """

    data = _run_query(query)

    return map(lambda n: n["node"]["name"], data["data"]["repository"]["refs"]["edges"])
