from collections import deque

# Initializing a queue
q = deque()

# Adding elements to a queue
q.append('g')
q.append('f')
q.append('g')

print("Initial queue")
print(q)

# Removing elements from a queue
print("\nElements dequeued from the queue")
print(q.popleft())
print(q.popleft())
print(q.popleft())

print("\nQueue after removing elements")
print(q)

# Uncommenting q.popleft()
# will raise an IndexError
# as queue is now empty
