import requests
import yaml

def read_config():
    with open('config.yaml') as config_file:
        try:
            config = yaml.safe_load(config_file)
        except:
            print('Error reading config.yaml')
            exit(1)
    return config

def get_repos(user_name):
    url = 'https://api.github.com/user/repos'
    headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json"
    }
    res = requests.get(url, headers=headers)
    repos = response.json()
    return repos


