# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduces Binary Search Trees (BSTs) and recursive tree operations.

## Learning Objectives

- Build a BST
- Insert values recursively
- Search recursively
- Perform in-order traversal
- Understand BST organization

## Requirements

1. Build a BST.
2. Insert multiple values.
3. Demonstrate in-order traversal.
4. Test searching.
5. Demonstrate edge cases.
6. Create a real-world BST example.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
I learned how to build and work with a Binary Search Tree in Python. 
I learned how to insert values recursively so that smaller values go into the left subtree and larger values go into the right subtree, 
how to search the tree recursively by comparing at each node and following only one side, and how to perform an in-order traversal that visits the left subtree, 
then the current node, then the right subtree. I also learned why an in-order traversal of a BST always comes out sorted.

2. What challenges did you encounter, and how did you overcome them?
My biggest challenges were with the recursion. At one point I put my return statement inside an elif block by mistake, 
so it only ran on one branch, and because Python uses indentation to define blocks, the tree silently broke. 
I also put my search logic inside the public search method instead of the recursive helper. 
I overcame both by understanding the split between the public method, which just starts the recursion at the root, and the recursive helper, 
which does the actual comparing, and by paying closer attention to my indentation.

3. Explain BST behavior and compare to how ordering works to create efficiency as compared to other data structures.
A BST stays organized by its ordering rule: every left child is smaller and every right child is larger than its parent. 
That ordering is what makes searching efficient, because at each step the search follows only one side and discards the other half of the tree, 
unlike a plain list where you may have to check every element. However, this efficiency depends on the tree staying balanced. 
If values are inserted in already-sorted order, the tree turns into a long single line like a linked list, and search slows back down to checking every node.