#Prasad Hanwadikar - CS519 - HW1

from random import *

def qselect(k, a):
    if a == [] or k < 1 or k > len(a):
        return 'Either list is empty or k is invalid'
    else:
        r = randint(0, len(a)-1)
        a[0], a[r] = a[r], a[0]
        pivot = a[0]
        left = [x for x in a if x < pivot]
        right = [x for x in a[1:] if x >= pivot]
        if len(left) == k-1:
            return pivot
        elif len(left) > k-1:
            return qselect(k, left)
        else:
            k = k - len(left) - 1
            return qselect(k, right)
