#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL and displays the
body of the response (decoded in utf-8).
"""
import urllib.request
import sys
from urllib.error import HTTPError


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except HTTPError as e:
        print("Error code: {}".format(e.code))
