def order(v, e):
    q = []
    while len(e) > 0:
        v1 = [t[1] for t in e]
        e1 = [t for t in e if t[0] not in v1]
        if e1 == []: return None
        e = list(set(e) - set(e1))
        v2 = [t[1] for t in e]
        q = q + [t[0] for t in e1 if t[0] not in q] + list(set(v1) - set(v2))
    return q

if __name__=='__main__':
    print(order(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)]))
    print(order(8, [(0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7)]))
    print(order(4, [(0,1), (1,2), (2,1), (2,3)]))