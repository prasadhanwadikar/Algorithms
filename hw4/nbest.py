from random import *
from operator import itemgetter, attrgetter

def nbesta(a, b):
    if a == [] or b == []:
        return []
    tuple_list = []
    for i in a:
        for j in b:
            tuple_list += [(i+j, i, j)]
    tuple_list.sort(key=itemgetter(0, 2))
    tuple_list = tuple_list[:len(a)]
    return [(t[1], t[2]) for t in tuple_list]

def nbestb(a, b):
    if a == [] or b == []:
        return []
    tuple_list = []
    for i in a:
        for j in b:
            tuple_list += [(i+j, i, j)]
    tuple_list = qselect(len(a), tuple_list)
    tuple_list.sort(key=itemgetter(0, 2))
    return [(t[1], t[2]) for t in tuple_list]

def qselect(k, a):
    #r = randint(0, len(a) - 1)
    #a[0], a[r] = a[r], a[0]
    pivot = a[0]
    left = [x for x in a if x[0] < pivot[0] or (x[0] == pivot[0] and x[2] < pivot[2])]
    right = [x for x in a[1:] if x[0] > pivot[0] or (x[0] == pivot[0] and x[2] >= pivot[2])]
    if len(left) == k - 1:
        return left + [pivot]
    elif len(left) > k - 1:
        return qselect(k, left)
    else:
        k = k - len(left) - 1
        return left + [pivot] + qselect(k, right)

def nbestc(a, b):
    if a == [] or b == []:
        return []
    tuple_list = []
    a.sort()
    b.sort()
    i = j = 0
    for _ in range(len(a)):
        tuple_list.append((a[i] + b[j], a[i], b[j]))
        for r in range(i):
            tuple_list.append((a[r] + b[j], a[r], b[j]))
        for c in range(j):
            tuple_list.append((a[i] + b[c], a[i], b[c]))
        i += 1
        j += 1
    tuple_list.sort(key=itemgetter(0, 2))
    tuple_list = tuple_list[:len(a)]
    return [(t[1], t[2]) for t in tuple_list]

def nbestc2(a, b): #todo
    if a == [] or b == []:
        return []
    tuple_list = []
    a.sort()
    b.sort()
    i = j = 0
    while(len(tuple_list) < len(a)):
        r = c = 0
        while(r < i and c < j):
            if a[r] < b[c]:
                tuple_list.append((a[i] + b[j], a[i], b[j]))
                i += 1
        tuple_list.append((a[i] + b[j], a[i], b[j]))
        for r in range(i):
            tuple_list.append((a[r] + b[j], a[r], b[j]))
        for c in range(j):
            tuple_list.append((a[i] + b[c], a[i], b[c]))
        i += 1
        j += 1
    tuple_list.sort(key=itemgetter(0, 2))
    tuple_list = tuple_list[:len(a)]
    return [(t[1], t[2]) for t in tuple_list]