#!/bin/bash
# Sends a GET request to URL and displays body of response (if code is 200)
curl -s -o /dev/null -w "%{http_code}" "$1" | grep -q "200" && curl -s "$1" | sed '1,/^$/d'
