#!/bin/python
# -*- coding: utf-8 -*-

# Start sun 10 may 2015 23:42
# End  sun 10 may 2015 23:52

def fib_rec(fib_n):

    if fib_n == 0:
        sol = [0]
    if fib_n == 1:
        sol = [0,1]
    else:
        count = 0
        sol = [0, 1]
        for index in range( 2, fib_n-1):
            sol.append(     sol[index - 1] + sol [index - 2])

    return sol


if __name__ == "__main__":

    sol = fib_rec (100)
    print sol
