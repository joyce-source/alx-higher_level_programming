#!/bin/bash
# Sends a GET request to a URL with custom header and displays body of response
curl -s -H "X-School-User-Id: 98" "$1"
