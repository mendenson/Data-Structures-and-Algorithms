# A particular item can be removed from a set using the methods discard() and remove(). 
# The only difference between the two is that the discard() function leaves a set unchanged if the element is not present in the set. 
# On the other hand, the remove() function will raise an error in such a condition (if element is not present in the set).

# initialize my_set
my_set = {1, 3, 4, 5, 6}
print(my_set)

# discard an element
# Output: {1, 3, 5, 6}
my_set.discard(4)
print(my_set)

# remove an element
# Output: {1, 3, 5}
my_set.remove(6)
print(my_set)

# discard an element
# not present in my_set
# Output: {1, 3, 5}
my_set.discard(2)
print(my_set)

# remove an element
# not present in my_set
# you will get an error.
# Output: KeyError

my_set.remove(2)