function hasDuplicateValue(array) {
    let steps = 0;
    // It creates an array called existingNumbers, which atarts out empty
    let existingNumbers = [];
    for(let i = 0; i < array.length; i++) {
        steps++;
        // The significant type of step is looking at each number and checking whether
        // the value of its index in existingNumbers is a 1
        if(existingNumbers[array[i]] === 1) {
            return true;
        }else{
            existingNumbers[array[i]] = 1;
        }
    }
    console.log(steps);
    return false;
}

// If we run hasDuplicateValue([1, 4, 5, 2, 9]) now, we'll see that the output 
// in the JavaScript console is 5, which is the same as the size of our array.
// We'd find this to be true across arrays of all sizes. This algorithm, then, is O(N). 