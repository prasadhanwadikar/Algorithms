def mergesort(a):
    n = len(a)
    if n < 2:
        return
    else:
        mid = n//2
        left = a[0:mid]
        right = a[mid:]
        mergesort(left)
        mergesort(right)
        merge(left, right, a)

def merge(l, r, a):
    i = j = k = 0
    ll = len(l)
    rl = len(r)
    while i < ll and j < rl:
        if l[i] <= r[j]:
            a[k] = l[i]
            i += 1
        else:
            a[k] = r[j]
            j += 1
        k += 1
    while i < ll:
        a[k] = l[i]
        i += 1
        k += 1
    while j < rl:
        a[k] = r[j]
        j += 1
        k += 1
