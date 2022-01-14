### [Back to Main](https://github.com/mendenson/Data_Structures-Algorithms)

# Big O Notation
We’ve seen in the preceding topics that the primary factor in determining an algorithm’s efficiency is the number of steps it takes.

The more effective way to quantify the efficiency of linear search is to say that linear search takes _N steps_ for _N elements in the array_. That is, if an array has N elements, linear search takes N steps. Now, this is a pretty wordy way of expressing this concept.

To help ease communication regarding time complexity, computer scientists have borrowed a concept from the world of mathematics to describe a concise and consistent language around the efficiency of data structures and algorithms. Known as Big O Notation, this formalized expression of these concepts allows us to easily categorize the efficiency of a given algorithm and convey it to others.

## Big O: How Many Steps Relative to N Elements?
Big O achieves consistency by focusing on the number of steps an algorithm takes, but in a specific way.

In a worst-case scenario, linear search will take as many steps as there are elements in the array. As we’ve previously phrased it: for N elements in the array, linear search can take up to N steps. The appropriate way to express this in Big O Notation is: O(N).

Some pronounce this as “Big Oh of N.” Others call it “Order of N.” (My personal preference is the last).

Here’s what the notation means. It expresses the answer to what we’ll call the “key question.” The key question is: _if there are N data elements, how many steps will the algorithm take?_

Let’s quickly review the thought process for expressing time complexity with Big O Notation, again using the example of linear search. First, we ask the key question: if there are N data elements in an array, how many steps will linear search take? Because the answer to this question is that linear search will take N steps, we express this as O(N).

If there are N data elements, how many steps will reading from an array take? The answer is that reading takes just one step. So, we express his as O(1), which I pronounce “Oh of 1.” That is, _no matter how many elements_ an array has, reading from the array always takes one step.

And this is why O(1) is considered the “fastest” kind of algorithm. Even as the data increases, an O(1) algorithm doesn’t take any additional steps. The algorithm always takes a constant number of steps no matter what N is. In fact, an O(1) algorithm can also be referred to as having constant time.

## The Soul of Big O
While Big O is an expression of the number of an algorithm’s steps relative to N data elements, that alone misses the deeper _why_ behind Big O, what I dub the “soul of Big O.”

The soul of Big O is what Big O is truly concerned about: how will an algorithm’s performance _change as the data increases?_

This is the soul of Big O. Big O doesn’t want to simply tell you how many steps an algorithm takes. It wants to tell you the story of how the number of steps increase as the data _changes_.

Viewed with this lens, we don’t care very much whether an algorithm is O(1) or O(3). Because both algorithms are the type that aren’t affected by increased data, as their number of steps remain constant, they’re essentially the same kind of algorithm. They’re both algorithms whose steps remain constant irrespective of the data, and we don’t care to make a distinction between the two.

An algorithm that is O(N), on the other hand, is a different type of algorithm. It’s an algorithm whose performance is affected as we increase the data. More specifically, it’s the kind of algorithm whose steps increase in direct proportion to the data as the data increases. This is the story O(N) tells. It tells you about the proportional relationship between the data and the algorithm’s efficiency. It describes exactly how the number of steps increase as the data increases.

