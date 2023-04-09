import requests

def get_repos(user_name):
    url = 'https://api.github.com/user/repos'
    res = requests.get(url)
    repos = response.json()
    return repos


