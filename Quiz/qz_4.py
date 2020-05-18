#!/usr/bin/env python3

def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """
    n = len(L)
    maxSum = max(L)
    for i in range(n):
        for j in range(n-i):
            maxSum = max(maxSum, sum(L[i:i+j+1]))
    return maxSum