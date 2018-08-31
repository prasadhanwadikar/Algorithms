from heapdict import heapdict
from collections import defaultdict


def shortest(V, E):
    if V < 1 or E == []:
        return 0, []
    snl = []
    for i in range(V):
        snl.append([])
    for (u, v, w) in E:
        snl[u].append((u, v, w))
        snl[v].append((v, u, w))
    sl = 0
    hd = heapdict()
    hd[0] = 0
    pnd = defaultdict(int)  # popped node dict - key is node and value is last node in shortest path till node
    pnd[0] = -1
    nsl = [0] * V  # node status list nsl[n] = 1 means node n is popped
    while len(hd) > 0:
        (n, sl) = hd.popitem()  # n = node, sl = shortest path length till n
        nsl[n] = 1
        if n == V - 1:
            break
        for (u, v, w) in snl[n]:
            if nsl[v] == 0 and (v not in hd or sl + w < hd[v]):
                hd[v] = sl + w
                pnd[v] = u
    n = V - 1
    sp = [n]
    while pnd[n] > -1:
        n = pnd[n]
        sp = [n] + sp
    return sl, sp


if __name__ == '__main__':
    print(shortest(4, [(0, 1, 1), (0, 2, 5), (1, 2, 1), (2, 3, 2), (1, 3, 6)]))
    print(shortest(7, [(0, 1, 0), (0, 2, 1), (0, 3, 2), (1, 4, 1), (2, 4, 2), (2, 5, 2), (3, 5, 1), (4, 6, 1), (5, 6, 2)]))
