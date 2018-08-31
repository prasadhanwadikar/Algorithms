def num_inversions(a):
    n = len(a)
    if n < 2:
        return 0
    else:
        mid = n//2
        left = a[0:mid]
        right = a[mid:]
        lc = num_inversions(left)
        rc = num_inversions(right)
        ic = merge_and_count(left, right, a)
        return lc + rc + ic

def merge_and_count(l, r, a):
    i = j = k = 0
    ic = 0
    ll = len(l)
    rl = len(r)
    while i < ll and j < rl:
        if l[i] <= r[j]:
            a[k] = l[i]
            i += 1
        else:
            a[k] = r[j]
            j += 1
            ic = ic + ll - i
        k += 1
    while i < ll:
        a[k] = l[i]
        i += 1
        k += 1
    while j < rl:
        a[k] = r[j]
        j += 1
        k += 1
    return ic
