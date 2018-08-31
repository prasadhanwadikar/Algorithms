def best(bagSize, items):
    d = {0: [0, [0] * len(items)]}
    return fillBag(bagSize, items, d)

def fillBag(bagSize, items, d):
    if bagSize in d:
        return d[bagSize]
    result = d[0]
    for i in range(len(items)):
        if bagSize >= items[i][0]:
            [v, pickedItems] = fillBag(bagSize - items[i][0], items, d)
            v += items[i][1]
            newPickedItems = list(pickedItems)
            newPickedItems[i] += 1
            if v > result[0]:
                result = [v, newPickedItems]
    d[bagSize] = result
    return result

if __name__=='__main__':
    print(best(0, [(2, 4), (3, 5)]))
    print(best(3, [(2, 4), (3, 5)]))
    print(best(3, [(1, 5), (1, 5)]))
    print(best(3, [(1, 2), (1, 5)]))
    print(best(3, [(1, 2), (2, 5)]))
    print(best(58, [(5, 9), (9, 18), (6, 12)]))
    print(best(92, [(8, 9), (9, 10), (10, 12), (5, 6)]))