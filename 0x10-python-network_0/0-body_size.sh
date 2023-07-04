#!/bin/bash
# Sends a request to URL and displays the size of the response body in bytes
curl -s "$1" | grep -oP 'GET \/ => "\K[^"]+'
