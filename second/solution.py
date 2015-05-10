#!/bin/python
# -*- coding: utf-8 -*-

# starts at 23:23 sun 10 may
# end at 23:40 sun 10 may

def get_sol(array1, array2):
    sol = []
    for index in range(0, len(array1) - 1):
        sol.append(array1[index])
        sol.append(array2[index])
    return sol


if __name__ == "__main__":
    array1 = [0,1,2,3,4,5]
    array2 = ['a', 'b', 'c', 'd', 'e', 'f']
    print "Inputs: \n\tarray1 => ", array1, "\n\tarray2 => ", array2
    sol = get_sol(array1, array2)
    print sol
