#!/bin/bash
# Sends a request to URL and displays the size of the response body in bytes

URL=$1
curl -sI "$URL" | grep -i Content-Length | awk '{print $2}'

