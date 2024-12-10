from collections import defaultdict

with open('input.txt', 'r') as f:
    data = f.read()

rules, updates = data.split('\n\n')
rules, updates = rules.strip().split('\n'), updates.strip().split('\n')

rules = [ list(map(int, rule.split('|'))) for rule in rules ]
updates = [ list(map(int, update.split(','))) for update in updates ]

ordering = defaultdict(set)
for first, second in rules:
    ordering[first].add(second)

def compare_pages(first, second):
    if second in ordering[first]:
        return -1
    if first in ordering[second]:
        return 1
    return 0

from functools import cmp_to_key

def order_update(update):
    return sorted(update, key=cmp_to_key(compare_pages))

print("Task 1")

correct_updates = [ update for update in updates if update == order_update(update) ]
print(sum([update[len(update)//2] for update in correct_updates]))

print("Task 2")

incorrect_updates = [ order_update(update) for update in updates if update != order_update(update) ]
print(sum([update[len(update)//2] for update in incorrect_updates]))
