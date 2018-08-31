def find(a):
    result = []
    if len(a) < 3:
        return result
    a = sorted(a)
    for i in range(len(a)):
        l = 0
        r = len(a)-1
        while l < r:
            s = a[l] + a[r]
            if s == a[i]:
                result += [(a[l], a[r], a[i])]
                r -= 1
                l += 1
            elif s > a[i]:
                r -= 1
            else:
                l += 1
    return result