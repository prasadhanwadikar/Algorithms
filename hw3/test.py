from closest_unsorted import *

#returns [4,4]
print(find([4,1,3,2,7,4], 5.2, 2))
#returns [4,7,4]
print(find([4,1,3,2,7,4], 6.5, 3))
#returns [3,4]
print(find([5,3,4,1,6,3], 3.5, 2))


from closest_sorted import *

#[2]
print(find([1,2,3], 2.5, 1))
#[2,3]
print(find([1, 2, 3, 4, 5], 3, 2))
#[4,4]
print(find([1,2,3,4,4,7], 5.2, 2))
#[4,4,7]
print(find([1,2,3,4,4,7], 6.5, 3))
#[4,4,6]
print(find([1,2,3,4,4,6,6], 5, 3))
#[2,3,4,4,5]
print(find([1,2,3,4,4,5,6], 4, 5))


from xyz import *

print(find([-3, -2, -1, -4]))
print(find([1, 4, 2, 3, 5]))