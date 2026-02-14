from functools import cache

with open('input.txt') as f:
    lines = f.read()

line = lines.split('\n')
d = dict()
for l in line:
    key, values = l.split(':')
    d[key] = [x for x in values.strip().split(' ')]

@cache
def find(key, value):
    if key == value:
        return 1
    return sum(find(x, value) for x in d.get(key,[]))

print(find('you','out'))

# Part 2

print(find('svr','dac') * find('dac', 'fft') * find('fft', 'out')+\
      find('svr','fft') * find('fft','dac') * find('dac','out'))

