"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """
    #Linear search checks each element one at a time from the start.
    for i in range(len(lst)):
        #If this element matches, return its index.
        if lst[i] == target:
            return i
    #Not found after checking every element -> -1.
    return -1
    #O(n): in the worst case, missing or last, it checks all n elements.

def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    low = 0
    high = len(lst) - 1
    #Keep going while there is still a range to search.
    while low <= high:
        mid = (low + high) // 2     #Middle of the current range.
        if lst[mid] == target:
            return mid              #Found.
        elif lst[mid] < target:
            low = mid + 1           #Target bigger -> search right half.
        else:
            high = mid - 1          #Target smaller -> search left half.
    return -1                       #Range emptied -> not found.
    #Each step cuts the remaining range in half -> 0(log n) (divide and conquer).

def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")
    small = [10, 23, 34, 45, 56, 67, 78]        #Must be sorted for binary search.
    print("Small data set:", small)
    print("Linear search for 45:", linear_search(small, 45))    #Exists -> index 3.
    print("Binary search for 45:", binary_search(small, 45))    #Exists -> index 3.
    print("Linear search for 50:", linear_search(small, 50))    #Missing -> -1.
    print("Binary search for 50:", binary_search(small, 50))    #Missing -> -1.

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")
    large = list(range(0, 100000, 2))       #50,000 sorted even numbers.
    target = 99998                          #The last element = worst case for linear.
    print("Large dataset size:", len(large))
    print("Linear search for 99998:", linear_search(large, target))
    print("Binary search for 99998:", binary_search(large, target))
    #Linear had to check -50,000 elements to reach the last one. while binary found it in about log2(50000) -= 16 steps. This is why binary search scales far better as the dataset grows.

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("Binary search on empty list:", binary_search([], 5))                     # -1
    print("Linear search on empty list:", linear_search([], 5))                     # -1
    print("Binary search single element [42] for 42:", binary_search([42], 42))     # 0
    print("Linear search first element (10):", linear_search(small, 10))                # 0
    print("Binary search last element (78):", binary_search(small, 78))                 # 6


if __name__ == "__main__":
    main()