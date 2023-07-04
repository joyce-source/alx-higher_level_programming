#!/usr/bin/python3
"""
This script uses the requests package to fetch a URL and display the body of the response.
"""
import urllib.request

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    with urllib.request.urlopen(url) as response:
        body = response.read().decode('utf-8')

    print("Body response:")
    print("    - type: {}".format(type(body)))
    print("    - content: {}".format(body))
