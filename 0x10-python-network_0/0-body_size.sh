#!/bin/bash
# Sends a request to URL and displays the size of the response body in bytes
curl -sI "$1" | grep -i "Content-Length" | awk '{print "Response size: " $2 " bytes"}'
