#Prasad Hanwadikar - CS519 - HW1

from random import *

def sort(a):
    if a == []:
        return []
    else:
        r = randint(0, len(a)-1)
        a[0], a[r] = a[r], a[0]
        pivot = a[0]
        left = [x for x in a if x < pivot]
        right = [x for x in a[1:] if x >= pivot]
        return [sort(left)] + [pivot] + [sort(right)]

def sorted(t):
    if t == []:
        return []
    else:
        return sorted(t[0]) + [t[1]] + sorted(t[2])

def search(t, x):
    if t == []:
        return False
    else:
        if t[1] == x:
            return True
        elif t[1] < x:
            return search(t[2], x)
        else:
            return search(t[0], x)

def insert(t, x):
    if t == []:
        t = [[], x, []]
    else:
        if t[1] < x:
            t[2] = insert(t[2], x)
        elif t[1] > x:
            t[0] = insert(t[0], x)
    return t


