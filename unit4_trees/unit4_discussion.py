"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.
        self.value = value  #The data this node stores.
        self.left = None    #Left child (smaller values).
        self.right = None   #Right child(larger values).


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.
        self.root = None    #Empty tree with no root.

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        #Start the recursive insert @ root; store the (new value) root back
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        #Base case: empty spot found --> create new node here.
        if node is None:
            return Node(value)
        #Smaller values go to the left subtree.
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        #Larger values go to the right subtree.
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
        #Hand this node back so the level above can re-attach it.
        return node

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        #Start the recursive search @ root
        #BST search is more efficient than a linear search because at each node
        #we compare once and follow only one side, discarding half of the
        #remaining tree each step, instead of check every element in order.
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """

        if node is None:
            return False
        if value == node.value:
            return True
        if value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        #Collect the values into a list during the traversal.
        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        #Base case: nothing to do @ an empty spot.
        #Because every left subtree holds smaller values and every right subtree
        #holds larger ones, visiting left --> current --> right appends the values
        #in ascending order, so an in-order traversal of a BST is always sorted.
        if node is None:
            return
        #1. Visit the left subtree first (all smaller values).
        self._inorder_recursive(node.left, values)
        #2. Record this nodes value.
        values.append(node.value)
        #3. Visit the right subtree (all larger values).
        self._inorder_recursive(node.right, values)


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")
    tree = BST()
    values = [50, 30, 70, 20, 40, 60, 80]   #50 First, then smaller numbers go left, larger ones go right.
    for v in values:
        tree.insert(v)
    print("Inserted values:", values)

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")
    print("In-order (sorted):", tree.inorder()) #Expect: [20, 30, 40, 50, 60, 70, 80]

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")
    print("Search 40 (exists):", tree.search(40))   #True
    print("Search 60 (exists):", tree.search(60))   #True
    print("Search 25 (missing):", tree.search(25))   #False
    print("Search 99 (missing):", tree.search(99))   #False

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")
    empty = BST()
    print("In-order of empty tree:", empty.inorder())   #[]
    print("Search 10 in empty tree:", empty.search(10)) #False



if __name__ == "__main__":
    main()