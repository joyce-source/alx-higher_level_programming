#!/bin/bash
# Sends a DELETE request to a URL and displays the body of the response

URL=$1
curl -s -X DELETE "$URL"

