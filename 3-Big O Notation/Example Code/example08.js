array = [1, 5, 3, 9, 1, 4];

function hasDuplicateValue(array) {
    for(let i = 0; i < array.length; i++) {
        for(let j = 0; j < array.length; j++) {
            if(i !== j && array[i] === array[j]) {
                return true;
            }
        }
    }
    return false;
}

// In this function, we iterate through each value of the array using the variable i.
// As we focus on each value in i, we then run a second loop that loos through all 
// the values in the array - using j - and checks if the values at positions i and j
// are the same. If they are, it means we've encountered duplicate values and we return true.
// If we get through all of the looping and we haven't encountered any duplicates,
// we return false, since we know that there are no duplicates in the array.