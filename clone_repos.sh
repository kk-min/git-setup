#!/usr/bin/env bash
eval `ssh-agent`
token=$(grep -oP "(?<=\")(.*)(?=\")" config.toml)
curl -H "Accept: application/vnd.github.v3+json" -H "Authorization: token $token" https://api.github.com/user/repos | jq -r '.[] | .ssh_url' | while read url; do git clone $url $1; done
