import heapq

def ksmallest(k, a):
    h = []
    for i in a:
        if len(h) < k:
            heapq.heappush(h, i*-1)
        else:
            if (i*-1) > h[0]:
                heapq.heappop(h)
                heapq.heappush(h, i*-1)
    h = [x*-1 for x in h]
    h.sort()
    return h
