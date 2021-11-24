# Extend python array using extend() method.
# A python array can be extend with more than one value using extend() method.
from array import *

my_array = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(my_array)

my_array2 = array('i', [17, 18, 19])
my_array.extend(my_array2)

print('After extend: ', my_array)
