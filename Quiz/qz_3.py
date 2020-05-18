#!/usr/bin/env python3

def greedySum(L, s):
    """ input: s, positive integer, what the sum should add up to
               L, list of unique positive integers sorted in descending order
        Use the greedy approach where you find the largest multiplier for 
        the largest value in L then for the second largest, and so on to 
        solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
        return: the sum of the multipliers or "no solution" if greedy approach does 
                not yield a set of multipliers such that the equation sums to 's'
    """

    n = len(L)
    m = [0 for i in range(n)]

    tempSum = s
    for i in range(n):
        m[i]     = int(tempSum/L[i])
        tempSum -= m[i]*L[i]
    if tempSum == 0:
        return sum(m)
    return "no solution"