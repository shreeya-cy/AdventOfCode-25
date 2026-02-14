from itertools import combinations

with open('input.txt') as f:
    lines = f.read()

line = lines.split('\n')
indicators = list()
buttons = list()
for l in line:
    comps = l.split(' ')
    indicators.append(comps[0].strip("[]"))
    buttons.append([
        tuple(map(int, s.strip("()").split(",")))
        for s in comps[1:-1]
    ])

total = 0


for i in range(len(indicators)):
    flag = 0
    target = {idx for idx, val in enumerate(indicators[i]) if val == '#'}
    for r in range(1, len(buttons)+1):
        for combo in combinations(buttons[i], r):
            lights = set()
            for c in combo:
                lights ^= set(c)
            if lights == target:
                total += r
                flag = 1
                break

        if flag==1:
            break

print(total)




