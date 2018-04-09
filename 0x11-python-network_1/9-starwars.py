#!/usr/bin/python3
''' search star wars api '''

if __name__ == "__main__":
    import requests
    from sys import argv

    search = argv[1]

    r = requests.get('https://swapi.co/api/people/', params={'search': search})
    data = r.json()
    print("Number of results: {}".format(data.get("count")))
    for x in data['results']:
        print(x.get('name'))
