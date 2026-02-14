with open('input.txt') as f:
    lines = f.read()

line = lines.split('\n')
indicators = list()
buttons = list()
joltage = list()
for l in line:
    comps = l.split(' ')
    indicators.append(comps[0].strip("[]"))
    buttons.append([
        tuple(map(int, s.strip("()").split(",")))
        for s in comps[1:-1]
    ])
    joltage.append(comps[-1].strip('{}'))

print(joltage)