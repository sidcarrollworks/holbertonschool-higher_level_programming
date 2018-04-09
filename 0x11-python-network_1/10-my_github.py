#!/usr/bin/python3
''' github api '''

if __name__ == "__main__":
    import requests
    from sys import argv
    from requests.auth import HTTPBasicAuth
    r = requests.get('https://api.github.com/users/{}'.format(argv[1]),
                     auth=HTTPBasicAuth(argv[1], argv[2]))
    json = r.json()
    print(json.get('id'))
