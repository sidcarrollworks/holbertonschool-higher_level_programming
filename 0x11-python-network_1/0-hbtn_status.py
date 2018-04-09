#!/usr/bin/python3
''' fetch a url '''

if __name__ == "__main__":
    from urllib.request import urlopen
    with urlopen('https://intranet.hbtn.io/status') as r:
        html = r.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode("UTF-8")))
