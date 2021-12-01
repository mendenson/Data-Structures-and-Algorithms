function arraySum(array)
{
    let sum = 0;

    for( let i = 0; i < array.lenght; i++)
        {
            sum += array[i];
        }
    return sum;
}

// This is O(N). For N elements in the array, the loop will run N times.