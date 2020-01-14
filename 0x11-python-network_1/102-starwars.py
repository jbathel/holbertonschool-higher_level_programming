#!/usr/bin/python3
"""
Write a Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
if __name__ == '__main__':
    import requests
    import sys
    r = requests.get(
        'https://swapi.co/api/people', params={'search': sys.argv[1]})
    data = r.json()
    if data:
        print("Number of results: {}".format(data['count']))
        for item in data['results']:
            print(item['name'])