![img01](https://user-images.githubusercontent.com/60521016/144307425-2817494a-4b7a-4508-879b-3ceb9824d73e.png)

Notice that O(N) makes a perfect diagonal line. This is because for every additional piece of data, the algorithm takes one additional step. Accordingly, the more data, the more steps the algorithm will take.

Contrast this with O(1), which is a perfect horizontal line. No matter how much data there is, the number of steps remain constant.

While Big O effectively describes both the best- and worst-case scenarios of a given algorithm, Big O Notation generally refers to the worst-case scenario unless specified otherwise. This is why most references will describe linear search as being O(N) even though it can be O(1) in a best-case scenario.

This is because a “pessimistic” approach can be a useful tool: knowing exactly how inefficient an algorithm can get in a worst-case scenario prepares us for the worst and may have a strong impact on our choices.

## An Algorithm of the Third Kind
In the previous topic, you learned that binary search on an ordered array is much faster than linear search on the same array. Let’s now look at how to describe binary search in terms of Big O Notation.

In Big O terms, we describe binary search as having a time complexity of: O(log N).

Simply put, O(log N) is the Big O way of describing an algorithm that _increases one step each time the data is doubled_. As you learned in the previous chapter, binary search does just that.

Let’s look at a graph that compares the three types:

![image](https://user-images.githubusercontent.com/60521016/144309847-3cf20696-5206-42c0-93e2-cc36095e257e.png)

Note how O(log N) curves ever so slightly upward, making it less efficient than O(1), but much more efficient than O(N).

In computer science, whenever we say O(log N), it’s actually shorthand for saying O(log<sub>2</sub>N). We just omit that small 2 for convenience.

O(log N) means that for N data elements, the algorithm would take log2 N steps. If there are 8 elements, the algorithm would take three steps, since log<sub>2</sub>8 = 3.

Said another way, if we keep dividing the 8 elements in half, it would take us three steps until we end up with 1 element.

This is exactly what happens with binary search. As we search for a particular item, we keep dividing the array’s cells in half until we narrow it down to the correct number.

Said simply: _O(log N) means the algorithm takes as many steps as it takes to
keep halving the data elements until we remain with 1_.

## Practical Examples
- ### [Example 1](https://github.com/mendenson/Data-Structures-and-Algorithms/blob/Big-O-Notation/3-Big%20O%20Notation/Example%20Code/example01.py)
- ### [Example 2](https://github.com/mendenson/Data-Structures-and-Algorithms/blob/Big-O-Notation/3-Big%20O%20Notation/Example%20Code/example02.py)
- ### [Example 3](https://github.com/mendenson/Data-Structures-and-Algorithms/blob/Big-O-Notation/3-Big%20O%20Notation/Example%20Code/example03.cs)
- ### [Example 4](https://github.com/mendenson/Data-Structures-and-Algorithms/blob/Big-O-Notation/3-Big%20O%20Notation/Example%20Code/example04.cs)
- ### [Example 5](https://github.com/mendenson/Data-Structures-and-Algorithms/blob/Big-O-Notation/3-Big%20O%20Notation/Example%20Code/example05.cs)
- ### [Example 6](https://github.com/mendenson/Data-Structures-and-Algorithms/blob/Big-O-Notation/3-Big%20O%20Notation/Example%20Code/example06.cs)
- ### [Example 7](https://github.com/mendenson/Data-Structures-and-Algorithms/blob/Big-O-Notation/3-Big%20O%20Notation/Example%20Code/example07.cs)

## Speeding Up Your Code with Big O
With Big O, you also have the opportunity to compare your algorithm to _general algorithms out there in the world_, and you can say to yourself, “Is this a fast or slow algorithm as far as algorithms generally go?”

If you find that Big O labels your algorithm as a “slow” one, you can now take a step back and try to figure out if there’s a way to optimize it by trying to get it to fall under a faster category of Big O. This may not always be possible, of course, but it’s certainly worth thinking about.

### Bubble Sort
Sorting algorithms have been the subject of extensive research in computer science, and tens of such algorithms have been developed over the years. They all solve the following problem: _Given an array of unsorted values, how can we sort them so that they end up in ascending order?_

Bubble Sort is a basic sorting algorithm and follows these steps:
1. Point to two consecutive values in the array. (Initially, we start by pointing to the array’s first two values.) Compare the first item with the second one
2. If the two items are out of order (in other words, the left value is greater than the right value), swap them (if they already happen to be in the correct order, do nothing for this step)
3. Move the “pointers” one cell to the right
4. Repeat Steps 1 through 3 until we reach the end of the array, or if we reach the values that have already been sorted. (This will make more sense in the walk-through that follows.) At this point, we have completed our first pass-through of the array. That is, we “passed through” the array by pointing to each of its values until we reached the end
5. We then move the two pointers back to the first two values of the array, and execute another pass-through of the array by running Steps 1 through 4 again. We keep on executing these pass-throughs until we have a passthrough in which we did not perform any swaps. When this happens, it means our array is fully sorted and our work is done

### [Code Implementation in Python: Bubble Sort](https://github.com/mendenson/Data-Structures-and-Algorithms/blob/Big-O-Notation/3-Big%20O%20Notation/Example%20Code/bubblesort.py)

### The Efficiency of Bubble Sort
The Bubble Sort algorithm contains two significant kinds of steps:
- _Comparisons_: two numbers are compared with one another to determine
which is greater.
- _Swaps_: two numbers are swapped with one another in order to sort them.

Notice the inefficiency here. As the number of elements increases, the number of steps grows exponentially. We can see this clearly in the following table:

![image](https://user-images.githubusercontent.com/60521016/144329096-bbeb44e6-585c-4f28-9fcd-5157d7919d10.png)

If you look at the growth of steps as N increases, you’ll see that it’s growing by approximately N<sup>2</sup>. Take a look at the following table:
![image](https://user-images.githubusercontent.com/60521016/144329230-7a002c43-5f97-40b9-940d-2414612c23dc.png)

Because for N values, Bubble Sort takes N<sup>2</sup> steps, in Big O, we say that Bubble Sort has an efficiency of O(N<sup>2</sup>).

O(N<sup>2</sup>) is considered to be a relatively inefficient algorithm, since as the data increases, the steps increase dramatically. Look at this graph, which compares O(N<sup>2</sup>) against the faster O(N):

![image](https://user-images.githubusercontent.com/60521016/144330092-9de9cc44-5ca6-4b0a-9101-51892146a8a3.png)

Note how O(N<sup>2</sup>) curves sharply upward in terms of number of steps as the data grows. Compare this with O(N), which plots along a simple, diagonal line.

One last note: O(N<sup>2</sup>) is also referred to as _quadratic time_.

### A Quadratic Problem
