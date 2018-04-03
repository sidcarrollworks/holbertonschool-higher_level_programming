#!/bin/bash
#post json file
curl -H "Content-Type: application/json" -X POST -d @"$2" "$1"
