#!/usr/bin/python3
def best_score(my_dict):
    if my_dict:
        return None
    num = max(zip(my_dict.values(), my_dict.keys()))
    return num[1]
