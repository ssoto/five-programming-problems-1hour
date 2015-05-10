#!/bin/python
# -*- coding: utf-8 -*-

# starts at 20:28 sun 10 may
# end at 21:12 sun 10 may

# DO IT FOR-EACH WAY:
#     METHOD=0
# WHILE WAY:
#    METHOD=1
# RECURSIVE WAY:
# METHOD=2
METHOD=2

def for_loop (array):
    for element in array:
        print "element " , array.index(element) , " => " , str(element)

def while_loop (array):
    for i in range (0, len(array)+1):
        print array[i]

def for_recursive(array, depth=0):

    if len(array) == 1:
        print array[0]
    elif len(array) == 2:
        for_recursive( [array[0]], depth)
        for_recursive( [array[1]], depth)
    else:
        for_recursive( [array[0]], depth)
        for_recursive( array[1:len(array)-1], depth)

if __name__ == "__main__":

    array = (0,1,2,3,4,5)
    if METHOD == 0:
        for_loop (array)
    elif METHOD == 1:
        for_loop (array)
    elif METHOD == 2:
        for_recursive(array)
    else:
        print "Error. Method only can be 0,1 or 2"
