from qselect import *
from qsort import *

n = qselect(2, [3, 10, 4, 7, 19])
print(n)
n = qselect(3, [11, 2, 8, 3])
print(n)

t = sort([4,8,2,6,3,5,7,1,9])
print(t)
st = sorted(t)
print(st)
print(search(t, 6))
print(search(t, 6.5))
insert(t, 6.5)
print(t)