// The following function calculates the median from an ordered array.

function median(array)
{
    const middle = Math.floor(array.length / 2);

    // If array has even amount of numbers:
    if (array.length % 2 === 0)
    {
        return (array[middle - 1] + array[middle]) / 2;
    }
    else
    {
        // If array has odd amount of numbers:
        return array[middle];
    }
}

// This is O(1). We can consider N to be the size of the array, but the algorithm
// takes a fixed number of steps no matter what N is. The algorithm
// does account for whether N is even or odd, but in either case, it takes the
// same number of steps.