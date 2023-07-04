#!/usr/bin/python3
"""
This script sends a request to a URL and displays the value of the X-Request-Id variable.
"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        header = response.headers
        request_id = header.get('X-Request-Id')

    print(request_id)
