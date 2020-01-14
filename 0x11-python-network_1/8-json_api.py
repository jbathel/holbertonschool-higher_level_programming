#!/usr/bin/python3
"""
Write a Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
if __name__ == '__main__':
    import requests
    import sys

    data = {'q': ""}

    if len(sys.argv) > 1:
        data['q'] = sys.argv[1]
        r = requests.post('http://0.0.0.0:5000/search_user', data)
        try:
            data = r.json()
            if data:
                print("[{}] {}".format(data['id'], data['name']))
            else:
                print('No result')
        except Exception:
            print('Not a valid JSON')
