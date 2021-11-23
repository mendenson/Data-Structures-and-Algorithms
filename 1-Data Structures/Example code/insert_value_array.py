# We can use the insert() method to insert at any index of the array. 

from array import *

my_array = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

print('Before insert: ', my_array)

my_array.insert(0, 24)

print('After insert: ', my_array)

# In the above example, using insert() method, the value 24 was inserted at index 0.
# Note that the first argument is the index while the second argument is the value. 