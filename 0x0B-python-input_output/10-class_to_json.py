#!/usr/bin/python3
import json

def class_to_json(obj):
	return getattr(obj, '__dict__')
