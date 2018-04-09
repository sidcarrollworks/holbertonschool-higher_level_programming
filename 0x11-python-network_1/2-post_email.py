#!/usr/bin/python3
''' send post request '''

if __name__ == "__main__":
    from urllib.request import urlopen, Request
    from urllib.parse import urlencode
    from sys import argv
    url = argv[1]
    values = {'email': argv[2]}

    data = urlencode(values).encode("UTF-8")
    req = Request(url, data)
    with urlopen(req) as r:
        print(r.read().decode("UTF-8"))
