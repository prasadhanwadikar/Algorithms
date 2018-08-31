def longest(a):
    d, lp = _longest(a)
    return lp

def _longest(a):
    if a == [] or (a[0] == [] and a[2] == []):
        return 0, 0
    ld, llp = _longest(a[0])
    rd, rlp = _longest(a[2])
    d = max(ld, rd) + 1
    if ld == 0 and rd == 0:
        if a[0] == [] or a[2] == []:
            lp = 1
        else:
            lp = 2
    else:
        lp = max((ld + rd + 2), llp, rlp)
    return d, lp
