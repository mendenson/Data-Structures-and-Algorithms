### [Back to Main](https://github.com/mendenson/Data_Structures-Algorithms)

# Alghoritms

An algorithm is simply a set of _instructions for completing a specific task_.

When applied to computing, an algorithm refers to the set of instructions given to a computer to achieve a particular task. When we write any code, then, we’re creating algorithms for the computer to follow and execute.

In this topic, we’ll encounter another two algorithms that solve the same problem. In this case, though, one algorithm will be faster than the other by _orders of magnitude_.

To explore these new algorithms, we’ll need to take a look at a new data structure.

## Ordered Arrays
The ordered array is almost identical to the “classic” array. The only difference is that ordered arrays require that the values are always kept—you guessed it—_in order_. That is, every time a value is added, it gets placed in the proper cell so that the values in the array remain sorted.

when inserting into an ordered array, we need to always conduct a search before the actual insertion to determine the correct spot for the insertion. This is one difference in performance between a classic array and an ordered array.

While insertion is less efficient for an ordered array than for a classic array, the ordered array has a secret superpower when it comes to searching.

The number of steps for insertion remains similar no matter where in the ordered array our new value ends up. If our value ends up toward the beginning of the ordered array, we have fewer comparisons and more shifts. If our value ends up toward the end, we get more comparisons but fewer shifts. The fewest steps occur when the new value winds up at the very end, since no shifts are necessary. In this case, we take N steps to compare the new value with all N existing values, plus one step for the insertion itself, yielding a total of N + 1 steps.

In terms of N, we’d say that for N elements in an ordered array, the insertion took N + 2 steps in total.

## Searching an Ordered Array
Linear search can take fewer steps in an ordered array than in a classic array in certain situations. That being said, if we’re searching for a value that happens to be the final value or not within the array at all, we will still end up searching each and every cell.

Standard arrays and ordered arrays don’t have tremendous differences in efficiency, or at least not in worst-case scenarios. For both kinds of arrays, if they contain N elements, linear search can take up to N steps.

The big advantage of an ordered array over a classic array is that an ordered array allows for an alternative searching algorithm. This algorithm is known as _binary search_, and it is a much, much faster algorithm than linear search.

## Binary Search
While this is the same number of steps linear search would have taken in this example, we’ll take a look at the power of binary search shortly.

Note that binary search is only possible within an ordered array. With a classic array, values can be in any order, and we’d never know whether to look to the left or right of any given value. This is one of the advantages of ordered arrays: we have the option of binary search.

## Binary Search vs. Linear Search
With ordered arrays of a small size, the algorithm of binary search doesn’t have much of an advantage over linear search.

With an array containing 100 values, here are the maximum number of steps each type of search would take:
- Linear search: 100 steps
- Binary search: 7 steps

With an array of 10,000 elements, linear search can take up to 10,000 steps, while binary search takes up to a maximum of just 13 steps. For an array of size one million, linear search would take up to one million steps, while binary search would take up to just 20 steps.

Keep in mind that ordered arrays aren’t faster in every respect. As you’ve seen, insertion in ordered arrays is slower than in standard arrays. But here’s the trade-off: by using an ordered array, you have somewhat slower insertion, but much faster search. Again, you must always analyze your application to see which is a better fit.

The whole beauty of binary search is that each inspection eliminates half of the remaining elements. Therefore, each time we double the amount of data, we add only one step. After all, this doubling of data gets totally eliminated with the first inspection!

It’s worth noting that now that we’ve added binary search to our toolkit, insertion within an ordered array can become faster as well. Insertion requires a search before the actual insertion, but we can now upgrade that search from a linear search to a binary search. However, insertion within an ordered array still remains slower than within a regular array, as the regular array’s insertion doesn’t require a search at all.

It’s also important to realize that there usually isn’t a single data structure or algorithm that is perfect for every situation. For example, just because ordered arrays allow for binary search doesn’t mean you should always use ordered arrays. In situations where you don’t anticipate the need to search the data much, only adding data, standard arrays may be a better choice because their insertion is faster.

# Example code using Python 3
- [Guessing Game](https://github.com/mendenson/Data_Structures-Algorithms/blob/main/2-Algorithm/Example%20code/GuessingGame.py)

# References
- - WENGROW, Jay. [A Common-Sense Guide to Data Structures and Algorithms](https://www.amazon.com/Common-Sense-Guide-Structures-Algorithms-Second/dp/1680507222/ref=sr_1_1?crid=ACD0HCKZKRG2&keywords=a+common+sense+guide+to+data+structures+and+algorithms&qid=1637177261&qsid=141-3457049-6381441&sprefix=a+common%2Caps%2C221&sr=8-1&sres=1680507222%2C1680502441%2CB093N93PFD%2C1617295485%2CB01D24NAL6%2C1492043451%2C0984782850%2C0262033844%2C1789801214%2C1118771338%2C1449364934%2C195120400X%2C1789537177%2CB07N3SC7W2%2CB09L37B2Z7%2CB084RFJFZ9&srpt=ABIS_BOOK), page 21-34.

