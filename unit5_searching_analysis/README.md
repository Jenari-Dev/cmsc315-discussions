# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compares linear search and binary search.

## Learning Objectives

- Implement linear search
- Implement binary search
- Compare performance
- Analyze algorithm efficiency

## Requirements

1. Test both algorithms on a small dataset.
2. Test both algorithms on a large dataset.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world search scenario.


## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
I have implemented a linear search and a binary search with Python, and analyzed the time complexity of these searches. 
The linear search looks at each element individually until it finds what you are looking for; this is why its time complexity is O(n) (where n = number of elements). 
Binary search divides the size of the data set in half with each pass through the dataset, so its time complexity is O(log n) (where n = number of elements). 
I have tested my code with both a small dataset and a large dataset. I have also handled edge cases like when you start off with an empty list, a list with only one element, 
and when you look up an item that is the first item in your list or the last item in your list.

2. What challenges did you encounter, and how did you overcome them?
The biggest problem I encountered was that I made an error in the test program code - the "print statements" for the "linear search" actually called the "binary_search". 
Therefore, the small dataset didn't accurately evaluate the performance of the linear search. However, after reading through my code carefully and checking the labels, I fixed the problem by making sure I used correct function names. 
In addition, earlier in the week I had a similar type of error in my binary search that resulted from me using a "<" instead of "==" when I evaluated the middle element to determine if it was equal to the target. This time around, 
I double-checked for equality before evaluating whether or not the middle element is less than.

3. Explain when to use linear versus binary search, including tradeoffs in real-world scenarios.
If you have a very small dataset, or if your data does not remain in an ordered state due to frequent updates/insertions/deletions, linear search may be preferred. 
However, if you have a large amount of data stored in order (i.e., sorted), then binary search will be significantly faster. The main disadvantage of sorting your data before searching with binary search is that it can take some initial time; 
however, once your data has been pre-sorted, subsequent searches using binary search will occur at extremely high speeds.