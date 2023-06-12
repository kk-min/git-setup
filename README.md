# Git Setup
_Copyright © 2023 kk-min_

Scripts for setting up git repos on a new machine.

## Requirements

**Python:**
- [Requests](https://pypi.org/project/requests/) library: `pip install requests`

**Bash:**
- [jq](https://jqlang.github.io/jq/) cli JSON processor: `sudo apt-get install jq` for Ubuntu/Debian systems, or via your distro's package manager

## Usage

1. Add your github [access token](https://docs.github.com/en/enterprise-server@3.4/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) in config.toml. Ensure that this token has permission to read repositories. If setting up a fine-grained token, ensure that it has read access to repository metadata at minimum to read private repos.
2. To clone all repositories under `<path>`,
- **Python:** `python clone_repos.py <path>`
- **Bash:** `./clone_repos.sh <path>` (You may need to make the file executable using `chmod +x ./clone_repos.sh`)
