#!/usr/bin/python3
'''search an api'''

if __name__ == "__main__":
    import requests
    from sys import argv
    import sys
    try:
        q = argv[1]
    except:
        q = ""
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        json = r.json()
        if len(json) == 0:
            print("No result")
        else:
            ID = json.get('id')
            NAME = json.get('name')
            print("[{}] {}".format(ID, NAME))
    except:
        print("Not a valid JSON")
