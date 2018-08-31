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

def find(a, x, k):
    if a == []:
        return []

    #create an array of differences
    da = [abs(x-v) for v in a]

    #qselect kth value from differences array
    ksmalldiffvalue = qselect(k, da)

    #create an array of k difference values <= ksmalldiffvalue
    #ltda = [y for y in da if y < ksmalldiffvalue] - todo
    #eda = [y for y in da if y == ksmalldiffvalue] - todo
    kda = [y for y in da if y <= ksmalldiffvalue][:k]

    #for each diff value in kda - identify all values from original array (in sequence) where its diff = dv
    result = []
    for dv in kda:
        result += [v for v in a if abs(v-x) == dv]

    #only return the top k identified values from a
    return [] if result == [] else result[:k]