"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    #Existing elements shift one to the right.
    #This has worse performance since its shifting everything to the right one which is O(n) vs at the end which is closer to O(1).
    lst.insert(index, value)


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    #Check if the index is within the range of lst.
    if 0 <= index < len(lst):
        #Pops if index is valid and returns the item at index.
        return lst.pop(index)
    #Returns nothing if invalid.
    return None


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    #Checks each element one by one in order.
    for i in range(len(lst)):
        #If the position matches, index is returned.
        if lst[i] == value:
            return i
    #Checks the list with no match and returns.
    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    # INSERTION TESTS: start with a small list, then insert at the beginning,
    # middle, and end. The list is printed after each insert to show how existing
    # elements shift to the right to make room.
    print("\n=== INSERTION TESTS ===")
    songs = ["A", "B", "C"]
    print("Originals:", songs)
    insert_at(songs, 0, "START")
    print("After insert at beginning:", songs)
    insert_at(songs, 2, "MIDDLE")
    print("After insert middle:", songs)
    insert_at(songs, len(songs), "END")
    print("After insert at end:", songs)

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    # DELETION TESTS: remove items from the beginning, middle, and end.
    # delete_at returns the removed value, and the list is printed after each
    # removal to show the remaining elements.
    print("\n=== DELETION TESTS ===")
    print("Removed from beginning:", delete_at(songs, 0))
    print("List now:", songs)
    print("Removed from middle:", delete_at(songs, 2))
    print("List now:", songs)
    print("Removed end:", delete_at(songs, len(songs) -1))
    print("List now:", songs)

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    # SEARCH TESTS: use linear search to find a value that exists (returns its
    # index) and a value that does not exist (returns -1).
    print("\n=== SEARCH TESTS ===")
    print("Search for 'A' (exists):", search_value(songs, "A"))
    print("List now:", songs)
    print("Search for 'Z' (missing):", search_value(songs, "Z"))
    print("List now:", songs)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    # EDGE CASES: test an invalid index (delete_at returns None) and a missing
    # value (search_value returns -1) to show the code handles bad input safely
    # instead of crashing.
    print("\n=== EDGE CASES ===")
    print("Delete at invalid index 99:", delete_at(songs, 99))
    print("Search missing value:", search_value(songs, "nope"))


if __name__ == "__main__":
    main()