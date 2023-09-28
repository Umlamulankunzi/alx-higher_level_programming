#!/bin/bash
# sends a request to passed & displays only the status code of response
curl -s -o /dev/null -w "%{http_code}" "$1"
