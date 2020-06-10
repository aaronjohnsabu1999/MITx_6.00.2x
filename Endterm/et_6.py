import os
os.environ["OPENBLAS_NUM_THREADS"] = "1"
import numpy as np

def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int
 
    Returns result, a numpy.array of length len(choices) 
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total, 
    pick the one that gives sum(result*choices) closest 
    to total without going over.
    """
    def comboProduct(choices, combo):
        return sum([choices[i] * combo[i] for i in range(len(choices))])

    def int2bin(num, choices):
        numBin = bin(num).replace('0b', '')
        numArr = np.array([int(numBin[i]) for i in range(len(numBin))])
        while len(numArr) < len(choices):
            numArr = np.insert(numArr, 0, 0)
        return numArr

    combo = np.array([0 for i in range(len(choices))])
    secondChoice = np.array([0 for i in range(len(choices))])
    validCombo  = np.array([0 for i in range(len(choices))])
    maxVal = 2**len(choices)

    for i in range(maxVal):
        iArr    = int2bin(i, choices)
        product = comboProduct(choices, iArr)

        if product == total:
            if comboProduct(choices, validCombo) != total or sum(iArr) < sum(validCombo):
                validCombo = iArr
        elif product < total:
            if product > comboProduct(choices, secondChoice):
                secondChoice = iArr
    
    if comboProduct(choices, validCombo) == total:
        return validCombo
    else:
        return secondChoice

print(find_combination([1,2,2,3], 4))
print(find_combination([1,1,3,5,3], 5))
print(find_combination([1,1,1,9], 4))