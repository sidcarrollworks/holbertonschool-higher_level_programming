#!/bin/bash
# send post

curl -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" -X POST "$1"
