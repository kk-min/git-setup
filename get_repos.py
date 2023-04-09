import requests

def get_repos(user_name):
    url = 'https://api.github.com/user/repos'
    headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json"
            }
    res = requests.get(url, headers=headers)
    repos = response.json()
    return repos


