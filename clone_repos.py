import sys
import os
from github_api import get_repos

args = sys.argv[1:]
if len(args) != 1:
    print('Usage: python clone_repos.py <path>')
    sys.exit(1)

path = args[0]
repos = get_repos()

for repo in repos:
    name = repo['name']
    url = repo['clone_url']
    print(f'Cloning repository {name}...')
    os.system(f'git clone {url} {path}/{name}')
