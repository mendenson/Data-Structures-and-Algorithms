# Here’s an implementation of Bubble Sort in Python

def bubble_sort(list):
    # The first thing we do is create a variable called unsorted_until_index. 
    # This keeps track of the rightmost index of the array that has not yet been sorted.
    # When we first start the algorithm, the array is completely unsorted, so we initialize
    # this variable to be the final index in the array:
    unsorted_until_index = len(list) - 1
    # We also create a variable called sorted that will keep track of whether the array is fully sorted. 
    # Of course, when our code first runs, it isn’t, so we set it to False:
    sorted = False

    # We begin a while loop that continues to run as long as the array is not sorted.
    # Each round of this loop represents a pass-through of the array:
    while not sorted:
        # Next, we preliminarily establish sorted to be True:
        sorted = True
        # Within the while loop, we begin a for loop in which we point to each pair of values
        # in the array. We use the variable i as our first pointer, and it starts from the
        # beginning of the array and goes until the index that has not yet been sorted:
        for i in range(unsorted_until_index):
            # Within this loop, we compare each pair of adjacent values and swap those
            # values if they’re out of order. We also change sorted to False if we have to make a swap:
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                sorted = False
        # At the end of each pass-through, we know that the value we bubbled up all
        # the way to the right is now in its correct position. Because of this, we decrement
        # the unsorted_until_index by 1, since the index it was already pointing to is now sorted:
        unsorted_until_index -= 1
    
    # The while loop ends once sorted is True, meaning the array is completely sorted.
    # Once this is the case, we return the sorted array:
    return list

# To use this function, we can pass an unsorted array to it, like so:
print(bubble_sort([65, 55, 45, 35, 25, 15, 10]))

# This function will then return the sorted array
# [10, 15, 25, 35, 45, 55, 65]