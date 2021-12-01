function isLeapYear(year)
{
    return (year % 100 === 0) ? (year % 400 === 0) : (year % 4 === 0);
}

// This is O(1). We can consider N to be the year passed into the function.
// But no matter what the year is, the algorithm doesn’t vary in how many
// steps it takes.