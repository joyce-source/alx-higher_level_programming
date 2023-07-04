#!/usr/bin/python3
"""
This script uses the requests package to fetch a URL and display the body of the response.
"""
import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    response = requests.get(url)
    body = response.text

    print("Body response:")
    print("    - type: {}".format(type(body)))
    print("    - content: {}".format(body))
