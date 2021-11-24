# A set is an unorded collection of itens. 
# Every set element is unique (no duplicates) and must be 
# immutable (cannot be changed). However, a set itself is mutable. 
# We can add or remove itens from it. Sets can also be used to 
# perform methematical set operations like union, intersection, 
# symmetric difference, etc.A set is an unorded collection of itens. 
# Every set element is unique (no duplicates) and must be immutable (cannot be changed). 
# However, a set itself is mutable. We can add or remove itens from it. 
# Sets can also be used to perform methematical set operations like union, intersection, symmetric difference, etc.

# set cannot have duplicates
# Output: {1, 2, 3, 4}
my_set = {1, 2, 3, 4, 3, 2}
print(my_set)

# we can make set from a list
# Output: {1, 2, 3}
my_set = set([1, 2, 3, 2])
print(my_set)

# set cannot have mutable items
# here [3, 4] is a mutable list
# this will cause an error.

my_set = {1, 2, [3, 4]}