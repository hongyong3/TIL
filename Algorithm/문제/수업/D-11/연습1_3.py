import sys
import queue
q = queue.Queue()
q.put(1)
q.put(2)
q.put(3)

print(q.pop(0))
print(q.pop(0))
print(q.pop(0))
if len(q) != 0:
    print(q.pop(0))
print(q)