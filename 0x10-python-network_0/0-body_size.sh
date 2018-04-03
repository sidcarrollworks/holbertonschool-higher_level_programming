#!/bin/bash
# get content length
curl -sI "$1" | awk '/Content-Length/ { print $2 }'
