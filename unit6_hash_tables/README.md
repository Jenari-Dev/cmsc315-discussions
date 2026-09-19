# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This assignment uses Python dictionaries to demonstrate hash table behavior.

## Learning Objectives

- Insert key-value pairs
- Retrieve values efficiently
- Update existing values
- Remove entries
- Understand hashing concepts

## Requirements

1. Create and populate a dictionary.
2. Demonstrate lookup operations.
3. Demonstrate update operations.
4. Demonstrate delete operations.
5. Test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
I found out how a Python dictionary functions as a hash table to store information in key-value pairs. I learned how to add new values to a hash table, search for the value associated with a given key, modify a currently stored value, 
and remove a particular value-pair and that these operations take constant time on average (O(1)), since the hash function gives you the index where the value is located. 
I also discovered alternative safe approaches to access a dictionary, including using get() for looking up and pop() for removing values, both of which provide a default if the key is absent to avoid crashing due to raising a KeyError.

2. What challenges did you encounter, and how did you overcome them?
My biggest obstacle was managing missing keys. The act of accessing a key in a hash table with square brackets will raise a KeyError and cause the application to crash if that key doesn't exist. To deal with that problem, 
I started using get() to perform lookups, pop() to delete elements and provided a default in case there wasn't a key in existence. 
I used "in" to see if a key existed prior to accessing it.

3. Explain how hash tables behave, what collisions are, and how hash tables can improve efficiency.
Hash tables use a hash function to determine which element within the array holds the key's corresponding value. This allows for very quick retrieval of values based on their keys rather than having to scan the entire structure. 
Collisions occur when two unique keys produce the same hash result. Hash tables resolve collisions through chaining (an array of pointers in each element of the array) or probing (searching for an empty slot). 
Hash tables increase efficiency because the average time required for all three primary operations (lookups, inserts and deletes) is approximately constant (or O(1)) as opposed to scanning a single-element array (which would be O(n)).