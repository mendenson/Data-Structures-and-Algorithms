// The following function accepts an array of strings and returns a new array
// that only contains the strings that start with the character "a".

function sectedAStrings(array)
{
    let newArray = [];

    for(let i = 0; i < array.length; i++)
        {
            if (array[i].startsWhith("a"))
                {
                    newArray.push(array[i]);
                }
        }

    return newArray;
}

// This is O(N). N is the number of strings within the array, and the loop will take N steps.