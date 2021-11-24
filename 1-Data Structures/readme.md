### [Back to Main](https://github.com/mendenson/Data_Structures-Algorithms)

# Data Structures
**Data** is a broad term that refers to all types of information, down to the most basic numbers and strings.

**Data structures** refer to how data is *organized*. 

We're going to begin our analysis of two data structures: arrays and sets.

# The Array: The foundational Data Structures
The *array* is one of the most basic data structures in computer science. The array is versatile, and can serve as a useful tool in many situations.

The *size* of an array is how many data elements the array holds.

The *index* of an array is the number that identifies where a piece of data lives inside the array.

Let's see this example:
```
array = ["apples", "bananas", "cucumbers", "dates", "elderberries"]

# This array has a size equal 5.
# index: "apples" = 0, "bananas" = 1, "cucumbers" = 2, "dates" = 3, "elderberries" = 4.
```

## Data Structure Operations
Many data structures are used in four basic ways, wich we refer to as *operations*. There operations are:
- **Read**: Reading refers to looking something up at a particular spot within the data structure. With an array, this means looking up a value at a particular index.
- **Search**: Searching refers to looking for a particular value within a data structure. With an array, this means looking to see if a particular value exists within the array, and if so, at which index.
- **Insert**: Insertion refers to removing a value from our data structure. With an array, this means adding a new value to an addtional slot within the array.
- **Delete**: Deletion refers to removing a value from our data structure. With an array, this means removing one of values from the array.
## Measuring Speed
When we measure how "fast" an operation takes. we do not refer to how fast the operation takes in terms of pure *time*, but instead in how many *steps* it takes. 

Measuring the speed of an operation in terms of time is undependable, since the time will always change depending on the hardware it is run on. 

However, we *can* measure the speed of an operation in terms how many computational *steps* it takes.

Let's jump into the four operations of an array and determine how many steps each one takes.
## Reading
A computer can read from an array in just one step. This is because the computer has the ability to jump to any particular index in the array and peer inside.

When the computer reads a value at a particular index of an array, it can jump straight to that index because of the combination of the following facts about computers:
1. A computer can jump to any *memory address* in one step. As an analogy, if Iask you to raise your right pinky finger, you wouldn't have to search all oyur fingers to find which one is your right pinky. You'd be able to identify it immediately.
2. Whenever a computer allocates an array, it also makes note at which memory address the array *begins*. So if we asked the computer to find the first element of the array, it would be able to instantly jump to the appropriate memory address to find it.

Reading from an array is, therefore, an efficient operation, since the computer can read any index by jumping to any memory address in one step.

Naturally, an operation that takes just one step is the fastest type of operation. Besides being a foundational data structure, arrays are also a very powerful data structure because we can read from them with such speed.
## Searching
*Searching* an array means looking to see whether a particular value exists within an array and if so, at which index it’s located.

In a sense, it’s the inverse of reading. Reading means providing the computer an index and asking it to return the value contained there. Searching, on the other hand, means providing the computer a value and asking it to return the index of that value’s location.

This is an important fact about computers: a computer has immediate access to all of its memory addresses, but it has no idea offhand what values are contained at each memory address.

The basic search operation — in which the computer checks each cell one at a time — is known as linear search.

Another way of saying this is that for N cells in an array, linear search would take a maximum of N steps. In this context, N is just a variable that can be replaced by any number.

In any case, it’s clear that searching is less efficient than reading, since searching can take many steps, while reading always takes just one step no matter the size of the array.
## Insertion
The efficiency of inserting a new piece of data into an array depends on where within the array you’re inserting it.

Let’s say we want to add to the end of a list. Such an insertion takes just one step.

We’ve dealt with insertions at the end of an array, but inserting a new piece of data at the beginning or in the middle of an array is a different story. In these cases, we need to shift pieces of data to make room for what we’re inserting, leading to additional steps.

The worst-case scenario for insertion into an array—that is, the scenario in which insertion takes the most steps—is when we insert data at the beginning of the array. This is because when inserting at the beginning of the array, we have to move all the other values one cell to the right.
##Deletion
Deletion from an array is the process of eliminating the value at a particular index.

Like insertion, the worst-case scenario of deleting an element is deleting the very first element of the array. This is because index 0 would become empty, and we’d have to shift all the remaining elements to the left to fill the gap.

We can say then, that for an array containing N elements, the maximum number of steps that deletion would take is N steps.

# Sets: How a Single Rule Can Affect Efficiency
A _set_ is a data structure that does not allow duplicate values to be contained within it.

