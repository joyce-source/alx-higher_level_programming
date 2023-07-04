#!/bin/bash
# Sends a GET request to URL and displays body of response (if code is 200)
response=$(curl -s -o /dev/null -w "%{http_code}" "$1")
[[ "$response" == "200" ]] && curl -s "$1" || echo "Unexpected response with status code: $response"
