#!/usr/bin/python3
''' Print error code '''

if __name__ == "__main__":
    from urllib.request import Request, urlopen
    from urllib.error import HTTPError
    from sys import argv

    try:
        with urlopen(Request(argv[1]) as r:
            print(r.read().decode("UTF-8"))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