Sets are useful when you need to ensure that you don’t have duplicate data.

Reading from a set is exactly the same as reading from an array—it takes just one step for the computer to look up what’s contained within a particular index.

Searching a set also turns out to be no different than searching an array—it takes up to N steps to search for a value within a set. And deletion is also identical between a set and an array—it takes up to N steps to delete a value and move data to the left to close the gap.

Insertion, however, is where arrays and sets diverge. Let’s first explore inserting a value at the _end_ of a set, which was a best-case scenario for an array. We saw that with an array, the computer can insert a value at its end in a single step.

So, every insertion into a set _first requires a search_.

Insertion into the end of a set will take up to N + 1 steps for N elements. This is because there are N steps of search to ensure that the value doesn’t already exist within the set, and then one step for the actual insertion. Contrast this with the regular array, in which such an insertion takes a grand total of one step.

In the worst-case scenario, where we’re inserting a value at the beginning of a set, the computer needs to search N cells to ensure that the set doesn’t already contain that value, another N steps to shift all the data to the right, and another final step to insert the new value. That’s a total of 2N + 1 steps. Contrast this to insertion into the beginning of a regular array, which only takes N + 1 steps.

# Array examples using Python 3
- [Basic Example and access individual elements through indexes](https://github.com/mendenson/Data_Structures-Algorithms/blob/main/1-Data%20Structures/Example%20code/intro_array.py)
- [Insert value in an array using insert() method](https://github.com/mendenson/Data_Structures-Algorithms/blob/main/1-Data%20Structures/Example%20code/insert_value_array.py)
- [Extend python array using extend() method](https://github.com/mendenson/Data_Structures-Algorithms/blob/main/1-Data%20Structures/Example%20code/extend_array.py)
- [Remove any array elelment using remove() method](https://github.com/mendenson/Data_Structures-Algorithms/blob/main/1-Data%20Structures/Example%20code/remove_array.py)
- [Remove last array element using pop() method](https://github.com/mendenson/Data_Structures-Algorithms/blob/main/1-Data%20Structures/Example%20code/remove_last.py)

# Set Examples using Python 3
- [Start example](https://github.com/mendenson/Data_Structures-Algorithms/blob/main/1-Data%20Structures/Example%20code/set_start.py)
- [Modifying a set](https://github.com/mendenson/Data_Structures-Algorithms/blob/main/1-Data%20Structures/Example%20code/set_modify.py)
- [Removing elements from a set](https://github.com/mendenson/Data_Structures-Algorithms/blob/main/1-Data%20Structures/Example%20code/set_remove.py)
- [Set Union](https://github.com/mendenson/Data_Structures-Algorithms/blob/main/1-Data%20Structures/Example%20code/set_union.py)
- [Set Intersection](https://github.com/mendenson/Data_Structures-Algorithms/blob/main/1-Data%20Structures/Example%20code/set_intersection.py)
- [Set Difference](https://github.com/mendenson/Data_Structures-Algorithms/blob/main/1-Data%20Structures/Example%20code/set_difference.py)
- [Set Symmetric Difference](https://github.com/mendenson/Data_Structures-Algorithms/blob/main/1-Data%20Structures/Example%20code/set_symDif.py)
- [Set Membership Test](https://github.com/mendenson/Data_Structures-Algorithms/blob/main/1-Data%20Structures/Example%20code/set_member.py)

# References
- WENGROW, Jay. [A Common-Sense Guide to Data Structures and Algorithms](https://www.amazon.com/Common-Sense-Guide-Structures-Algorithms-Second/dp/1680507222/ref=sr_1_1?crid=ACD0HCKZKRG2&keywords=a+common+sense+guide+to+data+structures+and+algorithms&qid=1637177261&qsid=141-3457049-6381441&sprefix=a+common%2Caps%2C221&sr=8-1&sres=1680507222%2C1680502441%2CB093N93PFD%2C1617295485%2CB01D24NAL6%2C1492043451%2C0984782850%2C0262033844%2C1789801214%2C1118771338%2C1449364934%2C195120400X%2C1789537177%2CB07N3SC7W2%2CB09L37B2Z7%2CB084RFJFZ9&srpt=ABIS_BOOK), page 01-19.
- The Geek Stuff. [15 Python Array Examples – Declare, Append, Index, Remove, Count](https://www.thegeekstuff.com/2013/08/python-array/).
- Programiz. [Python Sets](https://www.programiz.com/python-programming/set).
