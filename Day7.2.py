from functools import cache

with open('input.txt') as f:
    dig = f.read()
digs = dig.split('\n')
count=0
mat = []
for d in digs:
    d = list(d)
    mat.append(d)
row = len(mat)
cols = len(mat[0])

# Finding the location of S
r = 0
c = 0
for i in range(cols):
    if mat[0][i] == 'S':
        c = i

@cache
def solve(r,c):
    if r >= row:
        return 1
    if mat[r][c]=='.' or mat[r][c]=='S':
        return solve(r+1,c)
    if mat[r][c]=='^':
        return solve(r, c-1) + solve(r, c+1)

print(solve(r,c))