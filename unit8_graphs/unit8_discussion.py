"""
===========================================================
UNIT 8 DISCUSSION: BREADTH-FIRST SEARCH (BFS)
===========================================================

STUDENT INSTRUCTIONS:

This assignment is designed to help you understand how graphs
are traversed using Breadth-First Search (BFS) and how this
applies to real-world systems (e.g., networks, routes,
social connections).

===========================================================
"""

from collections import deque


def bfs(graph, start):
    """
    TODO (Student):
    Implement Breadth-First Search (BFS).

    Requirements:
    - Use a queue to manage traversal order.
    - Track visited nodes to prevent revisiting nodes.
    - Visit nodes level by level.
    - Return the order in which nodes were visited.

    Add comments explaining:
    - Why a queue is used.
    - Why neighbors are added to the queue.
    - How BFS differs from depth-first traversal.
    """
    # If the start node is not in the graph there is nothing to
    # traverse, so safely return an empty list (missing-node case).
    if start not in graph:
        return []

    order = [start]          # nodes in the order they are visited
    discovered = {start}     # set of nodes already found (fast lookup)

    # A queue (FIFO) is used so the FIRST node discovered is the FIRST
    # node explored. Processing the oldest node first is what makes BFS
    # fan out level by level, outward from the start, instead of diving
    # deep down one path the way depth-first search does.
    queue = deque([start])

    while queue:
        # Remove the oldest node from the FRONT of the queue.
        node = queue.popleft()
        # Look at every neighbor of the current node.
        for neighbor in graph[node]:
            # Only process neighbors we have not already discovered.
            # This prevents revisiting nodes and avoids infinite loops
            # in a graph that contains cycles.
            if neighbor not in discovered:
                discovered.add(neighbor)   # mark discovered when queued
                order.append(neighbor)     # record the visit order
                queue.append(neighbor)     # add to the BACK for later
    # Neighbors are added to the BACK of the queue so that every node at
    # the current distance is fully processed before any node that is
    # farther away. Depth-first search would instead use a stack (LIFO)
    # and follow one path all the way to its end before backing up.
    return order


def main():
    print("=== UNIT 8: BREADTH-FIRST SEARCH ===")

    # ===============================
    # TODO (Student): CREATE A GRAPH
    # ===============================
    #
    # Requirements:
    # 1. Create a graph using an adjacency list.
    # 2. Include at least 6 nodes.
    # 3. Include multiple connections between nodes.
    # 4. Clearly display the graph structure.
    # 5. Use comments to explain what the nodes and edges represent.

    # Real-world example: a streaming platform's "similar taste" network.
    # Each key is a user (a node). Each user's list holds the other users
    # they share viewing preferences with (the edges). The graph is
    # undirected -- if Ava is linked to Ben, Ben is also linked to Ava --
    # which models a mutual similarity used to drive recommendations.
    graph = {
        "Ava":  ["Ben", "Cam", "Dana"],
        "Ben":  ["Ava", "Eli"],
        "Cam":  ["Ava", "Finn"],
        "Dana": ["Ava", "Eli", "Finn"],
        "Eli":  ["Ben", "Dana", "Gwen"],
        "Finn": ["Cam", "Dana"],
        "Gwen": ["Eli"],
    }

    print("\n=== GRAPH STRUCTURE ===")
    # Display each user and the users they are directly connected to.
    for user, neighbors in graph.items():
        print(f"{user:5} -> {neighbors}")

    # ===============================
    # TODO (Student): BFS TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Select a starting node.
    # 2. Perform BFS traversal.
    # 3. Display the traversal order.
    # 4. Use comments to explain how BFS visits nodes level by level.
    # 5. Add at least one additional node or edge
    #    and demonstrate the updated traversal.

    print("\n=== BFS TRAVERSAL ===")
    start = "Ava"
    # BFS visits Ava first, then every user Ava is directly linked to
    # (her closest taste-matches), then their links, and so on outward.
    print(f"BFS from {start}: {bfs(graph, start)}")
    # Step-by-step by level (distance from Ava):
    #   level 0 = [Ava]
    #   level 1 = [Ben, Cam, Dana]   (Ava's direct connections)
    #   level 2 = [Eli, Finn]        (friends of her connections)
    #   level 3 = [Gwen]             (one step further out)
    # The closest connections -- the best first-pass recommendations --
    # always appear earliest in the traversal.

    # Add a new node AND new edges, then show the updated traversal.
    # A new user, Hana, joins and shares preferences with Finn and Gwen.
    graph["Hana"] = ["Finn", "Gwen"]   # new node with its own edges
    graph["Finn"].append("Hana")       # keep the graph undirected
    graph["Gwen"].append("Hana")
    print(f"BFS from {start} after adding Hana: {bfs(graph, start)}")
    # Hana is three steps away from Ava, so she now appears near the end
    # of the traversal, after everyone who is closer to Ava.

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Start from a different node
    # - Use a disconnected graph
    # - Handle a missing start node safely
    # - Graph containing only one node
    # - Empty graph
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")

    # 1) Different start node: the traversal order depends on where BFS
    #    begins, so starting at Gwen produces a different visit order.
    print("Start from Gwen:        ", bfs(graph, "Gwen"))

    # 2) Missing start node: 'Zoe' is not in the graph, so BFS returns an
    #    empty list instead of crashing with a KeyError.
    print("Missing node (Zoe):     ", bfs(graph, "Zoe"))

    # 3) Disconnected graph: Mia and Nel form their own island with no
    #    link to Ava's group, so BFS from Ava never reaches them. BFS
    #    only visits the nodes reachable from the start node.
    disconnected = {
        "Ava": ["Ben"],
        "Ben": ["Ava"],
        "Mia": ["Nel"],
        "Nel": ["Mia"],
    }
    print("Disconnected (from Ava):", bfs(disconnected, "Ava"))

    # 4) Single-node graph: a lone node with no edges just visits itself.
    print("Single node:            ", bfs({"Solo": []}, "Solo"))



if __name__ == "__main__":
    main()