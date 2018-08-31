import math

def best(bagSize, items):
    d = {}
    for i in range(len(items)+1):
        d[(i, 0)] = [0, [0] * len(items)]
    for w in range(bagSize+1):
        d[(0, w)] = [0, [0] * len(items)]
    return fillBag(len(items)-1, bagSize, items, d)

def fillBag(i, bagSize, items, d):
    if (i+1, bagSize) in d:
        return d[(i+1, bagSize)]
    result = d[(0, 0)]
    ci = items[i][2]
    mci = math.floor(bagSize / items[i][0])
    jRangeStop = min(ci, mci) + 1
    for j in range(jRangeStop):
        [value, pickedItems] = fillBag(i - 1, bagSize - j * items[i][0], items, d)
        value += j * items[i][1]
        newPickedItems = list(pickedItems)
        newPickedItems[i] += j
        if value > result[0]:
            result = [value, newPickedItems]
    d[(i+1, bagSize)] = result
    return result

if __name__=='__main__':
    print(best(3, [(2, 4, 2), (3, 5, 3)]))
    print(best(3, [(1, 5, 2), (1, 5, 3)]))
    print(best(3, [(1, 5, 1), (1, 5, 3)]))
    print(best(20, [(1, 10, 6), (3, 15, 4), (2, 10, 3)]))
    print(best(92, [(1, 6, 6), (6, 15, 7), (8, 9, 8), (2, 4, 7), (2, 20, 2)]))