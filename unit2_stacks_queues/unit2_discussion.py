"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        self.items = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        #LIFO: pushes a new item to the top/front of the stack and will be the first one to pop.
        self.items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        #Pops the last item added to the stack first and handles exceptions if the stack is empty.
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        #Peeks the last item added to the stack and returns it, handles the exception if the stack is empty.
        if self.is_empty():
            return None
        return self.items[-1]   #[-1] is the last item at the top of the stack.

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return len(self.items) == 0 #Returns true when the stack is empty.


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        self.items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        #FIFO: adds a new item to the back of the queue, and the oldest item will be the first item to pop.
        self.items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        #Checks if the queue is empty, pops the first item in the queue.
        if self.is_empty():
            return None
        return self.items.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        #Front returns the first item in the queue while leaving it there and does not remove it.
        if self.is_empty():
            return None
        return self.items[0] #[0] checks the front of the queue.

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return len(self.items) == 0 #Returns true when the queue is empty.


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    print("\n=== STACK DEMO ===")
    s = Stack() #Creates a new (empty) stack object.
    s.push("Player A")  #Pushes item Player A.
    s.push("Player B")  #Pushes item Player B.
    s.push("Player C")  #Pushes item Player C.
    s.push("Player D")  #Pushes item Player D.
    print("Pushed: Player A, B, C, D")  #Prints All the items (Players) pushed to the stack.

    print("Popped:", s.pop())   #Prints and pops the expected popped item: D.
    print("Peek:", s.peek())    #Prints and peeks the expected item peeked: C.

    print("Popped remaining Players:", s.pop(), s.pop(), s.pop())   #Prints and pops the remaining items (Players C, B, A)
    print("Pop on an empty stack returns:", s.pop())    #Prints and pops on an empty stack.
    print("Peek on an empty stack returns:", s.peek())   #Prints and peeks on an empty stack.

    print("\n=== Single item edge case ===")
    s2 = Stack()    #Creates a new stack object.
    s2.push("Player E")  #Pushes 1 new item into the stack.
    print("Pushed: Player E")   #Prints the new item pushed.
    print("Popped:", s2.pop())   #Prints and pops the only remaining item in the stack.
    print("Stack is empty check:", s2.is_empty())   #Prints and checks the stack is empty.


    # ===============================
    # TODO (Student): QUEUE DEMO
    # ===============================
    print("\n=== QUEUE DEMO ===")
    q = Queue() #Creates a new (empty) queue object.
    q.enqueue("Player 1")   #Enqueues item Player 1.
    q.enqueue("Player 2")   #Enqueues item Player 2.
    q.enqueue("Player 3")   #Enqueues item Player 3.
    q.enqueue("Player 4")   #Enqueues item Player 4.
    print("Queued: Players 1, 2, 3, 4") #Prints all Players enqueued to the queue.

    print("Dequeued:", q.dequeue()) #Dequeues the first item at the front of the queue.
    print("Peek:", q.front())   #Peeks the front item in the queue.

    print("Remaining Players dequeued:", q.dequeue(), q.dequeue(), q.dequeue()) #Dequeues the remaining items in the queue.
    print("Dequeue when the queue is empty returns:", q.dequeue())  #Returns (None) when the queue is empty.
    print("Peek when the queue is empty returns:", q.front())   #Peeks the front of the queue when empty.

    print("\n=== Single item edge case ===")
    q2 = Queue()    #Creates a new queue object.
    q2.enqueue("Player 5")  #Enqueues Player 5.
    print("Queued Player 5")    #Prints Player 5 has been queued.
    print("Dequeued:", q2.dequeue())    #Dequeues the last item in the queue.
    print("Queue is empty check:", q2.is_empty())   #Prints true when the queue is empty.

if __name__ == "__main__":
    main()
