# This way we create a simple python array and print it.
from array import *

my_array = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# print each array's element
for i in my_array:
    print(i)

# Individual elements can be accessed through indexes. 
# Remember that indexes from zero.
print(my_array[0])
print(my_array[3])
print(my_array[1])