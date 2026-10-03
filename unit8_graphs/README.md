# Unit 8 Discussion: Breadth-First Search (BFS)

## Overview

This assignment explores graph traversal using Breadth-First Search (BFS).

## Learning Objectives

- Represent graphs using adjacency lists
- Implement BFS
- Use queues in graph traversal
- Analyze graph traversal behavior

## Requirements

1. Create a graph.
2. Perform BFS traversal.
3. Add nodes or edges.
4. Demonstrate edge cases.
5. Analyze BFS behavior.
6. Create a real-world graph example.


## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
In completing this assignment I developed skills for representing a graph using an adjacency list in Python by creating an adjacency list as a dictionary where each key is a node and its values are lists of the adjacent nodes. 
I also created a breadth-first search by implementing a queue (deque) to keep track of what is next to be visited; a set of all visited nodes to help avoid revisiting a node; and a list of all the order in which the nodes were visited. 
Modeling the graph as a "similar tastes" network for a streaming platform gave me an opportunity to visualize how graphs store relationships between actual objects.

2. What challenges did you encounter, and how did you overcome them?
The most difficult task for me to understand was why Breadth-First Search (BFS) considers a node “visited” or marked “as discovered,” as soon as that node is placed into the queue. Initially, I had simply put all of my nodes in the queue without keeping track of them. 
This caused some of the same nodes to be placed in the queue multiple times. I corrected this issue by using an additional data structure called a "discovered" set where I would add each of the neighbors as they were being added to the queue. 
Adding the neighbors to this "discovered" set allowed me to prevent going back over previously visited nodes, while maintaining proper traversal of the graph even if there are cycles.

3. Compare BFS and DFS conceptually and describe real-world applications and use cases.
BFS uses a queue (FIFO) and explores a graph level by level, visiting all of a node's direct neighbors before moving farther out, which makes it ideal for finding the shortest path in an unweighted graph or the closest connections first, such as suggesting content from a user's nearest taste-matches. 
DFS uses a stack (LIFO) and follows one path as deep as possible before backing up, which suits problems like exploring every path, detecting cycles, or digging deep to uncover niche recommendations along a chain of similar items.