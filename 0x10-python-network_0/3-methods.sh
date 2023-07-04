#!/bin/bash
# This script displays all HTTP methods accepted by the server for a given URL
curl -s -X OPTIONS -i "$1" | awk '/^Allow:/ {print substr($0, 8)}'
