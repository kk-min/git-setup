#!/usr/bin/env bash
if [[ $# -ne 1 ]]; then
	echo "Usage: ./clone_repos.sh <path>"
	exit 1
fi
eval `ssh-agent`
curr_dir=$(pwd)
token=$(grep -oP "(?<=\")(.*)(?=\")" config.toml)
cd $1
if [[ $? -ne 0 ]]; then
	echo "Error: $1 is not a valid directory; ensure that target directory exists"
	exit 1
fi
curl -H "Accept: application/vnd.github.v3+json" -H "Authorization: token $token" https://api.github.com/user/repos | jq -r '.[] | .ssh_url' | while read url; do git clone $url; done
cd $curr_dir
