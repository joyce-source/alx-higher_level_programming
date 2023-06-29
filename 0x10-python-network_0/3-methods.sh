#!/bin/bash
# This script displays all HTTP methods accepted by the server for a given URL

URL=$1
curl -sI "$URL" | awk '/Allow:/ {print substr($0, index($0,$2))}'

