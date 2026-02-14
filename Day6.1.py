with open('input.txt') as f:
    problems = f.read()
problems = problems.split('\n')

mat = []
for p in problems:
    prob = p.split()
    mat.append(prob)
cols = list(zip(*mat))

total = 0
for *nums, op in cols:
    eq = op.join(nums)
    total+=eval(eq)

print(total)