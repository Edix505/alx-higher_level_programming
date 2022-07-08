#!/usr/bin/python3
def best_score(a_dict):
    "return a with maximum value"
    if a_dict and len(a_dict):
        maximum = list(a_dict.keys())[0]
        for a in a_dict:
            if a_dict[a] > a_dict[maximum]:
                maximum = a
        return maximum
    return None
