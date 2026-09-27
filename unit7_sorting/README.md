# Unit 7 Discussion: Sorting Algorithms

## Overview

This assignment compares Bubble Sort and Merge Sort.

## Learning Objectives

- Implement Bubble Sort
- Implement Merge Sort
- Understand divide-and-conquer
- Compare algorithm efficiency

## Requirements

1. Test Bubble Sort and Merge Sort.
2. Use multiple datasets.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world sorting example.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
In doing this assignment, I gained knowledge about implementing two types of sorting algorithms in Python; bubble sort is an iterative algorithm that repeatedly switches neighboring values whereas merge sort is a recursive algorithm using a divide-and-conquer approach. 
In addition to writing the "merge" code segment that takes two sorted lists and produces one, I have also learned the relative efficiencies of the two methods. 
Specifically, bubble sort has a worst-case time complexity of O(n^2), and therefore is quite inefficient compared to merge sort's worst-case time complexity of O(n log n). 
As an additional part of learning these two algorithms, I tested both algorithms on many different test data sets. For example, I used test data consisting of an empty list, 
a pre-sorted list, lists containing duplicate values, and lists containing only one value.

2. What challenges did you encounter, and how did you overcome them?
The most significant difficulty that I encountered while working on this assignment was understanding recursion. The way that a list is split into halves, 
and then merge_sort called recursively on each half until there are no more pairs of sub-lists to be merged does not immediately make sense. 
Therefore, to help me understand this process, I manually went through merging a few small lists. Furthermore, I ensured that my base case was clearly defined. 
A list that contains either zero or one value is already sorted. This ensures that at some point during the recursion, the function will call itself with arguments that cause it to return without further recursion occurring.

3. Compare and constrast each sorting algorithm based on efficiency differences, tradeoffs made, and when to each.
Bubble sort is relatively easy to understand, work with, and works extremely well when dealing with a small number of nearly sorted items. 
However, since bubble sort performs operations in linear order from the beginning of the list to the end of the list and repeats this process until all elements are in their proper positions, bubble sort is very slow when attempting to sort large numbers of items.
On the other hand, although merge sort is much more difficult to understand and work with than bubble sort and requires additional memory for its temporary sublist(s),
due to its significantly faster processing speed of O(n log n) (versus bubble sort's O(n^2)), merge sort is far superior to bubble sort for large amounts of data. 
If the amount of data is too small to require high levels of accuracy and speed, and/or if the data being sorted is nearly in its final position, bubble sort may still prove suitable.