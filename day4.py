import numpy as np

with open('input.txt', 'r') as f:
    data = f.read().strip()

matrix = np.array([ np.array(list(row)) for row in data.split('\n') ])
matrix = np.pad(matrix, 3, 'constant', constant_values=".")

print("Task 1")

goal = np.array(['X', 'M', 'A', 'S'])

def horizontal(x, y):
    return matrix[y:y+4, x]

def vertical(x, y):
    return matrix[y, x:x+4]

def diagonal(x, y):
    return matrix[y:y+4,x:x+4].diagonal()

def reverse_diagonal(x, y):
    return matrix[y:y+4,x:x+4][:, ::-1].diagonal()

def isXMAS(selection):
    return np.array_equal(selection, goal) or np.array_equal(selection[::-1], goal)
options = [horizontal, vertical, diagonal, reverse_diagonal]

XMAS = 0

for y in range(3, len(matrix)-3):
    for x in range(3, len(matrix[0])-3):
        for option in options:
            selection = option(x, y)
            if isXMAS(selection):
                XMAS += 1

print(XMAS)

print("Task 2")

goal = np.array(['M', 'A', 'S'])

def diagonal(x, y):
    return matrix[y:y+3,x:x+3].diagonal()

def reverse_diagonal(x, y):
    return matrix[y:y+3,x:x+3][:, ::-1].diagonal()

def isMAS(selection):
    return np.array_equal(selection, goal) or np.array_equal(selection[::-1], goal)

XMAS = 0

for y in range(3, len(matrix)-3):
    for x in range(3, len(matrix[0])-3):
        diag1 = diagonal(x, y)
        diag2 = reverse_diagonal(x, y)
        if isMAS(diag1) and isMAS(diag2):
            XMAS += 1
print(XMAS)
