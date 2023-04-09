# Git Setup
Scripts for setting up git repos on a new machine.

# Requirements
- [Requests](https://pypi.org/project/requests/) library

# Usage

1. Add your github [access token](https://docs.github.com/en/enterprise-server@3.4/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) in config.toml. Ensure that this token has permissions to read repositories.
2. `python clone_repos.py <path>` to clone all repositories under <path>. 
