# Symmetric Difference of A and B is a set of elements in A and B but not in both (excluding the intersection). 
# Symmetric difference is performed using ^ operator. 
# Same can be accomplished using the method symmetric_difference().

# Symmetric difference of two sets
# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use ^ operator
# Output: {1, 2, 3, 6, 7, 8}
print(A ^ B)