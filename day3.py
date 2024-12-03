import re
with open('input.txt', 'r') as f:
    data = f.read()

print("Task 1")
print(sum([ int(x) * int(y) for x, y in re.findall("mul\(([0-9]+),([0-9]+)\)", data)]))

print("Task 2")
split_by_do = data.split("do()")
split_by_do_dont = [ do.split("don't()") for do in split_by_do ]
total = 0
for do_dont in split_by_do_dont:
    do = do_dont[0]
    total += sum([ int(x) * int(y) for x, y in re.findall("mul\(([0-9]+),([0-9]+)\)", do)])

print(total)
