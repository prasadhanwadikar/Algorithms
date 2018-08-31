import bisect

def find(a, x, k):
    if a == [] or k == 0:
        return []

    i = bisect.bisect_left(a, x)
    l = i - 1
    r = i

    for n in range(k):
        if l > 0 and r < len(a):
            if abs(a[l]-x) <= abs(a[r]-x):
                l -= 1
            else:
                r += 1
        else:
            if l < 1:
                r += 1
            else: #r == len(a)
                l -= 1

    return a[l+1:r]