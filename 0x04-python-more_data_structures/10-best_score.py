#!/usr/bin/python3
def best_score(a_dictionary):
    max_score = None
    max_key = None
    if not a_dictionary:
        return max_score
    for key, val in a_dictionary.items():
        if max_score and val > max_score:
            max_score = val
            max_key = key
        elif max_score is None:
            max_score = val
            max_key = key
    return max_key
