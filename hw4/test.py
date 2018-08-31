from nbest import *
from datastream import *
from kmergesort import *

a, b = [4, 1, 5, 3], [2, 6, 3, 4]
print(nbesta(a, b))
print(nbestb(a, b))
print(nbestc(a, b))


a = ksmallest(4, [10, 2, 9, 3, 7, 8, 11, 5, 7])
print(a)
a = ksmallest(3, range(1000000, 0, -1))
print(a)


print(kmergesort([4,1,5,2,6,3,7,0], 3))