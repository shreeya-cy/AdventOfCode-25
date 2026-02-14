import re

with open('input.txt') as f:
    lines = f.read()

pound_counts = {0: 7, 1: 7, 2: 7, 3: 6, 4: 7, 5: 5}

line = lines.split('\n\n')[-1].splitlines()
count = 0

for l in line:
    x, y, *counts = list(map(int, re.findall(r"\d+", l)))
    total = 0
    for i in range(6):
        total = total + (counts[i]*pound_counts[i])
    if total <= (x*y):
        count+=1

print(count)

