#!/bin/python
# -*- coding: utf-8 -*-

# Start sun 10 may 2015 23:59
# pause on mon 11 may 2015 00:11

# End  sun 10 may 2015 XXXXXXX

import collections

def solver(input_values):
    ordered_dict = {}
    for value in input_values:
        key = int(str(value)[0])
        if not ordered_dict.has_key(key):
            ordered_dict[key] = []
        # allways append
        ordered_dict[key].append(value)

    return ordered_dict

if __name__ == "__main__":

    input_values = [50, 200, 2, 1, 10 , 9, 90]
    high_number = solver(input_values)
    print high_number
