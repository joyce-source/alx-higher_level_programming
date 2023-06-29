#!/bin/bash
# Sends a GET request to a URL with custom header and displays body of response

URL=$1
curl -s -H "X-School-User-Id: 98" "$URL"

