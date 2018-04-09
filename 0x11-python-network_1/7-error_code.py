#!/usr/bin/python3
''' print error code '''

if __name__ == "__main__":
    import requests
    from sys import argv

    r = requests.get(argv[1])
    code = r.status_code
    if code >= 400:
        print("Error code: {}".format(code))
    else:
        print(r.text)
