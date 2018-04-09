#!/usr/bin/python3
'''search an api'''

if __name__ == "__main__":
    import requests
    from sys import argv
    try:
        q = argv[1]
    except:
        q=""
    r = requests.get('https://api.github.com/events')
    r.json()
    print(r)
