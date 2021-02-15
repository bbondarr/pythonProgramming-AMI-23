import random
from LinkedList import LinkedList

def isAlternation(lst):
    """Checks whether the list is a sequence of alternations f.e. [-3, 2, -1, 10] - True"""
    for i in range(1, len(lst)):
        if not ((lst[i-1] >= 0 and lst[i] < 0) 
            or (lst[i-1] < 0 and lst[i] >= 0)):
            return False
    return True

def alternationsReverse(lst):
    res = lst.copy()
    reservedIndexes = []
    k = len(lst); i = 0

    while k > 1:
        while i+k <= len(lst):
            if (isAlternation(lst[i:i+k]) 
                and not i in reservedIndexes): 

                print('ALTERNATION SUBLIST - ', lst[i:i+k])

                reservedIndexes += list(range(i, i+k))
                temp = lst[i:i+k]; temp.reverse()
                res[i:i+k] = temp                   
                i += k
            else: i += 1 
        k -= 1; i = 0
    
    return res