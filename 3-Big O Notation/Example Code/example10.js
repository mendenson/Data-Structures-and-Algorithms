function hasDuplicateValue(array) {
    let steps = 0; // count of steps
    for(let i = 0; i < array.length; i++) {
        for(let j = 0; j < array.length; j++) {
            steps++; // increment number of steps
            if(i !== j && array[i] === array[j]) {
                return true;
            }
        }
    }
    console.log(steps); // print number of steps if no duplicates
    return false;
}

// This added code will print the number of steps taken when there are no duplicates.
// If we run hasDuplicateValue([1, 4, 5, 2, 9]), for example, well see an output of 25
// in the JavaScript console, indicating that there were 25 comparisons for the 5 elements
// in the array. if we test this for other values, we'll see that the output is always
// the size of the array squared.

// Whenever you encounter a slow algorithm, it's worth spending some time to consider whether
// there are any faster alternatives. There may not be any better alternatives, but let's
// first make sure.