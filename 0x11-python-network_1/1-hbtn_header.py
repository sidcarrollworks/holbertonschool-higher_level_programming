#!/usr/bin/python3
''' display x-request-id '''

if __name__ == "__main__":
    from urllib.request import urlopen
    from sys import argv
    with urlopen(argv[1]) as r:
        print(r.headers.get("X-Request-Id"))
