import collections
import math


def tsp(v, e):
    l = list(range(v))
    dist = [[math.inf for i in range(v)] for j in range(v)]
    for i in e:
        r, c, w = i
        dist[r][c] = w
        dist[c][r] = w
    return tsp_help(l, dist)


def tsp_help(l, dist):
    def solution(l, k):
        if not l:
            return [k]
        else:
            l.remove(k)
            return [k] + solution(l, c[frozenset(l), k][1])

    t = l[1:]
    pos = 0
    ll = []
    result = [0]
    while pos < len(t):
        for i in range(len(t)):
            te = t[::]
            te.remove(t[i])
            for j in range(len(te) + 1 - pos):
                ss = frozenset(te[j:pos + 1]), t[i]
                if ss not in ll:
                    ll.append(ss)
        pos += 1
    c = {}
    for i in sorted(ll):
        if not i[0]:
            c[i] = [dist[i[1]][0], 0]
        else:
            t1 = list(i[0])
            v = i[1]
            if len(t1) <= 1:
                x, *_ = i[0]
                t1.remove(x)
                c[i] = [dist[i[1]][x] + c[frozenset(t1), x][0], x]
            else:
                minv = math.inf
                p = None
                for iter in i[0]:
                    t2 = t1[::]
                    t2.remove(iter)
                    # print(dist[v][iter],c[frozenset(t2),iter])
                    if dist[v][iter] + c[frozenset(t2), iter][0] < minv:
                        minv = dist[v][iter] + c[frozenset(t2), iter][0]
                        p = iter
                c[i] = [minv, p]
    minv = math.inf
    p = None
    ft = frozenset(t)
    for i in ft:
        t2 = t[::]
        t2.remove(i)
        if dist[0][i] + c[frozenset(t2), i][0] < minv:
            minv = dist[0][i] + c[frozenset(t2), i][0]
            p = i
    c[ft, 0] = [minv, p]
    return c[ft, 0][0], [0] + solution(t, c[ft, 0][1])


if __name__ == '__main__':
    print(tsp(4, [(0, 1, 1), (0, 2, 5), (1, 2, 1), (2, 3, 2), (1, 3, 6)]))
    print(tsp(4, [(0, 1, 1), (0, 2, 5), (1, 2, 1), (2, 3, 2), (1, 3, 6), (3, 0, 1)]))
