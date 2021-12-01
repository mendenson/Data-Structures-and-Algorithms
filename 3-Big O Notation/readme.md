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
- ### [Example 1]()
- ### [Example 2]()
- ### [Example 3]()
- ### [Example 4]()
- ### [Example 5]()
- ### [Example 6]()
- ### [Example 7]()
