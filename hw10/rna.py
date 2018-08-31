from collections import defaultdict
import heapq

def best(s):
    nl = ['AU', 'GC', 'GU', 'UA', 'CG', 'UG']
    d = {}

    def _best(s):
        c, b = 0, ''
        j = len(s)
        if j == 0:
            return 0, ''
        elif j == 1:
            return 0, '.'
        if s in d:
            return d[s]
        for k in range(1, j):
            if s[0] + s[k] in nl:
                d[s[1:k]] = (c1, b1) = _best(s[1:k])
                d[s[k + 1:j]] = (c2, b2) = _best(s[k + 1:j])
                if (c1 + c2 + 1) > c:
                    c = c1 + c2 + 1
                    b = '(' + b1 + ')' + b2
        d[s[1:]] = (c3, b3) = _best(s[1:])
        b3 = '.' + b3
        d[s] = (c, b) if c > c3 else (c3, b3)
        return d[s]

    return _best(s)


def total(s):
    d = {}
    nl = ['AU', 'GC', 'GU', 'UA', 'CG', 'UG']

    def _total(s):
        if s in d:
            return d[s]
        t = 0
        j = len(s)
        if j == 0:
            return 1
        elif j == 1:
            return 1
        for k in range(1, j):
            if s[0] + s[k] in nl:
                t1 = _total(s[1:k])
                t2 = _total(s[k + 1:j])
                t += (t1 * t2)
        t3 = _total(s[1:])
        t += t3
        d[s] = t
        return d[s]

    return _total(s)


def kbest_naive(s, k):
    nl = ['AU', 'GC', 'GU', 'UA', 'CG', 'UG']
    d = {}

    def _strcutres(s):
        if s in d:
            return d[s]
        j = len(s)
        if j == 0:
            return [(0, '')]
        elif j == 1:
            return [(0, '.')]
        d[s] = []
        for k in range(1, j):
            if s[0] + s[k] in nl:
                sl1 = _strcutres(s[1:k])
                sl2 = _strcutres(s[k + 1:j])
                for s1 in sl1:
                    for s2 in sl2:
                        d[s].append((s1[0] + s2[0] + 1, '(' + s1[1] + ')' + s2[1]))
        sl3 = _strcutres(s[1:])
        for s3 in sl3:
            d[s].append((s3[0], '.' + s3[1]))
        return d[s]

    sl = _strcutres(s)
    return sorted(sl, reverse=True)[:k]


def kbest(s, k):
    d = defaultdict(int)
    def check_nucleotide(a, b):
        if a == 'G' and (b == 'C' or b == 'U'):
            return True
        if a == 'U' and (b == 'A' or b == 'G'):
            return True
        if a == 'C' and b == 'G':
            return True
        if a == 'A' and b == 'U':
            return True
        return False

    def _kbest(s, k):
        if s not in d:
            j = len(s)
            if j == 0:
                d[s] = [(0, '')]
            elif j == 1:
                d[s] = [(0, '.')]
            else:
                h, m, mat_id, u = [], [], 0, set()

                a = _kbest(s[1:], k)
                heapq.heappush(h, (-a[0][0], '.' + a[0][1], mat_id, 0))
                m.append((s[1:]))
                u.add((s[1:], 0))

                for l in range(1, j):
                    if check_nucleotide(s[0], s[l]):
                        mat_id += 1
                        la = _kbest(s[1:l], k)
                        ra = _kbest(s[l + 1:j], k)
                        heapq.heappush(h, (-(la[0][0] + ra[0][0] + 1), '(' + la[0][1] + ')' + ra[0][1], mat_id, 0, 0))
                        m.append((s[1:l], s[l + 1:j]))
                        u.add((s[1:l], s[l + 1:j], 0, 0))

                r = []
                while len(r) < k and len(h) != 0:
                    i = heapq.heappop(h)
                    r.append((-i[0], i[1]))
                    m_id = i[2]
                    if m_id == 0:
                        x = i[3]
                        a = _kbest(m[0], k)
                        if x + 1 < len(a) and (m[0], x + 1) not in u:
                            heapq.heappush(h, (-a[x + 1][0], '.' + a[x + 1][1], 0, x + 1))
                            u.add((m[0], x + 1))
                    else:
                        lx, rx = i[3], i[4]
                        la = _kbest(m[m_id][0], k)
                        ra = _kbest(m[m_id][1], k)
                        if lx + 1 < len(la) and (m[m_id][0], m[m_id][1], lx + 1, rx) not in u:
                            heapq.heappush(h, (-(la[lx + 1][0] + ra[rx][0] + 1), '(' + la[lx + 1][1] + ')' + ra[rx][1], m_id, lx + 1, rx))
                            u.add((m[m_id][0], m[m_id][1], lx + 1, rx))
                        if rx + 1 < len(ra) and (m[m_id][0], m[m_id][1], lx, rx + 1) not in u:
                            heapq.heappush(h, (-(la[lx][0] + ra[rx + 1][0] + 1), '(' + la[lx][1] + ')' + ra[rx + 1][1], m_id, lx, rx + 1))
                            u.add((m[m_id][0], m[m_id][1], lx, rx + 1))
                d[s] = r
        return d[s]

    return _kbest(s, k)

if __name__ == '__main__':
    print(best("AGGCAUCAAACCCUGCAUGGGAGCG"))
    print(total("AGGCAUCAAACCCUGCAUGGGAGCG"))
    print(kbest("AGGCAUCAAACCCUGCAUGGGAGCG", 10))
