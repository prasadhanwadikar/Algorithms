import heapq
import math

def kmergesort(a, k):
    l = len(a)
    if l < 2:
        return a
    list_of_pieces = []
    step = math.ceil(l/k)
    for i in range(k):
        piece = a[i*step:(i+1)*step]
        if piece != []:
            piece = kmergesort(piece, k)
            list_of_pieces.append(piece)
    return mergepieces(list_of_pieces, l)

def mergepieces(list_of_pieces, total_items):
    h = []
    merged_pieces_list = []
    total_pieces = len(list_of_pieces)

    for pi in range(total_pieces):
        heapq.heappush(h, (list_of_pieces[pi][0], pi))
        list_of_pieces[pi] = list_of_pieces[pi][1:]

    while(len(merged_pieces_list) != total_items):
        r = heapq.heappop(h)
        merged_pieces_list.append(r[0])
        pi = r[1]
        if list_of_pieces[pi] != []:
            heapq.heappush(h, (list_of_pieces[pi][0], pi))
            list_of_pieces[pi] = list_of_pieces[pi][1:]

    return merged_pieces_list