"""
===========================================================
UNIT 7 DISCUSSION: SORTING ALGORITHMS (BUBBLE SORT VS MERGE SORT)
===========================================================

STUDENT INSTRUCTIONS:

This project explores two fundamental sorting algorithms:
- Bubble Sort (iterative, comparison-based)
- Merge Sort (recursive, divide-and-conquer)

Your goal is to demonstrate both your coding ability and your
understanding of algorithm efficiency and behavior.
"""


def bubble_sort(lst):
    """
    TODO (Student):
    Implement Bubble Sort.

    Requirements:
    - Create a copy of the original list.
    - Compare adjacent elements.
    - Swap elements when they are out of order.
    - Continue until the list is sorted.
    - Return the sorted list.
    - Add meaningful comments.

    """
    # work on a copy so the original list is not changed
    result = lst.copy()
    n = len(result)
    # each pass bubbles the largest remaining value toward the end
    for i in range(n - 1):
        # track whether any swap happened this pass (for early stop)
        swapped = False
        # compare adjacent elements, skipping the already-sorted tail
        for j in range(n - 1 - i):
            if result[j] > result[j + 1]:
                # swap the out-of-order neighbors
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        # no swaps means the list is already sorted, so stop early
        if not swapped:
            break
    # two nested loops give bubble sort O(n^2) time complexity
    return result


def merge_sort(lst):
    """
    TODO (Student):
    Implement Merge Sort.

    Requirements:
    - Use recursion.
    - Divide the list into smaller halves.
    - Sort each half recursively.
    - Merge the sorted halves together.
    - Return the sorted list.
    - Add meaningful comments.

    """
    # base case: a list of 0 or 1 element is already sorted
    if len(lst) <= 1:
        return lst
    # divide: split the list into two halves
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])    # recursively sort the left half
    right = merge_sort(lst[mid:])   # recursively sort the right half
    # conquer: merge the two sorted halves back together
    # divide-and-conquer gives merge sort O(n log n) time complexity
    return merge(left, right)


def merge(left, right):
    """
    TODO (Student):
    Implement the merge step used by Merge Sort.

    Requirements:
    - Compare values from the left and right lists.
    - Build a new sorted result list.
    - Append any remaining values.
    - Return the merged sorted list.
    - Add meaningful comments.
    """
    result = []
    i = 0  # position in the left list
    j = 0  # position in the right list
    # take the smaller front value from the two lists each time
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # append any remaining values from whichever list still has some
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def main():
    print("=== UNIT 7: SORTING ALGORITHMS ===")

    # ===============================
    # TODO (Student): DATASET #1
    # ===============================
    #
    # Requirements:
    # 1. Create an unsorted list containing at least 7 values.
    # 2. Display the original list.
    # 3. Sort the list using Bubble Sort.
    # 4. Sort the same list using Merge Sort.
    # 5. Clearly label and display all results.

    # DATASET #1
    print("\n=== DATASET #1 ===")
    data1 = [42, 19, 88, 7, 31, 55, 3]
    print("Original:   ", data1)
    print("Bubble Sort:", bubble_sort(data1))
    print("Merge Sort: ", merge_sort(data1))
    # Both algorithms produce the same sorted order; only the method differs.

    # ===============================
    # TODO (Student): DATASET #2
    # ===============================
    #
    # Requirements:
    # 1. Create a second dataset.
    # 2. Use different values than Dataset #1.
    # 3. Sort using both algorithms.
    # 4. Compare the results.

    # DATASET #2
    print("\n=== DATASET #2 ===")
    data2 = [100, 64, 25, 12, 90, 8, 77, 45]
    print("Original:   ", data2)
    print("Bubble Sort:", bubble_sort(data2))
    print("Merge Sort: ", merge_sort(data2))

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Already sorted list
    # - Reverse-sorted list
    # - List with duplicate values
    # - Single-element list
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    # empty list -> both return an empty list safely
    print("Empty:          Bubble:", bubble_sort([]), "| Merge:", merge_sort([]))
    # already sorted -> bubble sort finishes early after one clean pass
    print("Already sorted: Bubble:", bubble_sort([1, 2, 3, 4]), "| Merge:", merge_sort([1, 2, 3, 4]))
    # duplicates -> both keep every copy and stay stable
    print("Duplicates:     Bubble:", bubble_sort([5, 2, 5, 2, 1]), "| Merge:", merge_sort([5, 2, 5, 2, 1]))
    # single element -> returned unchanged
    print("Single element: Bubble:", bubble_sort([42]), "| Merge:", merge_sort([42]))




if __name__ == "__main__":
    main()