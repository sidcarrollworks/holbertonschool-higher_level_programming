#!/bin/bash
# show methods
curl -sD - "$1" | awk '/Allow:/' | cut -c 8-
