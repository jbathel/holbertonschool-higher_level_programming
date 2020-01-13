#!/usr/bin/python3
# Python script that fetches https://intranet.hbtn.io/status

if __name__ == '__main__':
    import requests
    import sys

    r = requests.get(sys.argv[1])
    print(r.headers['X-Request-Id'])
