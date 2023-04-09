import requests
import tomllib

def read_config():
    with open('config.toml', "rb") as f:
        cfg = tomllib.load(f)
    return cfg 

config = read_config()

def get_repos():
    url = 'https://api.github.com/user/repos'
    headers = {
            "Authorization": f"token {config['token']}",
            "Accept": "application/vnd.github.v3+json"
    }
    res = requests.get(url, headers=headers)
    repos = res.json()
    return repos

print(get_repos())
