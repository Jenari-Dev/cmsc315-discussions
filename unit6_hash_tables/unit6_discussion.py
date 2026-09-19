"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.

    # A Python dictionary behaves like a hash table: each key is run through a
    # hash function to decide where its value is stored, so lookups by key are
    # very fast (about O(1)). Here the keys are contact names and the values are
    # phone numbers -- a simple real-world phone book.
    print("\n=== INSERT OPERATIONS ===")
    contacts = {
        "Alice": "555-1001",
        "Bob": "555-1002",
        "Carol": "555-1003",
        "Dave": "555-1004",
        "Erin": "555-1005",
    }
    print("Contacts:", contacts)

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.
    
    # A lookup hashes the key and jumps straight to its value, with no scanning.
    print("\n=== LOOKUP OPERATIONS ===")
    print("Alice's number:", contacts["Alice"])
    print("Carol's number:", contacts["Carol"])

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    # Assigning to an existing key replaces its value; no duplicate key is made.
    print("\n=== UPDATE OPERATIONS ===")
    print("Before update - Bob:", contacts["Bob"])
    contacts["Bob"] = "555-9999"
    print("After update  - Bob:", contacts["Bob"])

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    # del removes the key and its value from the dictionary entirely.
    print("\n=== DELETE OPERATIONS ===")
    print("Before delete:", contacts)
    del contacts["Dave"]
    print("After delete: ", contacts)


    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")
    # Edge case 1: look up a missing key safely with get(), which returns None
    # instead of raising a KeyError.
    print("Lookup missing key 'Zed':", contacts.get("Zed"))
    # Edge case 2: delete a missing key safely with pop() plus a default value,
    # which returns the default instead of raising an error.
    print("Delete missing key 'Zed':", contacts.pop("Zed", "Not found"))
    # Edge case 3: check membership before accessing to avoid a KeyError.
    print("Is 'Alice' a key?", "Alice" in contacts)



if __name__ == "__main__":
    main()