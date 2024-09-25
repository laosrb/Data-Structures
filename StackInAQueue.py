class Queue:
"""From CSC 2720 – Data Structures Lecture 7 ArrayQueue Class"""
    def __init__(self):
        # Initialize empty queue
        self.items = []
    
    def enqueue(self, item):
        # responsible for the push method
        self.items.append(item)
    
    def dequeue(self):
        # responsible for the pop method
        if not self.is_empty():
            return self.items.pop(0)
        print("Dequeue from an empty queue")
    
    def is_empty(self):
        # Check if they queue is empty
        return len(self.items) == 0
    
    def size(self):
        # Responsible for the __len__ method
        return len(self.items)
    
    def front(self):
        # Responsible for the top method
        if not self.is_empty():
            return self.items[0]
        print("Front from an empty queue")

class StackInAQueue:
    def __init__(self):
        self.q = Queue()

    def push(self, item):
        # pushes element in stack queue
        self.q.enqueue(item)    # SPACE COMPLEXITY .append method
        for i in range(self.q.size() - 1):
            self.q.enqueue(self.q.dequeue())

    def pop(self):
        # pops element and returns 
        if self.q.is_empty():
            print("Pop from an empty stack")
        return self.q.dequeue()

    def top(self):
        if self.q.is_empty():
            print("Top from an empty stack")
        return self.q.front()

    def __len__(self):
        return self.q.size()

    def push_k_items(self, k, items):
        # pushes 'k' number of items at once
        if k > len(self):
            # assume k <= current_size_of_the_stack
            print("k cannot be greater than the current size of the stack")
        
        for item in items:
            # Iterates over the items list and call 
            self.q.enqueue(item)
        
        size = self.q.size()
        for i in range(size - k):    # Same Time Complexity as push method
            self.q.enqueue(self.q.dequeue())


# Example 1:
stack = StackInAQueue()
print(stack.pop())
#stack.push(element)
stack.push(1)
stack.push(2)
print(stack.pop()) # Output = 2
stack.push_k_items(1, [1, 2, 3])
# stack.push_k_items(k, [list])
print(stack.pop())  # Output = 3

# Example 2:
print("\n\nNew Example:")
stack1 = StackInAQueue()
stack1.push(10)
stack1.push(20)
stack1.push(30)
print(stack1.pop())    # Output = 30
