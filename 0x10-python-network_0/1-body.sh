#!/bin/bash
# Sends a GET request to URL and displays body of response (if code is 200)

URL=$1
STATUS=$(curl -s -o /dev/null -w "%{http_code}" "$URL")
if [ "$STATUS" -eq 200 ]; then
    curl -s "$URL"
fi

