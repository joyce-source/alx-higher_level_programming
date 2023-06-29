#!/bin/bash
# This script sends a POST request to a URL with variables in the request body and
# displays the response body

EMAIL="test@gmail.com"
SUBJECT="I will always be here for PLD"

curl -s -X POST -d "email=$EMAIL&subject=$SUBJECT" "$URL"

