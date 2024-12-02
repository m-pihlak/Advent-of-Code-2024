import numpy as np
with open('input.txt', 'r') as f:
  data = f.read()

lines = data.strip().split('\n')
reports = [np.array(line.split(' '), dtype=np.int32) for line in lines]

print("Task 1")
def isSafe(level):
    increasing = np.all(level[1:] > level[:-1])
    decreasing = np.all(level[1:] < level[:-1])
    difference = np.all(np.abs(level[1:] - level[:-1]) < 4)
  
    return (increasing or decreasing) and difference

correct = [ level for level in reports if isSafe(level) ]

print(len(correct))

print("Task 2")
wrong = [ level for level in reports if not isSafe(level) ]
new_reports = [ [ np.delete(level, i) for i in range(len(level)) ] for level in wrong ]

new_correct = [ levels for levels in new_reports if len([ level for level in levels if isSafe(level) ]) != 0 ]
print(len(correct) + len(new_correct))
