#!/usr/bin/python3
"""
script that takes 2 arguments:
    - The first argument will be the repository name.
    - The second argument will be the owner name.
"""
import sys
import requests


if __name__ == "__main__":

    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'

    res = requests.get(url)
    res = res.json()
    try:
        for i in range(10):
            print(f"{res[i].get('sha')}: {res[i]['commit']['author']['name']}")
    except IndexError:
        pass
