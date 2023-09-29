#!/bin/bash
# A scrept tha send a request to give 'URL'.
curl -s -o /dev/null -w "%{http_code}" "$1"
