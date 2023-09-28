#!/bin/bash
# A scrept tha send a request to give 'URL'.
curl -s /dev/null -w "%{http_code}" "$1"
