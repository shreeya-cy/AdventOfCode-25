with open("input.txt", "r") as f:
    joltages = f.read()

joltage = joltages.split('\n')
total = 0

for jol in joltage:
    jol = list(jol)
    num = 0
    for i in range(11):
        digit = max(jol[:i-11])
        jol = jol[jol.index(digit)+1:]
        num = num * 10 + int(digit)
    num = num * 10 + int(max(jol))
    total += num

print(total)
