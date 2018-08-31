from msort import *
from inversions import *
from longest import *

a = [4, 2, 5, 1, 6, 3]
mergesort(a)
print(a)

a = [4, 1, 3, 2]
ic = num_inversions(a)
print(a)
print(ic)

a = [[], 1, []]
b = [[[], 1, []], 2, [[], 3, []]]
c = [[[[], 1, []], 2, [[], 3, []]], 4, [[[], 5, []], 6, [[], 7, [[], 9, []]]]]
alp = longest(a)
blp = longest(b)
clp = longest(c)
print(alp)
print(blp)
print(clp)