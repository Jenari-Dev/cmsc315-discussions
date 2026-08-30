# Unit 3 Discussion: List Operations

## Overview

This assignment examines insertion, deletion, and searching in Python lists.

## Learning Objectives

- Insert values into a list
- Delete values from a list
- Search for values in a list
- Analyze list behavior and performance

## Requirements

1. Test insertion at the beginning, middle, and end.
2. Test deletion at the beginning, middle, and end.
3. Search for existing and missing values.
4. Demonstrate edge cases.
5. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
I learned how to use Python lists by adding items, removing items from specific positions, and using a linear search to find items within the list. 
I saw how inserting an item at any position makes all the other elements shift out of the way to make room, how to remove an item by its index number as long as that index exists, 
and how to write a simple loop that checks each item in the list one at a time until it finds a match or returns -1. 
I also became more comfortable printing and updating the list as it changed.

2. What challenges did you encounter, and how did you overcome them?
The biggest problem I experienced was the difference in syntax between Java and Python. 
Because I have primarily worked in Java, I would often write Python code with Java syntax. 
To resolve this issue, I went back to my last week's Python file for a review. This reminded me of the proper way to write Python.

3. How do list operations impact performance in real-world applications?
Depending on where the list method is called within the program, list methods may significantly impact your performance. 
Adding or removing items at the beginning of a list causes all of the items after it to be moved down which takes O(n) time for long lists. 
On the other hand, adding or removing items from the end of a list is a fast process. 
Therefore, when creating reliable and/or timely programs for emergency situations or similar applications, 
the method used for performing list operations, along with the choice of data structure, has significant implications regarding efficiency of results produced.