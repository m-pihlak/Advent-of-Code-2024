import numpy as np
with open('input.txt', 'r') as f:
  data = f.read()
lines = data.strip().split('\n')
pairs = [line.split('   ') for line in lines]

lists = list(zip(*pairs))
left = np.sort(np.array(lists[0], dtype=np.int32))
right = np.sort(np.array(lists[1], dtype=np.int32))

print("Task 1")
print(np.sum(np.abs(left - right)))

print("Task 2")
counts = np.bincount(right)
possible = left[left < len(counts)]
print(np.sum(possible*counts[possible]))
