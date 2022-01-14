// Imagine you have a chessboard and put a single grain of rice on one
// square. On the second square, you put 2 grains of rice, since that is
// double the amount of rice on the previous square. On the third square,
// you put 4 grains. On the fourth square, you put 8 grains, and on the fifth
// square, you put 16 grains, and so on.

// The following function calculates which square you’ll need to place a
// certain number of rice grains. For example, for 16 grains, the function
// will return 5, since you will place the 16 grains on the fifth square.

function chessboardSpace(numberOfGrains)
{
    let chessboardSpaces = 1;
    let placedGrains = 1;

    while (placedGrains < numberOfGrains)
        {
            placedGrains *= 2;
            chessboardSpaces += 1;
        }
    
    return chessboardSpaces;
}

// This is O(log N). In this case, N is the number numberOfGrains, which is
// passed into the function. The loop runs as long as placedGrains < numberOf-
// Grains, but placedGrains starts at 1 and doubles each time the loop runs. If,
// for example, numberOfGrains was 256, we’d keep doubling the placedGrains
// nine times until we reach 256, meaning that our loop would run nine
// times for an N of 256. If numberOfGrains was 512, our loop would run 10
// times, and if numberOfGrains was 1024, the loop would run 11 times.
// Because our loop runs only one more time each time N is doubled, this
// is O(log N).